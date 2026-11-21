"""Replay the finite checks on an isolated copy of the public inputs."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time


if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")

HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_call(command, cwd, *, stdin=None, stdout=subprocess.PIPE, env=None):
    process = subprocess.run(
        command, cwd=cwd, stdin=stdin, stdout=stdout, stderr=subprocess.PIPE, env=env
    )
    if process.returncode:
        detail = (process.stderr or process.stdout or b"").decode(errors="replace").strip()
        raise RuntimeError(f"{command[-1]} exited with status {process.returncode}\n{detail}")
    return process


def check_inputs(reference):
    for filename, expected in reference["input_sha256"].items():
        require(digest((HERE / filename).read_bytes()) == expected, f"Input SHA-256 mismatch for {filename}")


def python_checks(work, reference):
    # Some source programs write beside their companion tables. Every write is to the scratch copy.
    env = {key: value for key, value in os.environ.items() if not key.startswith("PYTHON")}
    env["PYTHONNOUSERSITE"] = "1"
    for check in reference["checks"]:
        if check["output"] != "stdout":
            (work / check["output"]).unlink(missing_ok=True)
        if "write_stdout_to" in check:
            (work / check["write_stdout_to"]).unlink(missing_ok=True)
        start = time.monotonic()
        result = checked_call([sys.executable, "-B", check["script"]], work, env=env)
        raw = result.stdout if check["output"] == "stdout" else (work / check["output"]).read_bytes()
        if check["format"] == "json":
            value = json.loads(raw)
            # Compression headers can vary. The second census reader verifies the fresh compressed
            # bytes and the reference binds the decompressed deterministic certificate stream.
            for field in check.get("omit_from_comparison", []):
                del value[field]
            if "expected_result" in check:
                require(value == check["expected_result"], f"Result table mismatch in {check['script']}")
            normalized = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
        else:
            normalized = raw
        require(digest(normalized) == check["sha256"], f"Result mismatch in {check['script']}")
        if "write_stdout_to" in check:
            (work / check["write_stdout_to"]).write_bytes(raw)
        elapsed = time.monotonic() - start
        print(f"PASS {check['script']}  {check['summary']}  ({elapsed:.1f} s)", flush=True)


def compiler_command():
    system = Path("/usr/bin/clang")
    compiler = str(system) if system.is_file() else shutil.which("clang")
    if not compiler:
        raise RuntimeError("The order-nine and order-ten checks require an installed Clang C compiler.")
    return compiler


def run_augmentation(work, order, data, expected):
    count = len(data.read_bytes().splitlines()) * 2 ** (order - 1)
    require(count == expected["extensions"], f"Unexpected number of order-{order} input extensions")
    start = time.monotonic()
    print(f"Running order {order} on {count:,} single-vertex extensions.", flush=True)
    with data.open("rb") as source:
        result = checked_call(["./fast"], work, stdin=source)
    require(result.stdout == b"", f"Unexpected tight support at order {order}")
    message = result.stderr.decode("ascii").strip()
    match = re.fullmatch(
        rf"N={order} shard 0/1: triangle-connected spanning candidates=(\d+) exact-nu=(\d+) "
        r"tau-checks=(\d+) tight=(\d+)", message
    )
    require(match, f"Unexpected order-{order} summary: {message}")
    fields = ("candidates", "exact_packing", "exact_cover", "tight")
    require(tuple(map(int, match.groups())) == tuple(expected[k] for k in fields), message)
    print(f"PASS {message}  ({time.monotonic() - start:.1f} s)", flush=True)


def native_census(work, reference, max_order):
    compiler = compiler_command()
    shutil.copyfile(work / "data/graph8.g6", work / "graph8.g6")
    if max_order == 10:
        checked_call([compiler, "-O3", "-std=c11", "canon.c", "-o", "canon"], work)
    checked_call([compiler, "-O3", "-std=c11", "fast.c", "-o", "fast"], work)
    if max_order == 10:
        expected = reference["order_nine_catalogue"]
        catalogue = work / "c9.g6"
        with (work / "graph8.g6").open("rb") as source, catalogue.open("wb") as output:
            result = checked_call(["./canon"], work, stdin=source, stdout=output)
        generation = result.stderr.decode("ascii").strip()
        require(generation == (
            f"n=9 generated={reference['augmentation']['9']['extensions']} distinct={expected['rows']} "
            f"(canonical {expected['canonical']}, uncanonized {expected['fallback']}; "
            f"fallback events {expected['fallback']})"
        ), f"Unexpected catalogue summary: {generation}")
        shasum = "/usr/bin/shasum" if Path("/usr/bin/shasum").is_file() else shutil.which("shasum")
        if not shasum:
            raise RuntimeError("The manual order-ten check requires the shasum utility.")
        result = checked_call([shasum, "-a", "256", "c9.g6"], work)
        require(result.stdout.decode("ascii").split() == [expected["sha256"], "c9.g6"],
                "Order-nine catalogue SHA-256 mismatch")
        raw = catalogue.read_bytes()
        require(len(raw.splitlines()) == expected["rows"] and digest(raw) == expected["sha256"],
                "Order-nine catalogue failed the independent row-count and SHA-256 checks")
        print(f"PASS c9.g6  {expected['rows']:,} rows  SHA-256 {expected['sha256']}", flush=True)
    run_augmentation(work, 9, work / "graph8.g6", reference["augmentation"]["9"])
    if max_order == 10:
        run_augmentation(work, 10, work / "c9.g6", reference["augmentation"]["10"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-order", type=int, choices=(9, 10), default=9,
                        help="largest census order, defaults to 9")
    args = parser.parse_args()
    reference = json.loads((HERE / "reference.json").read_text(encoding="utf-8"))
    check_inputs(reference)
    start = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="triangle-census-") as directory:
        work = Path(directory) / "verification"
        shutil.copytree(HERE, work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        python_checks(work, reference)
        native_census(work, reference, args.max_order)
    print(f"All finite checks through order {args.max_order} passed in {time.monotonic() - start:.1f} s.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError) as exc:
        sys.exit(f"FAIL {exc}")

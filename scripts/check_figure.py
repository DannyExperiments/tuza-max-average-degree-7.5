"""Check the fan figure's HTML data, content security policy, and drawn incidences."""

import argparse
import base64
import hashlib
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from itertools import combinations
from pathlib import Path


VISUALS = Path(__file__).resolve().parents[1] / "visuals"
VERTICES = set("axbcz")
RIMS = ("xbcz", "bczx")
SVG = "{http://www.w3.org/2000/svg}"


def require(condition, message):
    if not condition:
        raise ValueError(message)


class ViewerHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.policies = []
        self.scripts = {}
        self.current = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "content-security-policy":
            self.policies.append(attrs["content"])
        if tag == "script":
            require(len(self.policies) == 1, "Expected one CSP before both scripts")
            require("src" not in attrs, "Viewer scripts must be inline")
            if attrs.get("id") == "fan-data":
                require(attrs.get("type") == "application/json", "fan-data must be JSON")
                kind = "data"
            else:
                require(attrs.get("type", "") in ("", "text/javascript", "application/javascript", "module"),
                        "Unexpected viewer script type")
                kind = "executable"
            require(kind not in self.scripts, f"Duplicate {kind} script")
            self.current = kind
            self.scripts[kind] = []

    def handle_data(self, text):
        if self.current is not None:
            self.scripts[self.current].append(text)

    def handle_endtag(self, tag):
        if tag == "script":
            self.current = None


def viewer_fans(path):
    html = ViewerHTML()
    html.feed(path.read_text(encoding="utf-8"))
    html.close()
    require(html.current is None and set(html.scripts) == {"data", "executable"},
            "Expected one closed fan-data script and one inline executable")
    require(len(html.policies) == 1, "Expected exactly one content security policy")
    code = "".join(html.scripts["executable"]).encode("utf-8")
    digest = base64.b64encode(hashlib.sha256(code).digest()).decode("ascii")
    directives = {}
    for field in html.policies[0].split(";"):
        words = field.split()
        if words:
            name = words[0].lower()
            require(name not in directives, f"Duplicate CSP directive {name}")
            directives[name] = words[1:]
    require(directives.get("script-src") == [f"'sha256-{digest}'"], "Inline script hash mismatch")
    require(directives.get("default-src") == ["'none'"] and directives.get("connect-src") == ["'none'"],
            "Default resources and network connections must be disabled")
    for name, values in directives.items():
        if name == "script-src":
            continue
        if name == "style-src":
            require(values in (["'unsafe-inline'"], ["'none'"]), "Styles may not load external resources")
        else:
            require(values == ["'none'"] and name not in ("report-uri", "report-to"),
                    f"Unexpected network or policy source in {name}")

    data = json.loads("".join(html.scripts["data"]))
    require(data["center"] == "a" and set(data["vertices"]) == VERTICES, "Wrong center or vertices")
    positions = list(data["vertices"].values())
    for xyz in positions:
        require(isinstance(xyz, list) and len(xyz) == 3 and
                all(type(x) in (int, float) and math.isfinite(x) for x in xyz),
                "Each vertex needs three finite 3D coordinates")
    require(len({tuple(xyz) for xyz in positions}) == 5, "Two model vertices coincide")
    require(len(data["rims"]) == 2, "Expected two selected rim paths")
    fans = []
    for rim, expected in zip(data["rims"], RIMS):
        require(isinstance(rim, list) and rim in (list(expected), list(reversed(expected))),
                f"Expected rim path {expected} up to reversal")
        edges = {mark("a" + v, 2) for v in rim}
        pages = set()
        for u, v in zip(rim, rim[1:]):
            edges.add(mark(u + v, 2))
            pages.add(mark("a" + u + v, 3))
        require(len(edges) == 7 and triangles(edges) == pages, "Rim data does not give the three fan pages")
        fans.append((edges, pages))
    first, second = (fan[0] for fan in fans)
    require(first - second == {"bx"} and second - first == {"xz"} and len(first & second) == 6,
            "The two fans must exchange bx and xz and share six edges")
    return fans


def mark(value, size):
    require(isinstance(value, str) and len(value) == size and len(set(value)) == size
            and set(value) <= VERTICES, f"Invalid {size}-vertex incidence {value!r}")
    return "".join(sorted(value))


def triangles(edges):
    return {"".join(t) for t in combinations(sorted(VERTICES), 3)
            if all("".join(side) in edges for side in combinations(t, 2))}


def point(x, y):
    xy = (float(x), float(y))
    require(all(math.isfinite(v) for v in xy), "Nonfinite drawing coordinate")
    return xy


def unique_group(root, group_id):
    groups = [g for g in root.iter(SVG + "g") if g.get("id") == group_id]
    require(len(groups) == 1, f"Expected one SVG group named {group_id}")
    return groups[0]


def check_drawing(group, fan):
    expected_edges, expected_faces = fan
    for attribute, tag in (("data-edge", "line"), ("data-face", "polygon"),
                           ("data-point", "circle"), ("data-vertex", "text")):
        require(all(el.tag == SVG + tag for el in group.iter() if attribute in el.attrib),
                f"{attribute} must be attached to an SVG {tag}")
    drawn = {}
    for line in group.iter(SVG + "line"):
        key = mark(line.get("data-edge"), 2)
        ends = {point(line.attrib["x1"], line.attrib["y1"]), point(line.attrib["x2"], line.attrib["y2"])}
        require(key not in drawn and len(ends) == 2, f"Duplicate or collapsed line {key}")
        drawn[key] = ends
    require(set(drawn) == expected_edges, "Drawn edge set differs from the viewer data")
    positions = {}
    for v in VERTICES:
        incident = [ends for edge, ends in drawn.items() if v in edge]
        common = set.intersection(*incident)
        require(len(common) == 1, f"The lines labeled with {v} do not meet at one point")
        positions[v] = common.pop()
    require(len(set(positions.values())) == 5, "Two drawn vertices coincide")
    dots = list(group.iter(SVG + "circle"))
    require(len(dots) == 5 and {c.get("data-point") for c in dots} == VERTICES, "Wrong node circles")
    for dot in dots:
        label = dot.attrib["data-point"]
        require(point(dot.attrib["cx"], dot.attrib["cy"]) == positions[label],
                f"Node {label} differs from its incident line endpoints")
    labels = [t for t in group.iter(SVG + "text") if "data-vertex" in t.attrib]
    require(len(labels) == 5 and {t.get("data-vertex") for t in labels} == VERTICES, "Wrong vertex labels")
    for label in labels:
        require("".join(label.itertext()).strip() == label.get("data-vertex"), "Displayed vertex label differs")

    faces = set()
    for poly in group.iter(SVG + "polygon"):
        key = mark(poly.get("data-face"), 3)
        coords = re.split(r"[\s,]+", poly.attrib["points"].strip())
        require(len(coords) == 6, f"Face {key} needs three coordinate pairs")
        corners = {point(x, y) for x, y in zip(coords[::2], coords[1::2])}
        require(key not in faces and corners == {positions[v] for v in key}, f"Incorrect triangular face {key}")
        faces.add(key)
    require(faces == expected_faces == triangles(drawn), "Polygons differ from the actual graph triangles")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rendered", type=Path, nargs=3, metavar=("FIRST", "SECOND", "BOTH"),
                        help="also check three SVG DOM exports from the viewer's three modes")
    args = parser.parse_args()
    fans = viewer_fans(VISUALS / "high-fans.html")
    root = ET.parse(VISUALS / "high-fans.svg").getroot()
    require(root.tag == SVG + "svg", "Expected an SVG figure")
    for i, fan in enumerate(fans, 1):
        check_drawing(unique_group(root, f"fan-{i}"), fan)
    if args.rendered:
        both = (fans[0][0] | fans[1][0], fans[0][1] | fans[1][1])
        for path, drawing in zip(args.rendered, [*fans, both]):
            check_drawing(unique_group(ET.parse(path).getroot(), "geometry"), drawing)
    print("Two labeled seven-edge fans verified, three pages each, six common edges, bx exchanged for xz.")
    print("3D data, SVG nodes and face corners agree. The inline script matches its offline CSP.")


if __name__ == "__main__":
    try:
        main()
    except (KeyError, TypeError, ValueError, OSError, ET.ParseError) as error:
        sys.exit(f"Figure verification failed: {error}")

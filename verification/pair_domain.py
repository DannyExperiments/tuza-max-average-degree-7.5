"""Marked one-defect two-hub graph domain, with Gupta's vertex labels."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from itertools import permutations, product

import check_gupta as prior


C = (2, 3, 4, 5)
A = (6, 7)
B = (8, 9)
edge = lambda a, b: tuple(sorted((a, b)))
CORE = tuple((a + 2, b + 2) for a, b in prior.CORE)
LEFT = tuple((a + 2, b + 2) for a, b in prior.SIDE)
RIGHT = tuple((a, b + 2) if a < 6 else (a + 2, b + 2) for a, b in LEFT)
OPTIONAL = CORE + LEFT + RIGHT
BITS = {e: 1 << i for i, e in enumerate(OPTIONAL)}
BASE = {(0, 1)} | {(u, x) for x in C for u in (0, 1)} | {(0, x) for x in A} | {(1, x) for x in B}
CROSS = tuple(product(A, B))
ALLMASK = (1 << len(OPTIONAL)) - 1


def graph(key):
    return BASE | {pair for pair, bit in BITS.items() if key & bit}


def encoded(edges):
    return sum(BITS[e] for e in set(edges) if e in BITS)


def labellings():
    for c in permutations(C):
        for a, b, swap in product(permutations(A), permutations(B), (False, True)):
            yield ((1, 0) + c + b + a) if swap else ((0, 1) + c + a + b)


def transforms():
    # Map a 24-bit encoding by three 8-bit lookup tables.
    for perm in labellings():
        newbits = [BITS[edge(perm[a], perm[b])] for a, b in OPTIONAL]
        table = []
        for shift in range(0, 24, 8):
            row = [0] * 256
            for i in range(1, 256):
                low = i & -i
                row[i] = row[i ^ low] | newbits[shift + low.bit_length() - 1]
            table.append(row)
        yield perm, table


def transform(mask, table):
    return table[0][mask & 255] | table[1][(mask >> 8) & 255] | table[2][mask >> 16]

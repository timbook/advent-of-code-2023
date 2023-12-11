import numpy as np
from itertools import combinations

lines = open('data/input.txt').readlines()
mx = np.array([list(row.strip()) for row in lines])
R, C = mx.shape

null_rows = [i for i in range(R) if np.all(mx[i] == '.')]
null_cols = [i for i in range(C) if np.all(mx[:, i] == '.')]

xs, ys = np.where(mx == '#')

#  galaxies = [(r, c) for r, c in zip(xs, ys)]

galaxies = []
for r, c in zip(xs, ys):
    # How many columns to expand?
    n_cols = sum(1 for nc in null_cols if nc < c)
    n_rows = sum(1 for nr in null_rows if nr < r)

    galaxies.append((r + n_rows, c + n_cols))

def l1(a, b):
    return abs(a[1] - b[1]) + abs(a[0] - b[0])

sol = sum(l1(g1, g2) for g1, g2 in combinations(galaxies, 2))

print(f"A ::: {sol}")

galaxies_1m = []
for r, c in zip(xs, ys):
    N_EXPAND = 1_000_000
    n_cols = (N_EXPAND - 1)*sum(1 for nc in null_cols if nc < c)
    n_rows = (N_EXPAND - 1)*sum(1 for nr in null_rows if nr < r)

    galaxies_1m.append((r + n_rows, c + n_cols))

sol = sum(l1(g1, g2) for g1, g2 in combinations(galaxies_1m, 2))

print(f"B ::: {sol}")

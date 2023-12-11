import numpy as np
from scipy.special import comb

x = np.loadtxt('data/input.txt', dtype=int, delimiter=' ')
R, C = x.shape

def get_d(row):
    for d in range(1, C):
        if np.all(np.diff(row, d) == 0):
            return d

next_vals = []
for row in x:
    d = get_d(row)
    tot = -sum((-1)**k * comb(d, k, exact=True) * row[-k] for k in range(1, d + 1))
    next_vals.append(tot)

sol = sum(next_vals)
print(f"A ::: {sol}")

next_vals = []
for row in x:
    row_inv = row[::-1]
    d = get_d(row_inv)
    tot = -sum((-1)**k * comb(d, k, exact=True) * row_inv[-k] for k in range(1, d + 1))
    next_vals.append(tot)

sol = sum(next_vals)
print(f"B ::: {sol}")

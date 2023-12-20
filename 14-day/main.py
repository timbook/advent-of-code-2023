import numpy as np

raw = open('data/input.txt').readlines()

mx = np.array([list(line.strip()) for line in raw])

class Platform:
    def __init__(self, mx):
        self.grid = mx

    def tilt_north(self):
        R, C = self.grid.shape
        mx_new = np.zeros_like(self.grid)
        for c in range(C):
            col = self.grid[:, c]
            col_str = ''.join(col)
            col_spl = col_str.split('#')
            col_sort = [''.join(sorted(s, reverse=True)) for s in col_spl]
            col_join = '#'.join(col_sort)
            mx_new[:, c] = list(col_join)
        self.grid = mx_new

    def tilt_west(self):
        R, C = self.grid.shape
        mx_new = np.zeros_like(self.grid)
        for r in range(R):
            row = self.grid[r, :]
            row_str = ''.join(row)
            row_spl = row_str.split('#')
            row_sort = [''.join(sorted(s, reverse=True)) for s in row_spl]
            row_join = '#'.join(row_sort)
            mx_new[r, :] = list(row_join)
        self.grid = mx_new

    def tilt_south(self):
        self.grid = self.grid[::-1, :]
        self.tilt_north()
        self.grid = self.grid[::-1, :]

    def tilt_east(self):
        self.grid = self.grid[:, ::-1]
        self.tilt_west()
        self.grid = self.grid[:, ::-1]

    def cycle(self):
        self.tilt_north()
        self.tilt_west()
        self.tilt_south()
        self.tilt_east()

    def get_score(self):
        R = self.grid.shape[0]
        score = 0
        for i, row in enumerate(self.grid):
            n = np.sum(row == 'O')
            score += n*(R - i)
        self.score = score
        return self.score

    def show(self):
        rows = [''.join(row) for row in self.grid]
        print('\n'.join(rows))

plat = Platform(mx)
plat.tilt_north()
plat.get_score()
sol = plat.score
print(f"A ::: {sol}")

plat = Platform(mx)
scores = []
for i in range(500):
    plat.cycle()
    plat.get_score()
    scores.append(plat.score)

# Find cycle len
last = scores[-1]
cycle_len = scores[:-1][::-1].index(last) + 1

cycle = scores[-(cycle_len + 1):-1]

B = 1_000_000_000
sol = cycle[(B - 500) % cycle_len]
print(f"B ::: {sol}")

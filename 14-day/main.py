import numpy as np
import re

raw = open('data/sample.txt').readlines()
#  raw = open('data/input.txt').readlines()

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

    def get_score(self):
        R = self.grid.shape[0]
        score = 0
        for i, row in enumerate(self.grid):
            n = np.sum(row == 'O')
            score += n*(R - i)
        self.score = score

plat = Platform(mx)
plat.tilt_north()
plat.get_score()
sol = plat.score
print(f"A ::: {sol}")

# Roll the rocks NWSE, then score after 1_000_000_000 cycleso

#  After 1 cycle:
#  .....#....
#  ....#...O#
#  ...OO##...
#  .OO#......
#  .....OOO#.
#  .O#...O#.#
#  ....O#....
#  ......OOOO
#  #...O###..
#  #..OO#....

#  After 2 cycles:
#  .....#....
#  ....#...O#
#  .....##...
#  ..O#......
#  .....OOO#.
#  .O#...O#.#
#  ....O#...O
#  .......OOO
#  #..OO###..
#  #.OOO#...O

#  After 3 cycles:
#  .....#....
#  ....#...O#
#  .....##...
#  ..O#......
#  .....OOO#.
#  .O#...O#.#
#  ....O#...O
#  .......OOO
#  #...O###.O
#  #.OOO#...O

# Sample solution after 1B cycles = 64

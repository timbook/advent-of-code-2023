import numpy as np

data_raw = open('data/input.txt').read()
blocks_raw = data_raw.split('\n\n')
blocks = [np.array([list(row) for row in block.split()]) for block in blocks_raw]

class Field:
    def __init__(self, block):
        self.grid = block

    def scan_by_row(self, transpose=False, diff=0):
        X = self.grid.T if transpose else self.grid
        R = X.shape[0]

        for r in range(1, R):
            top, bot = X[:r, :], X[r:, :]
            M = min(top.shape[0], bot.shape[0])
            top, bot = X[r - M:r, :], X[r:r + M, :]
            
            if np.sum(~(top == bot[::-1, :])) == diff:
                return r

    def scan_a(self):
        row_scan = self.scan_by_row()
        if row_scan:
            return 100*row_scan
        else:
            col_scan = self.scan_by_row(transpose=True)
            return col_scan

    def scan_b(self):
        row_scan = self.scan_by_row(diff=1)
        if row_scan:
            return 100*row_scan
        else:
            col_scan = self.scan_by_row(transpose=True, diff=1)
            return col_scan

fields = [Field(block) for block in blocks]
values = [f.scan_a() for f in fields]
sol = sum(values)

print(f"A ::: {sol}")

values = [f.scan_b() for f in fields]
sol = sum(values)

print(f"B ::: {sol}")

import numpy as np

data_raw = np.loadtxt('data/input.txt', dtype=str, comments=None)
data = np.array([list(r) for r in data_raw])
R, C = data.shape

class Number:
    def __init__(self):
        self.digits = []
        self.coords = []
        self.nb_coords = set()

    def add_digit(self, x):
        self.digits.append(x)

    def add_coord(self, r, c):
        self.coords.append((r, c))

    def is_engine_part(self):
        for r, c in self.coords:
            nb_coords = [
                (r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r    , c - 1),             (r    , c + 1),
                (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)
            ]
            nb_coords = [(r0, c0) for r0, c0 in nb_coords if 0 <= r0 <= R - 1 and 0 <= c0 <= C - 1]

            # Add new coords to set of all nb coords
            for coords in nb_coords:
                self.nb_coords.add(coords)
            self.nb_coords = self.nb_coords - set(self.coords)

            for r_nb, c_nb in nb_coords:
                val = data[r_nb, c_nb]
                if val not in '0123456789.':
                    return True
        return False

    def __repr__(self):
        return ''.join(self.digits)

    @property
    def value(self):
        return int(''.join(self.digits))

# Create list of numbers with coords
numbers = []
for r, row in enumerate(data):
    n = Number()
    for c, val in enumerate(row):
        if val.isdigit():
            n.add_digit(val)
            n.add_coord(r, c)
        elif n.digits:
            numbers.append(n)
            n = Number()

    if n.digits:
        numbers.append(n)

# Filter down to ones only next to symbols
engine_parts = [n for n in numbers if n.is_engine_part()]
sol = np.sum([p.value for p in engine_parts])
print(f"A ::: {sol}")

# List of gears
gears = [(r, c) for r, c in zip(*np.where(data == '*'))]
gear_ratios = []
for g_coord in gears:
    adj_numbers = [n for n in numbers if g_coord in n.nb_coords]
    if len(adj_numbers) == 2:
        n1, n2 = adj_numbers
        gear_ratios.append(n1.value*n2.value)

sol = sum(gear_ratios)
print(f"B ::: {sol}")

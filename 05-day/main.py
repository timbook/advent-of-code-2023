import numpy as np

#  data_raw = open('data/sample.txt').read()
data_raw = open('data/input.txt').read()
data = data_raw.split('\n\n')
seeds_raw = data[0]
seeds = [int(n) for n in seeds_raw.replace('seeds: ', '').split()]

class Map:
    def __init__(self, blob):
        numbers_flat = blob.split(':')[1].strip()
        self.array = np.fromstring(numbers_flat, sep=' ', dtype=int).reshape(-1, 3)

    def __repr__(self):
        output = '\n'.join([
            str(row).replace('[', '').replace(']', '')
            for row in self.array
        ])
        return output

    def pass_value(self, x):
        for D, S, L in self.array:
            if S <= x <= S + L - 1:
                return x - (S - D)
        return x

    def invert_pass(self, y):
        for D, S, L in self.array:
            if D <= y <= D + L - 1:
                return y + (S - D)
        return y

class Almanac:
    def __init__(self, maps):
        self.maps = maps
        self.cache = {}

    def pass_through(self, x):
        input_ = x
        for m in maps:
            x = m.pass_value(x)
        self.cache[input_] = x

    def invert_pass(self, y):
        output_ = y
        for m in maps[::-1]:
            y = m.invert_pass(y)
        return y

maps = [Map(d) for d in data[1:]]
almanac = Almanac(maps)

for s in seeds:
    almanac.pass_through(s)

sol = min(almanac.cache.values())
print(f"A ::: {sol}")

seed_pairs = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

def is_from_seed(x):
    for s, l in seed_pairs:
        if s <= x <= s + l - 1:
            return True
    return False

loc = 0
# Get millions digit
while True:
    possible_seed = almanac.invert_pass(loc)
    if is_from_seed(possible_seed):
        break
    loc += 1_000_000

loc -= 1_000_000
# Increment by 10K
while True:
    possible_seed = almanac.invert_pass(loc)
    if is_from_seed(possible_seed):
        break
    loc += 10_000

loc -= 10_000
# Increment by 1
while True:
    possible_seed = almanac.invert_pass(loc)
    if is_from_seed(possible_seed):
        break
    loc += 1
    
sol = loc
print(f"B ::: {sol}")

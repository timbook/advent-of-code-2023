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

class Almanac:
    def __init__(self, maps):
        self.maps = maps
        self.cache = {}

    def pass_through(self, x):
        input_ = x
        for m in maps:
            x = m.pass_value(x)
        self.cache[input_] = x

maps = [Map(d) for d in data[1:]]
almanac = Almanac(maps)

# Test
for s in seeds:
    almanac.pass_through(s)

sol = min(almanac.cache.values())
print(f"A ::: {sol}")

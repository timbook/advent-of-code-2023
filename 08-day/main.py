import re
from itertools import cycle
from math import gcd

lines = open('data/input.txt').readlines()

steps = cycle(lines[0].strip())

nodes_raw = lines[2:]

class Node:
    def __init__(self, line):
        self.name, self.L, self.R = re.findall('[A-Z0-9]{3}', line)

    def __repr__(self):
        return f"{self.name} -> ({self.L}, {self.R})"

    def __getitem__(self, d):
        return self.L if d == 'L' else self.R

nodes_list = [Node(line) for line in nodes_raw]
nodes = {n.name: n for n in nodes_list}

curr = nodes['AAA']
for count, direction in enumerate(steps):
    curr = nodes[curr[direction]]
    if curr.name == 'ZZZ':
        break

print(f"A ::: {count + 1}")

start_nodes = [n for n in nodes_list if n.name[-1] == 'A']

def get_first_z(node):
    curr = node
    for count, direction in enumerate(steps):
        curr = nodes[curr[direction]]
        if curr.name[-1] == 'Z':
            return count + 1


init_z = [get_first_z(n) for n in start_nodes]

# Compute LCM of these numbers to find sync index
lcm = 1
for i in init_z:
    lcm *= i // gcd(lcm, i)

print(f"B ::: {lcm}")

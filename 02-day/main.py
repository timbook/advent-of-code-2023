import re

class Game:
    def __init__(self, line):
        self.id = int(re.findall('Game (\\d+)', line)[0])
        self.r_pulls = [int(n) for n in re.findall('(\\d+) red', line)]
        self.g_pulls = [int(n) for n in re.findall('(\\d+) green', line)]
        self.b_pulls = [int(n) for n in re.findall('(\\d+) blue', line)]

    def is_legal(self):
        r_legal = all(r <= 12 for r in self.r_pulls)
        g_legal = all(g <= 13 for g in self.g_pulls)
        b_legal = all(b <= 14 for b in self.b_pulls)
        return r_legal and g_legal and b_legal

    def power(self):
        r_power = max(self.r_pulls)
        g_power = max(self.g_pulls)
        b_power = max(self.b_pulls)
        return r_power*g_power*b_power

lines = open('data/input.txt').readlines()

games = [Game(l) for l in lines]
legal_games = [g.id for g in games if g.is_legal()]
print(f"A ::: {sum(legal_games)}")

powers = [g.power() for g in games]
print(f"B ::: {sum(powers)}")

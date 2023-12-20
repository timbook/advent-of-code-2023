lines_raw = open('data/input.txt').readlines()

class Beam:
    def __init__(self, dir_in, loc):
        self.dir_in = dir_in
        self.loc = loc
        self.beam_id = f"{dir_in}:{loc[0]}:{loc[1]}"
        BEAM_HIST.add(self.beam_id)
        VISITED.add(self.loc)

    def __repr__(self):
        return f"Beam({self.dir_in}, {self.loc})"

    def make_new_beams(self, sym):
        r, c = self.loc

        if sym == '^':
            new_loc = (r - 1, c)
        elif sym == 'v':
            new_loc = (r + 1, c)
        elif sym == '>':
            new_loc = (r, c + 1)
        elif sym == '<':
            new_loc = (r, c - 1)

        new_r, new_c = new_loc
        valid_loc = (new_r >= len(GRID)) or (new_c >= len(GRID[0])) or (new_r < 0) or (new_c < 0)
        new_id = f"{sym}:{new_r}:{new_c}"

        if valid_loc or new_id in BEAM_HIST:
            return
        else:
            new_beam = Beam(sym, new_loc)
            BEAMS.append(new_beam)

    def reflect(self):
        r, c = self.loc
        sym = GRID[r][c]

        if self.dir_in == '>':
            if sym in '.-':
                self.make_new_beams('>')
            elif sym == '/':
                self.make_new_beams('^')
            elif sym == '\\':
                self.make_new_beams('v')
            elif sym == '|':
                self.make_new_beams('v')
                self.make_new_beams('^')

        elif self.dir_in == '<':
            if sym in '.-':
                self.make_new_beams('<')
            elif sym == '/':
                self.make_new_beams('v')
            elif sym == '\\':
                self.make_new_beams('^')
            elif sym == '|':
                self.make_new_beams('v')
                self.make_new_beams('^')

        elif self.dir_in == '^':
            if sym in '.|':
                self.make_new_beams('^')
            elif sym == '/':
                self.make_new_beams('>')
            elif sym == '\\':
                self.make_new_beams('<')
            elif sym == '-':
                self.make_new_beams('<')
                self.make_new_beams('>')

        elif self.dir_in == 'v':
            if sym in '.|':
                self.make_new_beams('v')
            elif sym == '/':
                self.make_new_beams('<')
            elif sym == '\\':
                self.make_new_beams('>')
            elif sym == '-':
                self.make_new_beams('<')
                self.make_new_beams('>')

GRID = [list(row.strip()) for row in lines_raw]
VISITED = set()
BEAM_HIST = set()
BEAMS = [Beam('>', (0, 0))]

while BEAMS:
    beam = BEAMS.pop()
    beam.reflect()

sol = len(VISITED)
print(f"A ::: {sol}")

R = len(GRID)
C = len(GRID[0])

possible_inputs = \
    [('v', (0, c)) for c in range(C)] + \
    [('^', (R - 1, c)) for c in range(C)] + \
    [('>', (r, 0)) for r in range(R)] + \
    [('<', (r, C - 1)) for r in range(R)]

n_energized = []

for input_ in possible_inputs:
    VISITED = set()
    BEAM_HIST = set()
    BEAMS = [Beam(*input_)]

    while BEAMS:
        beam = BEAMS.pop()
        beam.reflect()

    energized = len(VISITED)
    n_energized.append(energized)

sol = max(n_energized)
print(f"B ::: {sol}")

import re

#  raw = open('data/sample.txt').read()
raw = open('data/input.txt').read()

workflows_raw, parts_raw = raw.split('\n\n')
workflows_list = workflows_raw.strip().split('\n')
parts_list = parts_raw.strip().split('\n')

class Part:
    def __init__(self, part_str):
        x, m, a, s = re.findall('x=(\d+),m=(\d+),a=(\d+),s=(\d+)', part_str)[0]
        self.x = int(x)
        self.m = int(m)
        self.a = int(a)
        self.s = int(s)
        self.d = {'x': self.x, 'm': self.m, 'a': self.a, 's': self.s}

    def __repr__(self):
        return f"Part(x={self.x}, m={self.m}, a={self.a}, s={self.s})"

    def __getitem__(self, ix):
        return self.d.get(ix)

    def rating(self):
        return sum(v for k, v in self.d.items())

class Rule:
    def __init__(self, rule_str):
        self.output = re.findall('(\w+)$', rule_str)[0]
        if ':' in rule_str:
            var, sym, num = re.findall('([xmas])([<>])(\d+):', rule_str)[0]
            self.var = var
            self.sym = sym
            self.num = int(num)
            self.has_cond = True
        else:
            self.var = ''
            self.sym = ''
            self.num = ''
            self.has_cond = False

    def test(self, part):
        if not self.has_cond:
            return True

        if self.sym == '>':
            op = lambda a, b: a > b
        elif self.sym == '<':
            op = lambda a, b: a < b

        return op(part[self.var], self.num)

    def __repr__(self):
        return f"Rule({self.var} {self.sym} {self.num} => {self.output})"

class Workflow:
    def __init__(self, workflow_str):
        name, contents = re.findall('(\w+)\{(.*)\}', workflow_str)[0]
        self.name = name
        self.rules = [Rule(s) for s in contents.strip().split(',')]

    def pass_through(self, part):
        for rule in self.rules:
            if rule.test(part):
                return rule.output


parts = [Part(p) for p in parts_list]
wfs = [Workflow(w) for w in workflows_list]
wfs = {w.name: w for w in wfs}

    
def pass_through_wf(part):
    current_wf = wfs['in']
    while True:
        next_wf_str = current_wf.pass_through(part)
        if next_wf_str in 'AR':
            break
        else:
            current_wf = wfs[next_wf_str]
    return next_wf_str

part_ratings = [pass_through_wf(p) for p in parts]
sol = sum([p.rating() for r, p in zip(part_ratings, parts) if r == 'A'])
print(f"A ::: {sol}")

raw = open('data/input.txt').read().strip()

steps = raw.split(",")

def hash(text):
    val = 0
    for char in text:
        val += ord(char)
        val *= 17
        val %= 256
    return val

hashes = [hash(step) for step in steps]
sol = sum(hashes)

print(f"A ::: {sol}")

boxes = {i:[] for i in range(256)}
values = {}

for step in steps:
    if '=' in step:
        lbl, val = step.split('=')
        box = hash(lbl)
        if lbl not in boxes[box]:
            boxes[box].append(lbl)
        values[lbl] = int(val)
    elif '-' in step:
        lbl = step.replace('-', '')
        box = hash(lbl)
        if lbl in boxes[box]:
            boxes[box].remove(lbl)
        if lbl in values:
            del values[lbl]

def calc_power(n, box):
    tot = 0
    for lbl in box:
        tot += (n + 1) * (box.index(lbl) + 1) * values[lbl]

    return tot

powers = [calc_power(n, box) for n, box in boxes.items()]
sol = sum(powers)

print(f"B ::: {sol}")

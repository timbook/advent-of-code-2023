lines_raw = [l.strip() for l in open('input.txt', 'r').readlines()]
lines = [''.join([char for char in line if char.isdigit()]) for line in lines_raw]
nums = [int(line[0] + line[-1]) for line in lines]
print(f"A ::: {sum(nums)}")

num_str = [
    'zero', 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine'
]

num_keys = num_str + [str(n) for n in range(10)]
num_dict = {s: str(i) for i, s in enumerate(num_str)}

def key_to_int(k):
    return num_dict.get(k, k)

def process_line(line):
    lhs = min([(n, line.find(n)) for n in num_keys if n in line], key=lambda t: t[1])[0]
    rhs = max([(n, line.rfind(n)) for n in num_keys if n in line], key=lambda t: t[1])[0]
    return int(key_to_int(lhs) + key_to_int(rhs))

nums = [process_line(line) for line in lines_raw]
print(f"B ::: {sum(nums)}")

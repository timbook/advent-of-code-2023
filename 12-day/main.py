import re
from itertools import product

#  lines = open('data/sample.txt').readlines()
lines = open('data/input.txt').readlines()


def proc_row(line):
    row, seq = line.split()
    n_questions = row.count('?')
    count = 0
    prods = list(set(product('.#', repeat=n_questions)))
    for prod in prods:
        prod = list(prod)
        row_list = list(row)

        for i, char in enumerate(row):
            if char == '?':
                row_list[i] = prod.pop()
        seqs = re.findall('#+', ''.join(row_list))
        seq_lens = [str(len(s)) for s in seqs]
        seq_match = ','.join(seq_lens)
        if seq == seq_match:
            #  print(''.join(row_list))
            count += 1

    return count


#  prod = list(set(product(row, repeat=len(row))))

#  counts = [2**(line.count('?')*5) for line in lines]
#  print(counts)

counts = [proc_row(line) for line in lines]
sol = sum(counts)
print(f"A ::: {sol}")

import re

lines = open('data/input.txt', 'r').readlines()

class Card:
    def __init__(self, line):
        card_str, nums = line.split(':')
        try:
            self.id = int(re.findall('Card\\s+(\\d+)', card_str)[0])
        except:
            print(line)
            raise
        lhs, rhs = nums.split('|')
        self.winning_nums = [int(n) for n in lhs.split()]
        self.my_nums = [int(n) for n in rhs.split()]

        self.assign_score_a()
        self.assign_score_b()

    def assign_score_a(self):
        count = sum([1 for n in self.my_nums if n in self.winning_nums])
        score = 0 if count == 0 else 2**(count - 1)
        self.score_a = score

    def assign_score_b(self):
        count = sum([1 for n in self.my_nums if n in self.winning_nums])
        self.score_b = count

cards = [Card(line) for line in lines]
sol = sum(c.score_a for c in cards)
print(f"A ::: {sol}")

card_counts = {c.id : 1 for c in cards}

for card in cards:
    new_ids = [i for i in range(card.id + 1, card.id + card.score_b + 1)]
    n_cards = card_counts[card.id]
    for i in new_ids:
        card_counts[i] += n_cards

sol = sum(card_counts.values())
print(f"B ::: {sol}")

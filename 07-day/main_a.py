#  lines = open('data/sample.txt').readlines()
lines = open('data/input.txt').readlines()

card_map = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

class Hand:
    def __init__(self, line):
        cards_raw, bid = line.strip().split()
        self.cards_raw = cards_raw
        cards = list(cards_raw)

        self.bid = int(bid)
        self.cards = [int(card_map.get(c, c)) for c in cards]
        self.classify()
        self.make_order()

    def __repr__(self):
        return self.cards_raw

    def classify(self):
        card_dict = {}
        for c in self.cards:
            card_dict[c] = card_dict.get(c, 0) + 1

        # 6 - 5OAK
        if all(c == self.cards[0] for c in self.cards):
            self.type = 6

        # 5 - 4OAK
        elif set(card_dict.values()) == {4, 1}:
            self.type = 5

        # 4 - Full House
        elif set(card_dict.values()) == {2, 3}:
            self.type = 4

        # 3 - 3OAK
        elif any(v == 3 for v in card_dict.values()):
            self.type = 3

        # 2 - Two Pair
        elif len(card_dict) == 3 and set(card_dict.values()) == {1, 2}:
            self.type = 2        

        # 1 - One Pair
        elif len(card_dict) == 4 and set(card_dict.values()) == {1, 2}:
            self.type = 1

        # 0 - High Card
        else:
            self.type = 0

    def make_order(self): 
        self.order = (self.type, *self.cards)

hands = [Hand(line) for line in lines]
hands_sorted = sorted(hands, key=lambda h: h.order)
hands_ranked = [(h, i + 1) for i, h in enumerate(hands_sorted)]
sol = sum(h.bid*i for h, i in hands_ranked)
print(f"A ::: {sol}")








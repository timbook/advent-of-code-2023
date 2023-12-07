lines = open('data/input.txt').readlines()

card_map = {'T': 10, 'J': 0, 'Q': 12, 'K': 13, 'A': 14}

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
        cards_wo_j = [c for c in self.cards if c != 0]
        num_j = self.cards.count(0)

        # Edge case, all J:
        if num_j == 5:
            self.type = 6
            return

        card_dict = {}
        for c in cards_wo_j:
            card_dict[c] = card_dict.get(c, 0) + 1

        card_list = [(k, v) for k, v in card_dict.items()]
        card_list = sorted(card_list, key=lambda d: d[1], reverse=True)

        best_card = card_list[0]
        card_list[0] = (best_card[0], best_card[1] + num_j)

        print(f"{self.cards_raw} now looks like this: {card_list}")

        # 6 - 5OAK
        if card_list[0][1] == 5:
            self.type = 6

        # 5 - 4OAK
        elif card_list[0][1] == 4:
            self.type = 5

        # 4 - Full House
        elif card_list[0][1] == 3 and card_list[1][1] == 2:
            self.type = 4

        # 3 - 3OAK
        elif card_list[0][1] == 3:
            self.type = 3

        # 2 - Two Pair
        elif card_list[0][1] == 2 and card_list[1][1] == 2:
            self.type = 2        

        # 1 - One Pair
        elif card_list[0][1] == 2:
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

print(f"B ::: {sol}")

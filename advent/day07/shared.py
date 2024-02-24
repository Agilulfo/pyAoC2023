from advent import utils


def calculate_total_winning(scoring):
    with open(utils.input_path(__file__)) as input:
        hands = []
        for line in input:
            parts = line.split(" ")
            hands.append(Hand(parts[0], int(parts[-1]), scoring))

        hands = sorted(
            hands,
        )
        total_winning = 0
        for rank, hand in enumerate(hands):
            total_winning += hand.calculate_value(rank + 1)

        return total_winning


class Hand:
    def __init__(self, hand, bid, scoring):
        self.hand = hand
        self.bid = bid
        self.value = scoring.value(hand)
        self.type = scoring.type(hand)

    def calculate_value(self, rank):
        return rank * self.bid

    def __lt__(self, other):
        if self.type < other.type:
            return True
        elif self.type == other.type:
            return self.value < other.value
        else:
            return False

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value

    def __repr__(self):
        return f"Hand: {self.hand} - {self.type} - {self.value}"

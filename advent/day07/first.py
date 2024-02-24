from advent import utils


def main():
    with open(utils.input_path(__file__)) as input:
        hands = []
        for line in input:
            parts = line.split(" ")
            hands.append(Hand(parts[0], int(parts[-1])))

        hands = sorted(
            hands,
        )
        total_winning = 0
        for rank, hand in enumerate(hands):
            total_winning += hand.calculate_value(rank + 1)

        print(f"total_winning is: {total_winning}")


class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.value = Scoring.value(hand)
        self.type = Scoring.type(hand)

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


class Scoring:
    def value(hand):
        value = ""
        for card in hand:
            base_14 = ""
            match card:
                case "2":
                    base_14 = "1"
                case "3":
                    base_14 = "2"
                case "4":
                    base_14 = "3"
                case "5":
                    base_14 = "4"
                case "6":
                    base_14 = "5"
                case "7":
                    base_14 = "6"
                case "8":
                    base_14 = "7"
                case "9":
                    base_14 = "8"
                case "T":
                    base_14 = "9"
                case "J":
                    base_14 = "A"
                case "Q":
                    base_14 = "B"
                case "K":
                    base_14 = "C"
                case "A":
                    base_14 = "D"
            value += base_14
        return int(value, base=14)

    def type(hand):
        counter = {}
        for card in hand:
            if card in counter:
                counter[card] += 1
            else:
                counter[card] = 1

        occurrences = sorted([v for v in counter.values()], reverse=True)

        match occurrences:
            case [5]:
                return 7
            case [4, 1]:
                return 6
            case [3, 2]:
                return 5
            case [3, 1, 1]:
                return 4
            case [2, 2, 1]:
                return 3
            case [2, 1, 1, 1]:
                return 2
            case _:
                return 1

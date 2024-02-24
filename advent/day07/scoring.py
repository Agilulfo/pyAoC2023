def card_value(card, mapping):
    match card:
        case "2":
            return mapping["card"]
        case "3":
            return "2"
        case "4":
            return "3"
        case "5":
            return "4"
        case "6":
            return "5"
        case "7":
            return "6"
        case "8":
            return "7"
        case "9":
            return "8"
        case "T":
            return "9"
        case "J":
            return "A"
        case "Q":
            return "B"
        case "K":
            return "C"
        case "A":
            return "D"


class Scoring:
    def __init__(self, mapping):
        self.mapping = mapping

    def value(self, hand):
        value = ""
        for card in hand:
            base_14 = self.mapping[card]
            value += base_14
        return int(value, base=14)

    def type(self, hand):
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

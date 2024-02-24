from advent.day07.shared import calculate_total_winning
from advent.day07.scoring import Scoring


def main():
    print(
        f"total_winning is: {calculate_total_winning(Scoring(card_value_mapping, preprocessing=replace_joker))}"
    )


card_value_mapping = {
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "T": "A",
    "J": "1",
    "Q": "B",
    "K": "C",
    "A": "D",
}


def replace_joker(hand):
    cards_occurrences = Scoring.count_occurrences(hand)
    joker_count = cards_occurrences.pop("J", 0)

    other_occurrences = sorted(
        list(cards_occurrences.items()), key=lambda pair: pair[1], reverse=True
    )

    match joker_count:
        case 0:
            return hand
        case 5:
            return "AAAAA"
        case _:
            return hand.replace("J", other_occurrences[0][0])

from advent.day07.shared import calculate_total_winning
from advent.day07.scoring import Scoring


def main():
    print(f"total_winning is: {calculate_total_winning(Scoring(card_value_mapping))}")


card_value_mapping = {
    "2": "1",
    "3": "2",
    "4": "3",
    "5": "4",
    "6": "5",
    "7": "6",
    "8": "7",
    "9": "8",
    "T": "9",
    "J": "A",
    "Q": "B",
    "K": "C",
    "A": "D",
}

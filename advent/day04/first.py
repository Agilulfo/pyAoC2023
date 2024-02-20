from advent.day04 import shared


def main():
    cards = shared.parse_input()

    total_score = 0
    for card in cards:
        card_score = count_matches(card)
        total_score += 0 if card_score == 0 else pow(2, card_score - 1)

    print("total_score is: ", total_score)


def count_matches(card):
    _, winning, guessed = card
    guessed = set(guessed)
    counter = 0
    for number in winning:
        if number in guessed:
            counter += 1
    return counter

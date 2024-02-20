from advent.day04 import shared


def main():
    games = shared.parse_input()

    total_score = 0
    for game in games:
        game_score = count_matches(game)
        total_score += 0 if game_score == 0 else pow(2, game_score - 1)

    print("total_score is: ", total_score)


def count_matches(game):
    _, winning, guessed = game
    guessed = set(guessed)
    counter = 0
    for number in winning:
        if number in guessed:
            counter += 1
    return counter

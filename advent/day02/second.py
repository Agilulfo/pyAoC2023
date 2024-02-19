from advent import utils
from advent.day02 import shared


def main():
    with open(utils.input_path(__file__)) as input:
        score = 0
        for line in input:
            game = shared.decode(line)
            (_game_number, rounds) = game
            score += power(rounds)
        print("the answer is: ", score)


def power(rounds):
    red = 0
    green = 0
    blue = 0

    for r, g, b in rounds:
        red = max(r, red)
        green = max(g, green)
        blue = max(b, blue)

    return red * green * blue

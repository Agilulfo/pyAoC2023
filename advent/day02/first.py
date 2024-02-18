from advent import utils
from advent.day02 import shared


def main():
    with open(utils.input_path(__file__)) as input:
        score = 0
        for line in input:
            (game_number, rounds) = shared.decode(line)
            if validate(rounds):
                score += game_number
        print("the answer is: ", score)


def validate(rounds):
    valid = True
    for round in rounds:
        (red, green, blue) = round
        if red > 12:
            valid = False
            break
        if green > 13:
            valid = False
            break
        if blue > 14:
            valid = False
            break
    return valid

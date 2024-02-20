from advent import utils


def parse_input():
    path = utils.input_path(__file__)
    cards = []
    with open(path) as input:
        for line in input:
            index, data = line[:-1].split(":")
            card_index = extract_card_index(index)
            winning_numbers, guessed_numbers = data.split("|")
            winning_numbers = sequence_to_list(winning_numbers)
            guessed_numbers = sequence_to_list(guessed_numbers)
            cards.append((card_index, winning_numbers, guessed_numbers))
    return cards


def sequence_to_list(sequence):
    numbers = []

    for item in sequence.split(" "):
        try:
            numbers.append(int(item))
        except ValueError:
            pass

    return numbers


def extract_card_index(index):
    return int(index[4:])

def count_matches(card):
    _, winning, guessed = card
    guessed = set(guessed)
    counter = 0
    for number in winning:
        if number in guessed:
            counter += 1
    return counter

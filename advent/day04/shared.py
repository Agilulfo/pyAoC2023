from advent import utils


def parse_input():
    path = utils.input_path(__file__)
    games = []
    with open(path) as input:
        for line in input:
            index, data = line[:-1].split(":")
            game_index = extract_game_index(index)
            winning_numbers, guessed_numbers = data.split("|")
            winning_numbers = sequence_to_list(winning_numbers)
            guessed_numbers = sequence_to_list(guessed_numbers)
            games.append((game_index, winning_numbers, guessed_numbers))
    return games


def sequence_to_list(sequence):
    numbers = []

    for item in sequence.split(" "):
        try:
            numbers.append(int(item))
        except:
            pass

    return numbers


def extract_game_index(index):
    return int(index[4:])

from advent import utils


def load_map():
    with open(utils.input_path(__file__)) as input:
        return input.read().splitlines()

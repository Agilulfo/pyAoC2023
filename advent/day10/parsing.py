from advent import utils


def load_map(file_path=__file__):
    with open(utils.input_path(file_path)) as input:
        return [list(line) for line in input.read().splitlines()]

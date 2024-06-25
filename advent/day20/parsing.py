from advent import utils

def parse_input():

    setup = []
    with open(utils.input_path(__file__)) as input:
        for line in input:
            line = line.strip()
            module, outputs = line.split(" -> ")
            outputs = outputs.split(", ")
            setup.append((module, outputs))

    return setup

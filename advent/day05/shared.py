from advent import utils


def parse_input():
    input = {}
    with open(utils.input_path(__file__)) as input_file:
        input["seeds"] = [
            int(value) for value in input_file.readline()[7:-1].split(" ")
        ]
        input_file.readline()
        while True:
            result = extract_map(input_file)
            if result:
                map_name, rules = result
                input[map_name] = rules
            else:
                break
    return input


def extract_map(input_file):
    map_info = input_file.readline()
    if not map_info:
        return None
    map_name = map_info[:-6]
    rules = []

    for line in input_file:
        if len(line) > 1:
            rules.append([int(value) for value in line[:-1].split(" ")])
        else:
            break

    return (map_name, rules)

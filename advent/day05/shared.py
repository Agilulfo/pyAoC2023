import bisect
from advent import utils

MAP_SEQUENCE = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def find_lowest_location(seeds, maps):
    min_location = None
    for seed in seeds:
        location = apply_all_maps(seed, maps)
        if min_location is None or location < min_location:
            min_location = location
    return min_location


def init_maps(input):
    return [BotanicMap(map_type, input[map_type]) for map_type in MAP_SEQUENCE]


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


def apply_all_maps(value, map_list, index=0):
    if index == len(map_list):
        return value
    return apply_all_maps(map_list[index].convert(value), map_list, index=index + 1)


class Rule:
    def __init__(self, params):
        self.destination, self.source, self.size = params

    def __lt__(self, other):
        if isinstance(other, int):
            return self.source < other
        elif isinstance(other, Rule):
            return self.source < other.source
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, int):
            return self.source > other
        elif isinstance(other, Rule):
            return self.source > other.source
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, int):
            return self.does_apply_for(other)
        elif isinstance(other, Rule):
            return self.source == other.source and self.size == other.size
        else:
            return NotImplemented

    def does_apply_for(self, value):
        return self.source <= value < self.source + self.size

    def apply(self, value):
        if not self.does_apply_for(value):
            raise RuleNotApplicable()
        delta = self.destination - self.source
        return value + delta


class RuleNotApplicable(Exception):
    pass


class BotanicMap:
    def id(self):
        return self.id

    def __init__(self, name, rules):
        self.id = name
        self.rules = sorted([Rule(rule) for rule in rules])

    def convert(self, id):
        rule = self.pick_rule(id)
        if rule:
            return rule.apply(id)
        else:
            return id

    def pick_rule(self, id):
        index = bisect.bisect(self.rules, id)
        if index == 0:
            return None
        candidate = self.rules[index - 1]
        if candidate.does_apply_for(id):
            return candidate

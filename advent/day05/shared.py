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
    return [Map(map_type, input[map_type]) for map_type in MAP_SEQUENCE]


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
        destination, source, size = params
        self.delta = destination - source
        self.range = Range(source, size)
        self.range.item = self

    def apply(self, value):
        if not self.range.includes(value):
            raise RuleNotApplicable()
        return value + self.delta


class RuleNotApplicable(Exception):
    pass


class Map:
    def id(self):
        return self.id

    def __init__(self, name, rules):
        self.id = name
        self.ranges = sorted([Rule(rule).range for rule in rules])

    def convert(self, id):
        rule = self.pick_rule(id)
        if rule:
            return rule.apply(id)
        else:
            return id

    def pick_rule(self, id):
        index = bisect.bisect(self.ranges, id)
        if index == 0:
            return None
        candidate = self.ranges[index - 1].item
        if candidate.range.includes(id):
            return candidate
        else :
            return None


class Range:
    def __init__(self, start, size):
        self.start = start
        self.size = size

    def end(self):
        return self.start + self.size - 1

    def includes(self, other):
        if isinstance(other, int):
            return self.start <= other <= self.end()
        elif isinstance(other, self.__class__):
            return self.start <= other.start and self.end() >= other.end()
        else:
            NotImplemented

    def shift(self, delta):
        self.start += delta

    def __lt__(self, other):
        if isinstance(other, int):
            return self.start < other
        elif isinstance(other, self.__class__):
            return self.end() < other.start
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, int):
            return self.start > other
        elif isinstance(other, self.__class__):
            return self.start > other.end()
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, int):
            return self.includes(other)
        elif isinstance(other, self.__class__):
            return self.start == other.start and self.end() == other.end()
        else:
            return NotImplemented

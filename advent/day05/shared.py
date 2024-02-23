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
    return apply_all_maps(map_list[index].convert_id(value), map_list, index=index + 1)


class Rule:
    def __init__(self, params):
        destination, source, size = params
        self.delta = destination - source
        self.range = Range(source, size)
        self.range.item = self

    def apply(self, value):
        if isinstance(value, int):
            return self.__apply_id(value)
        else:
            return self.__apply_range(value)

    def __apply_id(self, id):
        if not self.range.includes(id):
            raise RuleNotApplicable()
        return id + self.delta

    def __apply_range(self, range):
        return range.shift(self.delta)


class RuleNotApplicable(Exception):
    pass


class Map:
    def id(self):
        return self.id

    def __init__(self, name, rules):
        self.id = name
        self.ranges = sorted([Rule(rule).range for rule in rules])

    def convert_id(self, id):
        rule = self.pick_rule_for_id(id)
        if rule:
            return rule.apply(id)
        else:
            return id

    # def convert_range(self, range):
    #     rules = pick_rules_for_range(self, range)
    #     ranges = [rule.range for rule in rules]
    #     new_ranges = [range.split_with_ranges(ranges)]
    #     converted_ranges = []
    #     for range, rule in new_ranges:
    #         if rule:
    #             rule.apply(range)
    #         converted_ranges.append(range)

    def pick_rule_for_id(self, id):
        index = bisect.bisect(self.ranges, id)
        if index == 0:
            return None
        candidate = self.ranges[index - 1].item
        if candidate.range.includes(id):
            return candidate
        else:
            return None

    def pick_rules_for_range(self, range):
        raise NotImplementedError


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

    def in_between(range_a, range_b):
        if range_b.start - range_a.end() <= 1:
            return None
        start = range_a.end() + 1
        end = range_b.start - 1
        size = Range.size_from_ends(start, end)
        return Range(start, size)

    def size_from_ends(start, end):
        return end - start + 1

    def split_with_ranges(self, ranges):
        ranges = sorted([range for range in ranges if self.collides(range)])

        if not ranges:
            return [(Range(self.start, self.size), None)]

        new_ranges = []

        previous_range = Range(self.start - 1, 1)

        for range in ranges:
            new_range = self.intersection(range)
            gap_range = Range.in_between(previous_range, new_range)
            if gap_range:
                new_ranges.append((gap_range, None))
            new_ranges.append((new_range, range))
            previous_range = new_range

        last_gap = Range.in_between(previous_range, Range(self.end() + 1, 1))
        if last_gap:
            new_ranges.append((last_gap, None))

        return new_ranges

    def collides(self, range):
        return self.includes(range.start) or self.includes(range.end())

    def intersection(self, other):
        start = max(self.start, other.start)
        end = min(self.end(), other.end())
        size = Range.size_from_ends(start, end)
        return Range(start, size)

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

    def __repr__(self):
        return "range " + str(self.start) + " " + str(self.end()) + " " + str(self.size)

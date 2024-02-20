import bisect
from advent.day05 import shared

MAP_SEQUENCE = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def main():
    input = shared.parse_input()
    min_location = None
    maps = [BotanicMap(map_type, input[map_type]) for map_type in MAP_SEQUENCE]

    for seed in input["seeds"]:
        location = apply_all_maps(seed, maps)
        if min_location is None or location < min_location:
            min_location = location

    print("the lowest location is: ", min_location)


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

from advent.day19.parsing import parse_input
from collections import deque


def main():
    workflows, _ = parse_input()

    workflows_map = {}
    for workflow in workflows:
        name, rules, default = workflow
        rules = [
            Rule(category, comparator, value, destination)
            for category, comparator, value, destination in rules
        ]
        workflows_map[name] = Workflow(name, rules, default)

    initial_part_combination = PartCombination(
        Interval(1, 4000),
        Interval(1, 4000),
        Interval(1, 4000),
        Interval(1, 4000),
        destination="in",
    )

    queue = deque()
    queue.append(initial_part_combination)

    total_combinations = 0

    while len(queue) > 0:
        part_combination = queue.pop()
        match part_combination.destination:
            case "A":
                total_combinations += part_combination.combinations()
            case "R":
                continue
            case destination:
                workflow = workflows_map[destination]
                queue.extend(workflow.apply(part_combination))

    print(f"The total amount of accepted combination is: {total_combinations}")


class Rule:
    def __init__(self, category, comparator, value, destination):
        self.category = category
        self.comparator = comparator
        self.value = int(value)
        self.destination = destination

    def apply(self, part_combination):
        pc_a = part_combination
        pc_b = part_combination.clone()

        match self.comparator:
            case ">":
                pc_a.__getattribute__(f"range_{self.category}").keep_gt(self.value)
                pc_a.destination = self.destination
                pc_b.__getattribute__(f"range_{self.category}").keep_lte(self.value)
                pc_b.destination = None
            case "<":
                pc_a.__getattribute__(f"range_{self.category}").keep_lt(self.value)
                pc_a.destination = self.destination
                pc_b.__getattribute__(f"range_{self.category}").keep_gte(self.value)
                pc_b.destination = None
        return [pc for pc in [pc_a, pc_b] if pc.is_valid()]

class Workflow:
    def __init__(self, name, rules, default):
        self.name = name
        self.rules = rules
        self.default = default

    def apply(self, part_combination):
        part_combinations = []
        for rule in self.rules:
            part_groups = rule.apply(part_combination)
            for pg in part_groups:
                if pg.destination is None:
                    part_combination = pg
                else:
                    part_combinations.append(pg)
        part_combination.destination = self.default
        part_combinations.append(part_combination)

        return part_combinations


class PartCombination:
    def __init__(self, range_x, range_m, range_a, range_s, destination="in"):
        self.range_x = range_x
        self.range_m = range_m
        self.range_a = range_a
        self.range_s = range_s
        self.destination = destination

    def combinations(self):
        return (
            self.range_x.element_count()
            * self.range_m.element_count()
            * self.range_a.element_count()
            * self.range_s.element_count()
        )

    def clone(self):
        return PartCombination(
            self.range_x.clone(),
            self.range_m.clone(),
            self.range_a.clone(),
            self.range_s.clone(),
            self.destination,
        )

    def is_valid(self):
        return (
            self.range_x.is_valid()
            and self.range_m.is_valid()
            and self.range_a.is_valid()
            and self.range_s.is_valid()
        )

    def __repr__(self):
        return f"x: {self.range_x}, m: {self.range_m}, a: {self.range_a}, s: {self.range_s} -> {self.destination}"


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def keep_gt(self, treshold):
        self.start = treshold + 1

    def keep_lt(self, treshold):
        self.end = treshold - 1

    def keep_gte(self, treshold):
        self.start = treshold

    def keep_lte(self, treshold):
        self.end = treshold

    def is_valid(self):
        return self.end >= self.start

    def element_count(self):
        return self.end - self.start + 1

    def clone(self):
        return Interval(self.start, self.end)

    def __repr__(self):
        return f"[{self.start} - {self.end}]"

from advent.day13.parsing import parse_input
from collections import defaultdict, Counter


def main():
    patterns = parse_input()
    result = [Pattern(pattern) for pattern in patterns]
    result[1].find_simmetry()


class Trine(Exception):
    pass


class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern

    def find_simmetry(self):
        d = defaultdict(list)
        for index, line in enumerate(self.pattern):
            line = Line(index, line)
            d[line].append(line)
        dups = [dups for dups in d.values() if len(dups) > 1]

        simmetry_candidates = []
        for pair in dups:
            if len(pair) != 2:
                raise Trine
            a, b = pair
            minimum, maximum = min(a.index, b.index), max(a.index, b.index)
            simmetry_candidates.append(minimum + (maximum - minimum) // 2)
        counter = Counter(simmetry_candidates)

        for index, matches in counter.most_common():
            if Pattern.expected_line_matches(self.pattern, index) == matches:
                return index + 1
        return None

    def expected_line_matches(pattern, simmetry_index):
        return min(simmetry_index + 1, len(pattern) - simmetry_index + 1)


class Line:
    def __init__(self, index, line):
        self.index = index
        self.line = line

    def __repr__(self):
        return f"{self.index} - {self.line}"

    def __hash__(self):
        return hash(self.line)

    def __eq__(self, other):
        return self.line == other.line

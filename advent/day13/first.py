from advent.day13.parsing import parse_input
from collections import defaultdict, Counter


def main():
    patterns = parse_input()
    patterns = [Pattern(pattern) for pattern in patterns]
    counter = 0
    for pattern in patterns:
        row_simmetry, index = pattern.find_simmetry()
        if row_simmetry:
            counter += 100 * index
        else:
            counter += index

    print(f"the sum is: {counter}")


class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern

    def find_simmetry(self):
        simmetry_index = Pattern.row_simmetry(self.pattern)
        if simmetry_index is not None:
            return True, simmetry_index
        else:
            return False, Pattern.row_simmetry(Pattern.transpose(self.pattern))

    def row_simmetry(pattern):
        d = defaultdict(list)
        for index, line in enumerate(pattern):
            line = Line(index, line)
            d[line].append(line)
        dups = [dups for dups in d.values() if len(dups) > 1]

        simmetry_candidates = []
        for matches in dups:
            if len(matches) != 2:
                for first in range(len(matches)):
                    for second in range(first + 1, len(matches)):
                        if not (first % 2 == 0 ^ second % 2 == 0):
                            dups.append([matches[first], matches[second]])
            else:
                a, b = matches
                minimum, maximum = min(a.index, b.index), max(a.index, b.index)
                simmetry_candidates.append(minimum + (maximum - minimum) // 2)

        counter = Counter(simmetry_candidates)

        for index, matches in counter.most_common():
            if Pattern.expected_line_matches(pattern, index) == matches:
                return index + 1
        return None

    def transpose(pattern):
        transposed = []
        for column in range(len(pattern[0])):
            line = []
            for row in range(len(pattern)):
                line.append(pattern[row][column])
            transposed.append("".join(line))
        return transposed

    def expected_line_matches(pattern, simmetry_index):
        return min(simmetry_index + 1, len(pattern) - simmetry_index - 1)


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

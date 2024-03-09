from advent.day13.parsing import parse_input
from collections import defaultdict, Counter


def main():
    patterns = parse_input()
    patterns = [Pattern(pattern) for pattern in patterns]
    counter = 0
    for pattern in patterns:
        row_simmetry, index = pattern.find_simmetry()
        index += 1
        if row_simmetry:
            counter += 100 * index
        else:
            counter += index
    print(f"the sum is: {counter}")


def word(row_simmetry):
    if row_simmetry:
        return "row"
    return "column"


class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern

    def __repr__(self):
        return "\n".join(self.pattern)

    def find_simmetry(self):
        simmetry_index = Pattern.row_simmetry(self.pattern)
        if simmetry_index is not None:
            return True, simmetry_index
        else:
            return False, Pattern.row_simmetry(Pattern.transpose(self.pattern))

    def row_simmetry(pattern):
        # group lines by hash (equals)
        d = defaultdict(list)
        for index, line in enumerate(pattern):
            line = Line(index, line)
            d[line].append(line)
        dups = [dups for dups in d.values() if len(dups) > 1]

        # groups matching lines by simmetry line
        # collect in simmetry_candidates the simmetry index for each couple
        simmetry_candidates = []
        for matches in dups:
            # handle case where more than one line are identical
            if len(matches) != 2:
                for first in range(len(matches)):
                    for second in range(first + 1, len(matches)):
                        # only handle valid simmetries
                        if Pattern.compatible_mirror_index(first, second):
                            dups.append([matches[first], matches[second]])
            else:
                a, b = matches
                if Pattern.compatible_mirror_index(a.index, b.index):
                    minimum, maximum = min(a.index, b.index), max(a.index, b.index)
                    simmetry_candidates.append(minimum + (maximum - minimum) // 2)

        # count how many lines share the same simmetry line
        counter = Counter(simmetry_candidates)

        # return the first simmetry index that have
        # a valid amount of simmetric lines
        for index, matches in counter.most_common():
            if Pattern.expected_line_matches(pattern, index) == matches:
                return index
        return None

    def compatible_mirror_index(first, second):
        """Check if two index have a valid simmetry line

        e.g. 0 and 2 do not produce a valid simmetry while 1 and 2 do
        """
        return not (first % 2 == 0 ^ second % 2 == 0)

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

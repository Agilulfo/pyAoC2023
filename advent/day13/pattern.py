from collections import defaultdict
from functools import cached_property


class Pattern:
    def __init__(self, pattern, transposed=None):
        self.pattern = pattern
        self.transposed = transposed
        self.is_transposed = self.transposed is not None
        self.partial_simmetries = []
        self.primary_simmetry = None
        self.secondary_simmetry = None
        self.__search_simmetries()

    def get_transposed(self):
        if self.transposed is None:
            self.transposed = Pattern(Pattern.transpose(self.pattern), transposed=self)
        return self.transposed

    def __repr__(self):
        return "\n".join(self.pattern)

    # recursion risk
    def get_primary_simmetry(self):
        if self.primary_simmetry is None:
            return self.get_transposed().get_primary_simmetry()
        else:
            return (not self.is_transposed, self.primary_simmetry.index)

    def get_secondary_simmetry(self):
        if self.secondary_simmetry is None:
            return self.get_transposed().get_secondary_simmetry()
        else:
            return (not self.is_transposed, self.secondary_simmetry.index)

    def __search_simmetries(self):
        # group lines by hash (equals)
        d = defaultdict(list)
        for index, line in enumerate(self.pattern):
            line = Line(index, line)
            d[line].append(line)
        dups = [dups for dups in d.values() if len(dups) > 1]

        unpacked_dups = []

        # unpack multiple equal lines
        for matches in dups:
            # handle case where more than one line are identical
            if len(matches) > 2:
                for first in range(len(matches)):
                    for second in range(first + 1, len(matches)):
                        a = matches[first]
                        b = matches[second]
                        if Pattern.compatible_mirror_index(a.index, b.index):
                            unpacked_dups.append([a, b])
            else:
                a, b = matches
                if Pattern.compatible_mirror_index(a.index, b.index):
                    unpacked_dups.append([a, b])

        simmetries = {}

        for pair in unpacked_dups:
            a, b = pair
            if Pattern.compatible_mirror_index(a.index, b.index):
                minimum, maximum = min(a.index, b.index), max(a.index, b.index)
                simmetry_index = minimum + (maximum - minimum) // 2
                try:
                    simmetry = simmetries[simmetry_index]
                except KeyError:
                    simmetry = Simmetry(simmetry_index, self)
                    simmetries[simmetry_index] = simmetry
                simmetry.add_pair(a, b)

        for simmetry in simmetries.values():
            if simmetry.is_valid():
                self.primary_simmetry = simmetry
            elif simmetry.is_secondary():
                self.secondary_simmetry = simmetry
            else:
                self.partial_simmetries.append(simmetry)

        if self.secondary_simmetry is None:
            candidates = [Simmetry(0, self), Simmetry(len(self.pattern) - 2, self)]
            for candidate in candidates:
                if candidate.is_secondary():
                    self.secondary_simmetry = candidate

    def compatible_mirror_index(first, second):
        """Check if two index have a valid simmetry line

        e.g. 0 and 2 do not produce a valid simmetry while 1 and 2 do
        """
        return not (((first % 2) == 0) == ((second % 2) == 0))

    def transpose(pattern):
        transposed = []
        for column in range(len(pattern[0])):
            line = []
            for row in range(len(pattern)):
                line.append(pattern[row][column])
            transposed.append("".join(line))
        return transposed

    def expected_line_matches(self, simmetry_index):
        return min(simmetry_index + 1, len(self.pattern) - simmetry_index - 1)


class Simmetry:
    def __init__(self, index, pattern):
        self.index = index
        self.pairs = []
        self.pattern = pattern

    def add_pair(self, a, b):
        self.pairs.append((a, b))

    @cached_property
    def missmatch_order(self):
        return self.pattern.expected_line_matches(self.index) - len(self.pairs)

    def is_valid(self):
        return self.missmatch_order == 0

    def is_secondary(self):
        if self.missmatch_order != 1:
            return False
        a, b = self._missing_pair()
        return a.is_close_enough(b)

    def _missing_pair(self):
        indexes = []
        couples_count = self.pattern.expected_line_matches(self.index)
        for delta in range(couples_count):
            indexes.append(self.index - delta)
            indexes.append(self.index + 1 + delta)

        for a, b in self.pairs:
            indexes.remove(a.index)
            indexes.remove(b.index)

        a, b = indexes
        return (Line(a, self.pattern.pattern[a]), Line(b, self.pattern.pattern[b]))


class Line:
    def __init__(self, index, line):
        self.index = index
        self.line = line

    def __repr__(self):
        return f"{self.index} - {self.line}"

    def __hash__(self):
        return hash(self.line)

    def is_close_enough(self, other):
        differences = 0
        for index in range(len(self.line)):
            if self.line[index] != other.line[index]:
                differences += 1
        return differences == 1

    def __eq__(self, other):
        return self.line == other.line

from collections import defaultdict, Counter
from bisect import bisect

PLATFORM_SIZE = 100
NUMBER_OF_CYCLES = 1000000000

class Platform:
    def __init__(self, platform):
        self.rounded_stones = []
        self.cubic_stones = []
        for row_index, row in enumerate(platform):
            for columnd_index, shape in enumerate(row):
                if shape != ".":
                    stone = Stone(
                        shape,
                        PLATFORM_SIZE - row_index,
                        PLATFORM_SIZE - columnd_index,
                        self,
                    )
                    if stone.shape == "#":
                        self.cubic_stones.append(stone)
                    else:
                        self.rounded_stones.append(stone)
        self.columns = self._build_columns()
        self.rows = self._build_rows()

    def tilt(self, direction):
        match direction:
            case "N":
                self.column_mode = True
                groups = defaultdict(list)
                for stone in self.rounded_stones:
                    column = self.columns[stone.column_index - 1]
                    stopper = column[bisect(column, stone)]
                    groups[stopper].append(stone)
                for stopper, stones in groups.items():
                    limit = stopper.row_index
                    for stone in stones:
                        stone.roll("N", limit)
                        limit = stone.row_index
            case "W":
                self.column_mode = False
                groups = defaultdict(list)
                for stone in self.rounded_stones:
                    row = self.rows[stone.row_index - 1]
                    stopper = row[bisect(row, stone)]
                    groups[stopper].append(stone)
                for stopper, stones in groups.items():
                    limit = stopper.column_index
                    for stone in stones:
                        stone.roll("W", limit)
                        limit = stone.column_index
            case "S":
                self.column_mode = True
                groups = defaultdict(list)
                for stone in self.rounded_stones:
                    column = self.columns[stone.column_index - 1]
                    stopper = column[bisect(column, stone) - 1]
                    groups[stopper].append(stone)
                for stopper, stones in groups.items():
                    limit = stopper.row_index
                    for stone in stones:
                        stone.roll("S", limit)
                        limit = stone.row_index
            case "E":
                self.column_mode = False
                groups = defaultdict(list)
                for stone in self.rounded_stones:
                    row = self.rows[stone.row_index - 1]
                    stopper = row[bisect(row, stone) - 1]  # ?
                    groups[stopper].append(stone)
                for stopper, stones in groups.items():
                    limit = stopper.column_index
                    for stone in stones:
                        stone.roll("E", limit)
                        limit = stone.column_index

    def spin_cycle(self):
        for direction in ("N", "W", "S", "E"):
            self.tilt(direction)

    def spin_and_weight(self, n):
        weights = defaultdict(list)
        history = []
        for iteration in range(1000):
            self.spin_cycle()
            current_weight = self.get_weight()
            weights[current_weight].append(iteration + 1)
            history.append(current_weight)

        periods = []
        for occurrences in weights.values():
            if len(occurrences) > 2:
                periods.append(occurrences[-1] - occurrences[-2])

        c = Counter(periods)
        period, _= c.most_common()[0]
        sequence = history[- period:]
        remaining_iterations = n - 1000
        prediction_index = remaining_iterations % period
        return sequence[prediction_index - 1]

    def get_weight(self):
        return sum([stone.get_weight() for stone in self.rounded_stones])

    def _build_columns(self):
        self.column_mode = True
        columns = [[] for _ in range(PLATFORM_SIZE)]
        for stone in self.cubic_stones:
            column = columns[stone.column_index - 1]
            column.insert(bisect(column, stone), stone)
        for index, column in enumerate(columns):
            column.append(Stone("#", PLATFORM_SIZE + 1, index + 1, self))
            column.insert(0, Stone("#", 0, index + 1, self))
        return columns

    def _build_rows(self):
        self.column_mode = False
        rows = [[] for _ in range(PLATFORM_SIZE)]
        for stone in self.cubic_stones:
            row = rows[stone.row_index - 1]
            row.insert(bisect(row, stone), stone)
        for index, row in enumerate(rows):
            row.append(Stone("#", index + 1, PLATFORM_SIZE + 1, self))
            row.insert(0, Stone("#", index + 1, 0, self))
        return rows

    def __repr__(self):
        map = []
        for row in range(PLATFORM_SIZE):
            row = []
            for column in range(PLATFORM_SIZE):
                row.append(".")
            map.append(row)

        for stone in self.rounded_stones:
            map[PLATFORM_SIZE - stone.row_index][
                PLATFORM_SIZE - stone.column_index
            ] = stone.shape
        for stone in self.cubic_stones:
            map[PLATFORM_SIZE - stone.row_index][
                PLATFORM_SIZE - stone.column_index
            ] = stone.shape

        return "\n".join(["".join(row) for row in map])


class Stone:
    def __init__(self, shape, row_index, column_index, platform):
        self.shape = shape
        self.row_index = row_index
        self.column_index = column_index
        self.platform = platform

    def __hash__(self):
        return hash((self.row_index, self.column_index))

    def __repr__(self):
        return f"{self.shape}, {self.row_index} {self.column_index}"

    def roll(self, direction, limit):
        if self.shape == "O":
            match direction:
                case "N":
                    self.row_index = limit - 1
                case "W":
                    self.column_index = limit - 1
                case "S":
                    self.row_index = limit + 1
                case "E":
                    self.column_index = limit + 1

    def get_weight(self):
        match self.shape:
            case "#":
                return 0
            case "O":
                return self.row_index

    def __lt__(self, other):
        if self.platform.column_mode:
            return self.row_index < other.row_index
        else:
            return self.column_index < other.column_index

    def __eq__(self, other):
        if self.platform.column_mode:
            return self.row_index == other.row_index
        else:
            return self.column_index == other.column_index

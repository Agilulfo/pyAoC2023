from collections import defaultdict
from bisect import bisect

PLATFORM_SIZE = 100
NUMBER_OF_CYCLES = 1000000000


class Platform:
    def __init__(self, platform):
        self.stones = []
        for row_index, row in enumerate(platform):
            for columnd_index, shape in enumerate(row):
                if shape != ".":
                    stone = Stone(
                        shape,
                        PLATFORM_SIZE - row_index,
                        PLATFORM_SIZE - columnd_index,
                        self,
                    )
                    self.stones.append(stone)

    def tilt(self, direction):
        match direction:
            case "N":
                for column in self._build_columns():
                    limit = PLATFORM_SIZE + 1
                    for stone in reversed(column):
                        stone.roll("N", limit)
                        limit = stone.row_index
            case "W":
                for row in self._build_rows():
                    limit = PLATFORM_SIZE + 1
                    for stone in reversed(row):
                        stone.roll("W", limit)
                        limit = stone.column_index
            case "S":
                for column in self._build_columns():
                    limit = -1
                    for stone in column:
                        stone.roll("S", limit)
                        limit = stone.row_index
            case "E":
                for row in self._build_rows():
                    limit = -1
                    for stone in row:
                        stone.roll("E", limit)
                        limit = stone.column_index

    def spin_cycle(self):
        for direction in ("N", "W", "S", "E"):
            self.tilt(direction)

    def spin(self, n):
        for time in range(n):
            print(f"spin: {time}")
            self.spin_cycle()

    def get_weight(self):
        return sum([stone.get_weight() for stone in self.stones])

    # CONTINUE: probably building the columns and rows
    # each time from scratch is too requiring
    # maybe I can keep stones sorted in a more efficient way

    def _build_columns(self):
        self.column_mode = True
        columns = defaultdict(list)
        for stone in self.stones:
            column = columns[stone.column_index]
            column.insert(bisect(column, stone), stone)
        return columns.values()

    def _build_rows(self):
        self.column_mode = False
        rows = defaultdict(list)
        for stone in self.stones:
            row = rows[stone.row_index]
            row.insert(bisect(row, stone), stone)
        return rows.values()


class Stone:
    def __init__(self, shape, row_index, column_index, platform):
        self.shape = shape
        self.row_index = row_index
        self.column_index = column_index
        self.platform = platform

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

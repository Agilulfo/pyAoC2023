from advent.day10.parsing import load_map


def main():
    platform = load_map(file_path=__file__)
    columns = extract_columns(platform)
    total_weight = 0
    for column in columns:
        roll_stones(column)
        total_weight += column_weight(column)
    print(f"the total weight is: {total_weight}")


def extract_columns(platform):
    columns = []
    rows_amount = len(platform)
    for columnd_index in range(len(platform[0])):
        column = []
        for row_index in range(len(platform)):
            shape = platform[row_index][columnd_index]
            if shape != ".":
                position = rows_amount - row_index
                column.append(Stone(shape, position))
        columns.append(column)
    return columns


def column_weight(column):
    return sum([stone.get_weight() for stone in column])


def roll_stones(column):
    limit = 101
    for stone in column:
        stone.roll(limit)
        limit = stone.position


class Stone:
    def __init__(self, shape, position):
        self.shape = shape
        self.position = position

    def __repr__(self):
        return f"{self.shape}, {self.position}"

    def roll(self, limit):
        match self.shape:
            case "#":
                pass
            case "O":
                self.position = limit - 1

    def get_weight(self):
        match self.shape:
            case "#":
                return 0
            case "O":
                return self.position

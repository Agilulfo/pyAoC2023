import sys


class Contraption:
    def __init__(self, field):
        self.field = field
        for row_index, row in enumerate(self.field):
            for column_index, tile in enumerate(row):
                self.field[row_index][column_index] = Tile(
                    tile, row_index, column_index
                )
        limit = len(self.field) * len(self.field[0])
        sys.setrecursionlimit(limit)

    def energize(self, direction="E", row_index=0, column_index=0):
        self.beam_hit(direction, self.field[row_index][column_index])

    def beam_hit(self, direction, tile):
        propagations = [
            (direction, self.pick_tile(direction, tile))
            for direction in tile.energize(direction)
        ]

        for direction, tile in propagations:
            if tile is not None:
                self.beam_hit(direction, tile)

    def pick_tile(self, direction, tile):
        row_index, column_index = tile.row_index, tile.column_index
        match direction:
            case "N":
                row_index -= 1
            case "W":
                column_index -= 1
            case "S":
                row_index += 1
            case "E":
                column_index += 1

        max_row = len(self.field) - 1
        max_column = len(self.field[0]) - 1

        if 0 <= row_index <= max_row and 0 <= column_index <= max_column:
            return self.field[row_index][column_index]
        else:
            return None

    def count_energized_tiles(self):
        counter = 0
        for row in self.field:
            for tile in row:
                if tile.energized:
                    counter += 1
                    tile.reset()
        return counter

    def __repr__(self):
        representation = []
        for row in self.field:
            representation.append("".join([tile.__repr__() for tile in row]))
        return "\n".join(representation)


class Tile:
    def __init__(self, content, row_index, column_index):
        self.content = content
        self.row_index = row_index
        self.column_index = column_index
        self.energized = False
        self.gates = set(["N", "W", "S", "E"])

        # continue remove gates once visited

    def energize(self, beam_direction):
        entrance_gate = opposite_of(beam_direction)
        if entrance_gate not in self.gates:
            return []
        exit_gates = self.propagation_gates(beam_direction)
        self.energized = True
        self.gates.discard(entrance_gate)
        self.gates.difference_update(exit_gates)
        return exit_gates

    def reset(self):
        self.energized = False
        self.gates = set(["N", "W", "S", "E"])

    def propagation_gates(self, beam_direction):
        match self.content:
            case ".":
                return [beam_direction]
            case "/":
                match beam_direction:
                    case "N":
                        return ["E"]
                    case "S":
                        return ["W"]
                    case "W":
                        return ["S"]
                    case "E":
                        return ["N"]
            case "\\":
                match beam_direction:
                    case "N":
                        return ["W"]
                    case "S":
                        return ["E"]
                    case "W":
                        return ["N"]
                    case "E":
                        return ["S"]
            case "-":
                match beam_direction:
                    case "N":
                        return ["W", "E"]
                    case "S":
                        return ["W", "E"]
                    case "W":
                        return [beam_direction]
                    case "E":
                        return [beam_direction]
            case "|":
                match beam_direction:
                    case "N":
                        return [beam_direction]
                    case "S":
                        return [beam_direction]
                    case "W":
                        return ["S", "N"]
                    case "E":
                        return ["S", "N"]

    def __repr__(self):
        if self.content == "." and self.energized:
            return "#"
        else:
            return self.content


def opposite_of(direction):
    match direction:
        case "N":
            return "S"
        case "S":
            return "N"
        case "W":
            return "E"
        case "E":
            return "W"

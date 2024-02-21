from advent.day05 import shared


def main():
    input = shared.parse_input()
    maps = shared.init_maps(input)
    shared.find_lowest_location(SeedIterator(input["seeds"]), maps)
    print("the lowest location is: ", shared.find_lowest_location(input["seeds"], maps))


class SeedIterator:
    def __init__(self, seed_info):
        self.seed_groups = []
        for index in range(0, len(seed_info), 2):
            self.seed_groups.append((seed_info[index], seed_info[index + 1]))
        self.group_index = 0
        self.seed_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.seed_groups) == self.group_index:
            raise StopIteration
        start, group_range = self.seed_groups[self.group_index]
        seed = start + self.seed_index

        self.seed_index += 1

        if self.seed_index == group_range:
            self.seed_index = 0
            self.group_index += 1

        return seed

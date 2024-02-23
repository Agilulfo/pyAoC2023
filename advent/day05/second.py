from advent.day05 import shared


def main():
    input = shared.parse_input()
    maps = shared.init_maps(input)
    seed_ranges = extract_seed_ranges(input["seeds"])

    lowest_location = shared.find_lowest_location_with_ranges(seed_ranges, maps)

    print("the lowest location is: ", lowest_location)


def extract_seed_ranges(seed_info):
    return [
        shared.Range(seed_info[index], seed_info[index + 1])
        for index in range(0, len(seed_info), 2)
    ]

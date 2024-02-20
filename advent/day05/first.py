from advent.day05 import shared


def main():
    input = shared.parse_input()
    maps = shared.init_maps(input)
    shared.find_lowest_location(input["seeds"], maps)
    print("the lowest location is: ", shared.find_lowest_location(input["seeds"], maps))

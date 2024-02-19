from advent.day03 import second


def test_find_adjacent_gears():
    map = [
        ".......*...",
        ".....*XX...",
        "........*..",
        "...........",
    ]

    assert second.adjacent_gears(map, (None, 1, 6, 7)) == [(0, 7), (1, 5), (2, 8)]

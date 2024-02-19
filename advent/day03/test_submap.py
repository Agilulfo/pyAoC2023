from advent.day03 import first


def test_adjacent_submap():
    full_map = [
        "...........",
        "...........",
        "...YYYY....",
        "...YXXY....",
        "...YYYY....",
        "...........",
    ]

    submap = first.adjacent_submap(full_map, 3, 4, 5)

    assert submap == [
        "YYYY",
        "YXXY",
        "YYYY",
    ]


def test_adjacent_submap_corner_top_left():
    full_map = [
        "XXY........",
        "YYY........",
        "...........",
        "...........",
        "...........",
        "...........",
    ]

    submap = first.adjacent_submap(full_map, 0, 0, 1)

    assert submap == ["XXY", "YYY"]


def test_adjacent_submap_corner_bottom_right():
    full_map = [
        "...........",
        "...........",
        "...........",
        "...........",
        "........YYY",
        "........YXX",
    ]

    submap = first.adjacent_submap(full_map, 5, 9, 10)

    assert submap == ["YYY", "YXX"]

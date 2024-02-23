from advent.day05.shared import Range


def test_range_lt():
    range_a = Range(7, 2)
    range_b = Range(34, 5)

    assert range_a < range_b
    assert range_a < 9


def test_range_sorting():
    range_a = Range(3, 4)
    range_b = Range(50, 3)
    range_c = Range(10, 7)
    assert sorted([range_a, range_b, range_c]) == [range_a, range_c, range_b]


def test_range_splitting():
    base = Range(3, 10)
    ranges = base.split_with_ranges([Range(4, 2)])

    assert ranges == [
        (Range(3, 1), None),
        (Range(4, 2), Range(4, 2)),
        (Range(6, 7), None),
    ]

    ranges = base.split_with_ranges([Range(1, 4)])

    assert ranges == [
        (Range(3, 2), Range(1, 4)),
        (Range(5, 8), None),
    ]

    ranges = base.split_with_ranges([Range(4, 1), Range(5, 1)])

    assert ranges == [
        (Range(3, 1), None),
        (Range(4, 1), Range(4, 1)),
        (Range(5, 1), Range(5, 1)),
        (Range(6, 7), None),
    ]

    ranges = base.split_with_ranges([Range(4, 1), Range(6, 1)])

    assert ranges == [
        (Range(3, 1), None),
        (Range(4, 1), Range(4, 1)),
        (Range(5, 1), None),
        (Range(6, 1), Range(6, 1)),
        (Range(7, 6), None),
    ]

    ranges = base.split_with_ranges([Range(10, 5)])

    assert ranges == [(Range(3, 7), None), (Range(10, 3), Range(10, 5))]


def test_range_collision():
    range_a = Range(4, 3)  # 4,5,6

    assert range_a.collides(Range(3, 2))
    assert range_a.collides(Range(4, 1))
    assert range_a.collides(Range(6, 3))
    assert range_a.collides(Range(5, 2))
    assert range_a.collides(Range(5, 1))

    assert not range_a.collides(Range(2, 2))
    assert not range_a.collides(Range(7, 3))

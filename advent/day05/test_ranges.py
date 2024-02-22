from advent.day05.shared import Range


def test_range_sorting():
    range_a = Range(3, 4)
    range_b = Range(50, 3)
    range_c = Range(10, 7)
    assert sorted([range_a, range_b, range_c]) == [range_a, range_c, range_b]

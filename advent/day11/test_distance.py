from advent.day11.first import distance


def test_distance():
    point_a = (0, 3)
    point_b = (7, 10)
    assert distance(point_a, point_b, [], []) == 14

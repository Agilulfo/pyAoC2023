from advent.day05 import shared


def test_map():
    map = shared.Map("seed-to-soil", [[50, 98, 2], [52, 50, 48]])
    assert map.convert_id(50) == 52
    assert map.convert_id(97) == 99
    assert map.convert_id(98) == 50
    assert map.convert_id(100) == 100
    assert map.convert_id(49) == 49


def test_convert_range():
    map = shared.Map("seed-to-soil", [[50, 98, 2], [52, 50, 48]])
    print(map)
    new_ranges = map.convert_range(shared.Range(10, 100))
    print(new_ranges)

    assert new_ranges == [
        shared.Range(10, 40),
        shared.Range(52, 48),
        shared.Range(50, 2),
        shared.Range(100, 10),
    ]

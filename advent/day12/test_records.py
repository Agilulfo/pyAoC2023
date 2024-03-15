import pytest
from advent.day12.records import count_fits, count_arrangements


def test_count_fits():
    assert count_fits("??###??", 3) == 1
    assert count_fits("??#?#??", 3) == 1
    assert count_fits("??##.#??", 3) == 0
    assert count_fits("??##?#??", 3) == 0
    assert count_fits("??.?.??", 1) == 5
    assert count_fits("??.?.??", 2) == 2
    assert count_fits("#?#?#?", 6) == 1


def test_count_arrangements():
    assert count_arrangements("##.##", (2, 2)) == 1
    assert count_arrangements("?#?.???", (2, 2)) == 4
    assert count_arrangements("????", (1, 1)) == 3
    assert count_arrangements("???.###", (1, 1, 3)) == 1
    assert count_arrangements(".??..??...?##.", (1, 1, 3)) == 4
    assert count_arrangements("????.#...#...", (4, 1, 1)) == 1
    assert count_arrangements("????.######..#####.", (1, 6, 5)) == 4
    assert count_arrangements("?###????????", (3, 2, 1)) == 10
    assert count_arrangements("?#?#?#?#?#?#?#?", (1, 3, 1, 6)) == 1

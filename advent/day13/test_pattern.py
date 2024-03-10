from advent.day13.pattern import Pattern


def test_simmetry():
    pattern = Pattern(
        [
            "#...#..##.#..##..",
            "..###.#.##..#..##",
            ".....#...#####.##",
            ".....#...#####.##",
            "..###.#.##..#..##",
            "#...#..##.#..##..",
            ".##.#.###.###..##",
            ".###.#.#..#.#.#.#",
            "##...#.#.....#.#.",
            ".#...#..##.##..#.",
            "######.#..#..##.#",
            "#######.##.....#.",
            "####.##.##.....#.",
        ]
    )

    assert pattern.get_primary_simmetry() == (True, 2)


def test_symmetry_multiple_matches():
    pattern = Pattern(
        [
            ".##..##",
            "###..##",
            "#..##..",
            "#..##..",
            "##....#",
            ".##..##",
            "##.##.#",
            "###..##",
            ".##..##",
            "..#..#.",
            ".#.##.#",
        ]
    )

    assert pattern.get_primary_simmetry() == (False, 3)


def test_partial_simmetry():
    pattern = Pattern(
        [
            "..#..####..#.",
            "##.#.#..#.#..",
            "...#..##..#..",
            "##.#......#.#",
            "###.##..##.##",
            "...########..",
            "..##..##..##.",
            "##.###..###.#",
            "..##..##..##.",
        ]
    )

    assert pattern.get_primary_simmetry() == (False, 0)


def test_secondary_simmetry():
    pattern = Pattern(
        [
            "..#..####..#.",
            "##.#.#..#.#..",
            "...#..##..#..",
            "##.#......#.#",
            "###.##..##.##",
            "...########..",
            "..##..##..##.",
            "##.###..###.#",
            "..##..##..##.",
        ]
    )

    assert pattern.get_secondary_simmetry() == (False, 6)


def test_compatible_mirror_index():
    assert not Pattern.compatible_mirror_index(7, 15)


def test_something():
    pattern = Pattern(
        [
            ".##.#.#",
            "###..##",
            "#..#.#.",
            "#..#...",
            "#..#...",
            "#.##.#.",
            "###..##",
            ".##.#.#",
            ".##.#.#",
            "###..##",
            "#.##.#.",
            "#..#...",
            "#..#...",
            "#..#.#.",
            "###..##",
            ".##.#.#",
            "....#..",
        ]
    )

    pattern.get_secondary_simmetry() == (False, 100)


def test_transpose():
    assert Pattern.transpose(["12", "34"]) == ["13", "24"]

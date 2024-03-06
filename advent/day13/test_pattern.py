from advent.day13.first import Pattern


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

    assert pattern.find_simmetry() == (True, 3)


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

    assert pattern.find_simmetry() == (False, 4)


def test_transpose():
    assert Pattern.transpose(["12", "34"]) == ["13", "24"]

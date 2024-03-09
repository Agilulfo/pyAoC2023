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

    assert pattern.find_simmetry()["valid"] == (True, 2)


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

    assert pattern.find_simmetry()["valid"] == (False, 3)


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

    simmetries = pattern.find_simmetry()
    print(simmetries)
    assert simmetries["valid"] == (False, 0)
    assert simmetries["partial"] == [(False, 6)]


def test_transpose():
    assert Pattern.transpose(["12", "34"]) == ["13", "24"]

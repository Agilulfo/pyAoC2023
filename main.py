import argparse
import importlib

DAYS = 25
PARTS = 2

parser = argparse.ArgumentParser(description="Advent Of Code 2023 challenges runner.")
parser.add_argument('day', type=int, choices = list(range(1,DAYS + 1)))
parser.add_argument("part", type=int, choices = list(range(1, PARTS + 1)))

arguments = parser.parse_args()

day = "%02d"%arguments.day
part = "first" if arguments.part == 1 else "second"

module = importlib.import_module("advent.day%s.%s"%(day, part))
module.main()

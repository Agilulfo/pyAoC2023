import math
import functools
from advent.day08 import parsing
from advent.day08.graph import Graph


def main():
    # my initial strategy (without too much hope) was a bruteforce approach
    # however as expected things do not allign quickly
    # since there is some periodicity involved I've figured out that
    # maybe a Least commond multiple could help to calculate when things
    # will allign. it worked!

    directions, nodes = parsing.parse_input()
    node_ids = [id for id, _, _ in nodes if id[-1] == "A"]
    periods = []

    graph = Graph(nodes)

    for node_id in node_ids:
        counter = 0
        while node_id[-1] != "Z":
            counter += 1
            node_id = graph.follow_path(node_id, directions)
        periods.append(counter)

    steps = functools.reduce(lcm, periods) * len(directions)

    print(f"needed {steps} steps")


# thanks google
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

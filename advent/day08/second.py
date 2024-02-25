from advent.day08 import parsing
from advent.day08.graph import Graph


def main():
    directions, nodes = parsing.parse_input()
    node_ids = [id for id, _, _ in nodes if id[-1] == "A"]

    graph = Graph(nodes)
    counter = 0

    while not all_z(node_ids):
        counter += 1
        node_ids = [graph.follow_path(node_id, directions) for node_id in node_ids]
    print(f"needed {counter*len(directions)} steps")


def all_z(node_ids):
    for id in node_ids:
        if id[-1] != "Z":
            return False
    return True

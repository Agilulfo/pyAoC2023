from advent.day08 import parsing
from advent.day08.graph import Graph


def main():
    directions, nodes = parsing.parse_input()
    node_id = "AAA"
    destination_id = "ZZZ"

    graph = Graph(nodes)
    counter = 0

    while True:
        counter += 1
        node_id = graph.follow_path(node_id, directions)
        if node_id == destination_id:
            break

    print(f"needed {counter*len(directions)} steps")

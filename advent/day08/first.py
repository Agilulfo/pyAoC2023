from advent import utils


def main():
    directions, nodes = parse_input()
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


def parse_input():
    with open(utils.input_path(__file__)) as input:
        directions = input.readline()[:-1]
        input.readline()
        nodes = [parse_line(line) for line in input]
        return directions, nodes


def parse_line(line):
    return (line[0:3], line[7:10], line[12:15])


class Node:
    def __init__(self, description):
        # not ideal way to implement a graph but will do :-p
        self.id, self.left, self.right = description

    def __repr__(self):
        return f"Node: {self.id}, L:{self.left} R:{self.right}"


class Graph:
    def __init__(self, nodes_description):
        self.node_index = {
            id: Node((id, left, right)) for id, left, right in nodes_description
        }

    def follow_path(self, node_id, instructions):
        node = self.node_index[node_id]

        for step in instructions:
            print(node)
            print(step)
            match step:
                case "L":
                    node = self.node_index[node.left]
                case "R":
                    node = self.node_index[node.right]
        return node.id

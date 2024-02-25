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
            match step:
                case "L":
                    node = self.node_index[node.left]
                case "R":
                    node = self.node_index[node.right]
        return node.id

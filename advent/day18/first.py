from advent.day18.parsing import parse_input
from PIL import Image, ImageDraw

# after inspecting the input I've found out that
# the path expand in all four quadrans of the plane
# if we start from point 0,0


def main():
    instructions = parse_input()

    origin = Point(0, 0)
    start_point = origin

    edges = []
    for direction, distance, _ in instructions:
        edge = Edge(start_point, direction, distance)
        start_point = edge.end()
        edges.append(edge)

    min_x, max_x, min_y, max_y = 0, 0, 0, 0

    prev = edges[-1]

    for edge in edges:
        prev.set_next(edge)
        prev = edge

        min_x = min(min_x, edge.start.x)
        min_y = min(min_y, edge.start.y)
        max_x = max(max_x, edge.start.x)
        max_y = max(max_y, edge.start.y)

    dim_x = max_x - min_x + 1
    dim_y = max_y - min_y + 1

    img = Image.new("1", (dim_x, dim_y))

    delta_x = -min_x
    delta_y = -min_y

    for edge in edges:
        edge.start.translate(delta_x, delta_y)

    draw = ImageDraw.Draw(img)
    for edge in edges:
        a = edge.start
        b = edge.next.start
        draw.line([(a.x, a.y), (b.x, b.y)], fill=255)

    left_most_edge = None

    for edge in edges:
        if edge.direction in ["U", "D"] and edge.start.x == 0:
            left_most_edge = edge
            break

    seed_x = 1
    seed_y = None

    if left_most_edge.direction == "U":
        seed_y = left_most_edge.start.y + 1
    else:
        seed_y = left_most_edge.start.y - 1

    ImageDraw.floodfill(img, (seed_x, seed_y), 255)

    counter = 0
    for x in range(dim_x):
        for y in range(dim_y):
            if img.getpixel((x, y)) == 255:
                counter += 1

    print(f"lake size is: {counter}")

    # for debugging purporse
    # img.save("test.png")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


class Edge:
    def __init__(self, start, direction, distance):
        self.start = start
        self.direction = direction
        self.distance = distance

    def end(self):
        match self.direction:
            case "U":
                return Point(self.start.x, self.start.y + self.distance)
            case "D":
                return Point(self.start.x, self.start.y - self.distance)
            case "R":
                return Point(self.start.x + self.distance, self.start.y)
            case "L":
                return Point(self.start.x - self.distance, self.start.y)

    def set_next(self, edge):
        self.next = edge

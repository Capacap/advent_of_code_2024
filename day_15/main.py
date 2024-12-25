import os
from time import sleep


def parse_input(file_path):
    walls = set()
    boxes = set()
    robot = ()
    commands = []
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")
        for y, line in enumerate(lines):
            for x, symbol in enumerate(line):
                if symbol == "#":
                    walls.add((x, y))
                if symbol == "O":
                    boxes.add((x, y))
                if symbol == "@":
                    robot = (x, y)

                if symbol == "<":
                    commands.append((-1, 0))
                if symbol == ">":
                    commands.append((1, 0))
                if symbol == "v":
                    commands.append((0, 1))
                if symbol == "^":
                    commands.append((0, -1))

    return walls, boxes, robot, commands


class Entity:
    def __init__(self, x: int, y: int, static: bool, size: int):
        self.x = x
        self.y = y
        self.static = static
        self.size = size

    def __repr__(self):
        return f"[({self.x}, {self.y}), {self.size}, {self.static}]"


class Simulation:
    def __init__(
        self,
        dynamic_entities: list[tuple],
        static_entities: list[tuple],
        operator: tuple,
        part_02: bool,
    ):
        self.entities: list[Entity] = []

        for e in dynamic_entities:
            x = e[0] * 2 if part_02 else e[0]
            y = e[1]
            static = False
            size = 2 if part_02 else 1
            self.entities.append(Entity(x, y, static, size))

        for e in static_entities:
            x = e[0] * 2 if part_02 else e[0]
            y = e[1]
            static = True
            size = 2 if part_02 else 1
            self.entities.append(Entity(x, y, static, size))

        x = operator[0] * 2 if part_02 else operator[0]
        y = operator[1]
        static = False
        size = 1
        self.entities.append(Entity(x, y, static, size))
        self.operator: Entity = self.entities[-1]

    def simulate(self, command):
        self._move_operator(command[0], command[1])

    def _move_operator(self, dx, dy):
        entity_map = {}
        for e in self.entities:
            for i in range(e.size):
                entity_map[(e.x + i, e.y)] = e

        cluster = set()
        frontier = set([self.operator])
        while frontier:
            e = frontier.pop()
            cluster.add(e)
            neighbours = set()
            for i in range(e.size):
                x = e.x + dx + i
                y = e.y + dy
                n = entity_map.get((x, y), None)
                if n:
                    neighbours.add(n)
                    
            for n in neighbours:
                if n not in cluster and n not in frontier:
                    frontier.add(n)

        if any([c.static for c in cluster]):
            return

        for c in cluster:
            c.x += dx
            c.y += dy

    def print(self):
        max_x, max_y = 0, 0
        for e in self.entities:
            max_x = max(max_x, e.x)
            max_y = max(max_y, e.y)

        rows = [["." for _ in range(max_x + 2)] for _ in range(max_y + 1)]

        for e in self.entities:
            if e == self.operator:
                continue

            if e.static:
                rows[e.y][e.x] = "<"
                rows[e.y][e.x + 1] = ">"
            else:
                rows[e.y][e.x] = "["
                rows[e.y][e.x + 1] = "]"
            

        rows[self.operator.y][self.operator.x] = "@"

        for i, row in enumerate(rows):
            print("".join(row))

    def calc_gps_sum(self):
        gps_sum = 0
        for e in self.entities:
            if e.static or e == self.operator:
                continue

            gps_sum += (e.y * 100) + (e.x)

        return gps_sum


def main():
    walls, boxes, robot, commands = parse_input("./day_15/input.txt")

    sim = Simulation(boxes, walls, robot, False)
    for command in commands:
        sim.simulate(command)
    print(sim.calc_gps_sum())  # Part 1 - 1406628

    sim = Simulation(boxes, walls, robot, True)
    for command in commands:
        sim.simulate(command)
    print(sim.calc_gps_sum())  # Part 2 - 1432781


if __name__ == "__main__":
    main()

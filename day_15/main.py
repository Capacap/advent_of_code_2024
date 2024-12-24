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
                if symbol == "^":
                    commands.append((0, -1))
                if symbol == "v":
                    commands.append((0, 1))

    return walls, boxes, robot, commands


class Entity():
    def __init__(self, x: int, y: int, static: bool):
        self.x = x
        self.y = y
        self.static = static


class Simulation():
    def __init__(self, dynamic_entities: list[tuple], static_entities: list[tuple], operator: tuple):
        self.entities: list[Entity] = []

        for w in dynamic_entities:
            self.entities.append(Entity(w[0], w[1], True))
        
        for b in static_entities:
            self.entities.append(Entity(b[0], b[1], False))

        self.entities.append(Entity(operator[0], operator[1], False))
        self.operator: Entity = self.entities[-1]


    def simulate(self, command):
        self.move_operator(command[0], command[1])

        
    def move_operator(self, dx, dy):
        xy_to_entity_map = {}
        for entity in self.entities:
            xy_to_entity_map[(entity.x, entity.y)] = entity

        x = self.operator.x
        y = self.operator.y

        cascade = []
        while True:
            xy = (x, y)
            entity = xy_to_entity_map.get(xy, None)

            # No further entities for motion to cascade onto
            if not entity:
                break

            # Cascade stopped by a static entity
            if entity and entity.static:
                cascade.clear()
                break

            # Movement cascades onto an additional entity
            if entity and not entity.static:
                cascade.append(entity)
                x += dx
                y += dy

        # Apply motion to cascade
        for e in cascade:
            e.x += dx
            e.y += dy

        

    def print(self):
        max_x, max_y = 0, 0
        for e in self.entities:
            max_x = max(max_x, e.x)
            max_y = max(max_y, e.y)

        rows = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        for e in self.entities:
            symbol = "#" if e.static else "O"
            rows[e.y][e.x] = symbol

        rows[self.operator.y][self.operator.x] = "@"

        for row in rows:
            print("".join(row))


    def calc_gps_sum(self):
        gps_sum = 0
        for e in self.entities:
            if e.static or e == self.operator:
                continue

            gps_sum += e.y * 100 + e.x

        return gps_sum


def main():
    walls, boxes, robot, commands = parse_input("./day_15/input.txt")

    sim = Simulation(walls, boxes, robot)
    sim.print()
    print("SIMULATING...")
    for command in commands:
        sim.simulate(command)
    sim.print()

    print(sim.calc_gps_sum()) # Part 1 - 1406628


if __name__ == "__main__":
    main()
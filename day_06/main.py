from copy import copy
from typing import Dict, Tuple, Set


class Simulation:
    def __init__(self):
        self.obstacles: Set[Tuple[int, int]] = {}
        self.bounds: Tuple[int, int] = (0, 0)
        self.guard_pos: Tuple[int, int] = (0, 0)
        self.guard_dir: Tuple[int, int] = (0, 0)
        self.guard_oob: bool = False
        self.guard_obstructed: bool = False

        self._turn_map: Dict[Tuple[int, int], Tuple[int, int]] = {
            (0, -1): (1, 0),
            (-1, 0): (0, -1),
            (1, 0): (0, 1),
            (0, 1): (-1, 0),
        }

    def progress_simulation(self):
        x = self.guard_pos[0] + self.guard_dir[0]
        y = self.guard_pos[1] + self.guard_dir[1]
        next_pos = (x, y)

        self.guard_obstructed = False
        if next_pos in self.obstacles:
            self.guard_obstructed = True
            self.guard_dir = self._turn_map[self.guard_dir]
        else:
            self.guard_pos = (x, y)

        self.guard_oob = False
        if not 0 <= x <= self.bounds[0]:
            self.guard_oob = True

        if not 0 <= y <= self.bounds[1]:
            self.guard_oob = True


def main() -> None:
    init_guard_pos = (0, 0)
    init_guard_dir = (0, 0)
    obstacles = set()
    max_x = 0
    max_y = 0

    with open("./day_06/input.txt", "r") as file:
        for y, line in enumerate(file):
            max_y = max(max_y, y)
            for x, symbol in enumerate(line.strip()):
                max_x = max(max_x, x)

                if symbol == "#":
                    obstacles.add((x, y))

                if symbol == "^":
                    init_guard_pos = (x, y)
                    init_guard_dir = (0, -1)

    sim = Simulation()
    sim.obstacles = obstacles
    sim.bounds = (max_x, max_y)
    sim.guard_pos = init_guard_pos
    sim.guard_dir = init_guard_dir

    path = set()
    while not sim.guard_oob:
        path.add(sim.guard_pos)
        sim.progress_simulation()

    print(len(path)) # Part 1 - 4973

    loop_possibilities = set()
    for tile in path:
        new_sim = Simulation()
        new_sim.obstacles = set.union(sim.obstacles, [tile])
        new_sim.bounds = (max_x, max_y)
        new_sim.guard_pos = init_guard_pos
        new_sim.guard_dir = init_guard_dir

        turns = set()
        while not new_sim.guard_oob:
            new_sim.progress_simulation()
            if new_sim.guard_obstructed:
                if (new_sim.guard_pos, new_sim.guard_dir) in turns:
                    loop_possibilities.add(tile)
                    break
                turns.add((new_sim.guard_pos, new_sim.guard_dir))

    print(len(loop_possibilities)) # Part 2 - 1482


if __name__ == "__main__":
    main()

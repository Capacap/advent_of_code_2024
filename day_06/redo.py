from copy import copy, deepcopy
from typing import Dict, Tuple, Set


class Simulation:
    def __init__(self):
        self.obstacles: Set[Tuple[int, int]] = {}
        self.bounds: Tuple[int, int] = (0, 0)
        self.guard_pos: Tuple[int, int] = (0, 0)
        self.guard_dir: Tuple[int, int] = (0, 0)
        self.guard_oob: bool = False

    def progress_simulation(self):
        x = self.guard_pos[0] + self.guard_dir[0]
        y = self.guard_pos[1] + self.guard_dir[1]
        next_pos = (x, y)

        if next_pos in self.obstacles:
            self.guard_dir = get_turn_direction(self.guard_dir)
            x = self.guard_pos[0] + self.guard_dir[0]
            y = self.guard_pos[1] + self.guard_dir[1]

        self.guard_pos = (x, y)
        
        self.guard_oob = False
        if not 0 <= x <= self.bounds[0]:
            self.guard_oob = True

        if not 0 <= y <= self.bounds[1]:
            self.guard_oob = True


def get_turn_direction(dir):
    match dir:
        case (0, -1):
            dir = (1, 0)  # ^ - >
        case (-1, 0):
            dir = (0, -1)  # < - ^
        case (1, 0):
            dir = (0, 1)  # > - v
        case (0, 1):
            dir = (-1, 0)  # v - <
    return dir


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

    path = []
    tiles = set()
    while True:
        path.append(sim.guard_pos)
        tiles.add(sim.guard_pos)
        sim.progress_simulation()
        if sim.guard_oob:
            break

    print(len(tiles))

    l = set()
    for pos in path:
        if pos == init_guard_pos:
            continue

        if pos in l:
            continue

        new_sim = copy(sim)
        new_sim.obstacles = set.union(sim.obstacles, [pos])
        new_sim.guard_pos = init_guard_pos
        new_sim.guard_dir = init_guard_dir
        
        route = {}
        rethread_count = 0
        while True:

            prev_dir = new_sim.guard_dir
            new_sim.progress_simulation()

            if new_sim.guard_pos in route:
                if route[new_sim.guard_pos] == new_sim.guard_dir:
                    rethread_count += 1
                    if rethread_count > 10:
                        l.add(pos)
                        break
            else:
                route[new_sim.guard_pos] = prev_dir

            if new_sim.guard_oob:
                break

    print(len(l))


if __name__ == "__main__":
    main()

from copy import copy, deepcopy
from typing import Dict, Tuple


class Simulation:
    def __init__(self):
        self.layout: Dict[int] = {}
        self.layout_bounds: Tuple[int, int] = (0, 0)
        self.guard_pos: Tuple[int, int] = (0, 0)
        self.guard_dir: Tuple[int, int] = (0, 0)
        self.guard_oob: bool = False

    def progress_simulation(self):
        # Check out-of-bounds
        if (
            self.guard_pos[0] < 0
            or self.guard_pos[0] > self.layout_bounds[0]
            or self.guard_pos[1] < 0
            or self.guard_pos[1] > self.layout_bounds[1]
        ):
            self.guard_oob = True
            return self

        # Handle collisions
        next_pos = (
            self.guard_pos[0] + self.guard_dir[0],
            self.guard_pos[1] + self.guard_dir[1],
        )
        next_tile = self.layout.get(next_pos, 0)
        if next_tile == 1:
            self.guard_dir = get_turn_direction(self.guard_dir)

        # Move guard
        self.guard_pos = (
            self.guard_pos[0] + self.guard_dir[0],
            self.guard_pos[1] + self.guard_dir[1],
        )
        return self


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
    guard_pos = (0, 0)
    guard_dir = (0, 0)
    layout = {}
    max_x = 0
    max_y = 0
    # Parse input for initial state of the simulation
    with open("./day_06/input.txt", "r") as file:
        for y, line in enumerate(file):
            # Calculate span of the y-axis
            max_y = max(max_y, y)

            for x, symbol in enumerate(line.strip()):
                # Calculate span of the x-axis
                max_x = max(max_x, x)

                # Parse symbol as a tile type (0 = clear, 1 = wall)
                tile_type = 0
                if symbol == "#":
                    tile_type = 1

                # Update layout
                coo = (x, y)
                layout[coo] = tile_type

                # Check if symbol is guard starting position
                if symbol in ["^", "<", ">", "v"]:
                    guard_pos = (x, y)
                    match symbol:
                        case "^":
                            guard_dir = (0, -1)
                        case "<":
                            guard_dir = (-1, 0)
                        case ">":
                            guard_dir = (1, 0)
                        case "v":
                            guard_dir = (0, 1)

    # Initialize the simulation
    simulation = Simulation()
    simulation.layout = layout
    simulation.layout_bounds = (max_x, max_y)
    simulation.guard_pos = guard_pos
    simulation.guard_dir = guard_dir
    simulation.guard_oob = False

    patrol = []
    turns = []
    # Start the simulation
    while True:
        # Cache current simulation state then progress the simulation
        prev = copy(simulation)
        next = simulation.progress_simulation()

        # Check if simulation should end
        if next.guard_oob:
            break

        # Add tile to patrol route
        if prev.guard_pos not in patrol:
            patrol.append(prev.guard_pos)

        # Check if guard has turned
        if (
            prev.guard_dir[0] != next.guard_dir[0]
            or prev.guard_dir[1] != next.guard_dir[1]
        ):
            turns.append(prev.guard_pos)

    print(len(patrol))
    print(len(turns))


if __name__ == "__main__":
    main()

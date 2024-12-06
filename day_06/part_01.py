from typing import List

def main() -> None:
    guard_coo = (0, 0)
    guard_dir = (0, 0)
    coo_to_tile = {}
    max_x = 0
    max_y = 0
    with open("./day_06/input.txt", "r") as file:
        for y, line in enumerate(file):
            max_y = max(max_y, y)
            for x, symbol in enumerate(line.strip()):
                max_x = max(max_x, x)
                coo = (x, y)
                coo_to_tile[coo] = symbol
                if symbol in ["^", "<", ">", "v"]:
                    guard_coo = (x, y)
                    match symbol:
                        case "^": guard_dir = (0, -1)
                        case "<": guard_dir = (-1, 0)
                        case ">": guard_dir = (1, 0)
                        case "v": guard_dir = (0, 1)
                    coo_to_tile[coo] = "."

    patrol = []
    while True:
        # Check out-of-bounds
        if guard_coo[0] < 0 or guard_coo[0] > max_x:
            break
        if guard_coo[1] < 0 or guard_coo[1] > max_y:
            break
        
        # Handle collisions
        next_coo = (guard_coo[0] + guard_dir[0], guard_coo[1] + guard_dir[1])
        next_tile = coo_to_tile.get(next_coo, ".")
        if next_tile == "#":
            match guard_dir:
                case (0, -1): guard_dir = (1, 0)  # ^ - >
                case (-1, 0): guard_dir = (0, -1) # < - ^
                case (1, 0):  guard_dir = (0, 1)  # > - v
                case (0, 1):  guard_dir = (-1, 0) # v - <

        # Mark patrolled location
        if guard_coo not in patrol:
            patrol.append(guard_coo)

        # print(f"{guard_coo} - {guard_dir}")

        # Move guard
        guard_coo = (guard_coo[0] + guard_dir[0], guard_coo[1] + guard_dir[1])

    print(len(patrol))
                

if __name__ == "__main__":
    main()
from typing import Set, Dict
from itertools import combinations

class Antenna:
    x:int
    y:int
    frequency: int

def main() -> None:
    freq_count: int = 0
    symbol_to_freq_index: Dict[str, int] = {}
    antennas: Set[Antenna] = set()
    max_x: int = 0
    max_y: int = 0

    with open("./day_08/input.txt", "r") as file:
        for y, line in enumerate(file):
            max_y = max(max_y, y)
            for x, symbol in enumerate(line.strip()):
                max_x = max(max_x, x)
                if not symbol == ".":
                    if symbol not in symbol_to_freq_index:
                        symbol_to_freq_index[symbol] = freq_count
                        freq_count += 1
                    antenna = Antenna()
                    antenna.x = x
                    antenna.y = y
                    antenna.frequency = symbol_to_freq_index[symbol]
                    antennas.add(antenna)

    antinodes = set()
    for freq in range(freq_count):
        subset = [a for a in antennas if a.frequency == freq]
        for pair in combinations(subset, 2):
            for order in [(pair[0], pair[1]), (pair[1], pair[0])]:
                a = order[0]
                b = order[1]
                dx = a.x - b.x
                dy = a.y - b.y
                x = a.x + dx
                y = a.y + dy
                if 0 <= x <= max_x and 0 <= y <= max_y:
                    antinodes.add((x, y))

    print(len(antinodes)) # Part 1 - 265

    antinodes = set()
    for freq in range(freq_count):
        subset = [a for a in antennas if a.frequency == freq]
        for pair in combinations(subset, 2):
            for order in [(pair[0], pair[1]), (pair[1], pair[0])]:
                a = order[0]
                b = order[1]
                dx = a.x - b.x
                dy = a.y - b.y

                x = a.x + dx
                y = a.y + dy
                while True:
                    if 0 <= x <= max_x and 0 <= y <= max_y:
                        antinodes.add((x, y))
                        x += dx
                        y += dy
                    else:
                        break

                x = a.x - dx
                y = a.y - dy
                while True:
                    if 0 <= x <= max_x and 0 <= y <= max_y:
                        antinodes.add((x, y))
                        x -= dx
                        y -= dy
                    else:
                        break

    print(len(antinodes)) # Part 2 - 962

if __name__ == "__main__":
    main()

from collections import deque


def bfs(origin: tuple, layout: dict[tuple, int]) -> list[tuple]:
    explored: set[tuple] = set()
    frontier: deque[tuple] = deque([origin])
    while frontier:
        tile: tuple = frontier.popleft()
        if tile in explored:
            continue
        explored.add(tile)
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            xy: tuple = (tile[0] + d[0], tile[1] + d[1])
            if xy in layout and xy not in explored and layout[tile] == layout[xy]:
                frontier.append(xy)
    return explored


def find_islands(layout: dict[tuple, int]) -> list[tuple]:
    islands: list[set[tuple]] = []
    forbidden: set[tuple] = set()
    for xy in layout.keys():
        if xy in forbidden:
            continue
        island = bfs(xy, layout)
        islands.append(island)
        forbidden.update(island)
    return islands


def calc_island_area(island: set[tuple]) -> int:
    return len(island)


def calc_island_perimeter(island: set[tuple]):
    perimeter: int = 0
    for tile in island:
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            xy: tuple = (tile[0] + d[0], tile[1] + d[1])
            if xy not in island:
                perimeter += 1
    return perimeter


def find_island_borders(island: set[tuple]) -> set[tuple]:
    borders: set[tuple] = set()
    for tile in island:
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            xy: tuple = (tile[0] + d[0], tile[1] + d[1])
            if xy not in island:
                border_tile = (xy[0], xy[1], d[0], d[1])
                borders.add(border_tile)
    return borders


def calc_island_sides(island: set[tuple]) -> int:
    borders: set[tuple] = find_island_borders(island)

    sides = []
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        tiles = [(tile[0], tile[1]) for tile in borders if tile[2] == d[0] and tile[3] == d[1]]
        layout = {tile: 0 for tile in tiles}
        forbidden = set()
        for xy in tiles:
            if xy in forbidden:
                continue
            side = bfs(xy, layout)
            sides.append(side)
            forbidden.update(side)

    return len(sides)


def main() -> None:
    layout: dict[tuple, int] = {}
    with open("./day_12/input.txt", "r") as file:
        tile_types: list[str] = []
        for y, line in enumerate(file):
            for x, symbol in enumerate(line.strip()):
                if symbol not in tile_types:
                    tile_types.append(symbol)
                layout[(x, y)] = tile_types.index(symbol)

    islands: list[set[tuple]] = find_islands(layout)

    island_areas: list[int] = []
    for island in islands:
        island_areas.append(calc_island_area(island))

    island_perimeters: list[int] = []
    for island in islands:
        island_perimeters.append(calc_island_perimeter(island))

    island_sides: list[int] = []
    for island in islands:
        island_sides.append(calc_island_sides(island))

    total_price: int = 0
    for area, perimeter in zip(island_areas, island_perimeters):
        total_price += area * perimeter

    print(total_price) # Part 1 - 1473408

    total_price: int = 0
    for area, sides in zip(island_areas, island_sides):
        total_price += area * sides

    print(total_price) # Part 2 - 886364


if __name__ == "__main__":
    main() 
def bfs(origin, heightmap, bounds):
    explored: set[tuple] = set()
    frontier: set[tuple] = set()
    frontier.add(origin)
    while len(frontier) > 0:
        c = frontier.pop()
        explored.add(c)
        for delta in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x: int = c[0] + delta[0]
                y: int = c[1] + delta[1]
                if 0 <= x <= bounds[0] and 0 <= y <= bounds[1]:
                    c_height = heightmap[c]
                    xy_height = heightmap[(x, y)]
                    is_explored = (x, y) in explored
                    if xy_height == c_height + 1 and not is_explored:
                        frontier.add((x, y))
    return explored


def dfs(current, destination, path, paths, explored, heightmap, bounds):
    if path is None:
        path = []

    if paths is None:
        paths = []

    if explored is None:
        explored = {}

    path.append(current)

    if current == destination:
        paths.append(path.copy())
        path.pop()
        return paths

    explored[current] = True
    for delta in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        x: int = current[0] + delta[0]
        y: int = current[1] + delta[1]
        if 0 <= x <= bounds[0] and 0 <= y <= bounds[1]:
            c_height = heightmap[current]
            xy_height = heightmap[(x, y)]
            is_explored = explored.get((x, y), False)
            if xy_height == c_height + 1 and not is_explored:
                dfs((x, y), destination, path, paths, explored, heightmap, bounds)
    explored[current] = False

    path.pop()
    return paths
            

def main() -> None:
    trailheads: set[tuple] = set()
    heightmap: dict[tuple, int] = {}
    heightmap_bounds: list[int, int] = [0, 0]
    with open("./day_10/input.txt", "r") as file:
        for y, line in enumerate(file):
            heightmap_bounds[1] = max(heightmap_bounds[1], y)
            for x, symbol in enumerate(line.strip()):
                heightmap_bounds[0] = max(heightmap_bounds[0], x)
                heightmap[(x, y)] = int(symbol)
                if heightmap[(x, y)] == 0:
                    trailheads.add((x, y))

    trailhead_to_score: dict[tuple, int] = {}
    trailhead_to_rating: dict[tuple, int] = {}
    for trailhead in trailheads:
        explored: set[tuple] = bfs(trailhead, heightmap, heightmap_bounds)
        trailhead_to_score[trailhead] = len([xy for xy in explored if heightmap[xy] == 9])

        trailhead_to_rating[trailhead] = 0
        for trailend in [xy for xy in explored if heightmap[xy] == 9]:
            paths = dfs(trailhead, trailend, [], [], {}, heightmap, heightmap_bounds)
            trailhead_to_rating[trailhead] += len(paths)

    print(sum(trailhead_to_score.values())) # Part 1 - 733
    print(sum(trailhead_to_rating.values())) # Part 2 - 1514

if __name__ == "__main__":
    main()

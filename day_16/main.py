import math
import heapq

def angle_between(v1, v2):
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
    magnitude_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
    cos_theta = dot_product / (magnitude_v1 * magnitude_v2)
    cos_theta = max(-1.0, min(1.0, cos_theta))
    angle = math.degrees(math.acos(cos_theta))
    return angle

def parse_input(file_path):
    walls = set()
    start = None
    end = None
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")
        for y, line in enumerate(lines):
            for x, symbol in enumerate(line):
                if symbol == "#":
                    walls.add((x, y))
                elif symbol == "S":
                    start = (x, y)
                elif symbol == "E":
                    end = (x, y)
    return start, end, walls

def print_maze(walls, path):
    max_x, max_y = 0, 0
    for w in walls:
        max_x = max(max_x, w[0])
        max_y = max(max_y, w[1])

    rows = [["." for _ in range(max_x + 2)] for _ in range(max_y + 1)]

    for w in walls:
        rows[w[1]][w[0]] = "#"

    for i in range(len(path)):
        heading = (-1, 0)
        if i > 0:
            prev = path[i-1]
            next = path[i]
            heading = (next[0] - prev[0], next[1] - prev[1])

        symbol = "x"
        if heading == (1, 0):
            symbol = ">"
        elif heading == (-1, 0):
            symbol = "<"
        elif heading == (0, -1):
            symbol = "^"
        elif heading == (0, 1):
            symbol = "v"

        rows[path[i][1]][path[i][0]] = symbol

    for row in rows:
        print("".join(row))

def main():
    start, end, walls = parse_input("./day_16/input.txt")

    travel_map = {start: None}
    cost_map = {start: 0}
    heading_map = {start: (1, 0)}
    frontier_queue = [(0, start)]

    while frontier_queue:
        current_cost, current_xy = heapq.heappop(frontier_queue)

        if current_cost > cost_map[current_xy]:
            continue

        for heading in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbour_xy = (current_xy[0] + heading[0], current_xy[1] + heading[1])

            if neighbour_xy in walls:
                continue

            angle = angle_between(heading_map[current_xy], heading)
            turns = round(angle / 90)
            cost = current_cost + 1 + turns * 1000
            if cost < cost_map.get(neighbour_xy, math.inf):
                travel_map[neighbour_xy] = current_xy
                cost_map[neighbour_xy] = cost
                heading_map[neighbour_xy] = heading
                heapq.heappush(frontier_queue, (cost, neighbour_xy))

    path = []
    current = end
    while travel_map[current]:
        current = travel_map[current]
        path.append(current)
    path.reverse()

    print_maze(walls, path)
    print(cost_map[end]) # Part 1 - 106512

if __name__ == "__main__":
    main()

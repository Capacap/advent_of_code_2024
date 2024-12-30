import math
from functools import cache
from collections import deque

@cache
def calc_90deg_turns(a, b):
    dot_product = a[0] * b[0] + a[1] * b[1]
    magnitude_a = math.sqrt(a[0] ** 2 + a[1] ** 2)
    magnitude_b = math.sqrt(b[0] ** 2 + b[1] ** 2)
    cos_theta = dot_product / (magnitude_a * magnitude_b)
    cos_theta = max(-1.0, min(1.0, cos_theta))
    angle = math.degrees(math.acos(cos_theta))
    turns = round(angle / 90)
    return turns

def visualize_graph(graph, highlight_nodes):
    max_x, max_y = 0, 0
    for x, y in graph:
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    rows = [["░" for _ in range(max_x + 2)] for _ in range(max_y + 2)]
    
    for x, y in graph:
        rows[y][x] = "▒"

    for x, y in highlight_nodes:
        rows[y][x] = "█"

    for row in rows:
        print("".join(row))

def build_node_graph(file_path):
    graph = {}
    nodes = set()
    start = None
    end = None
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")
        for y, line in enumerate(lines):
            for x, symbol in enumerate(line):
                if symbol == ".":
                    nodes.add((x, y))
                if symbol == "S":
                    nodes.add((x, y))
                    start = (x, y)
                if symbol == "E":
                    nodes.add((x, y))
                    end = (x, y)

    for x, y in nodes:
        graph[(x, y)] = set()
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            xy = x + d[0], y + d[1]
            if xy in nodes:
                graph[(x, y)].add(xy)

    return graph, start, end
  
def calc_node_costs(graph, start_node, end_node):
    heading_map = {start_node: (1, 0)}
    cost_map = {}
    frontier = deque()

    cost_map[start_node] = 0
    frontier.append(start_node) 
    
    while frontier:
        current_node = frontier.popleft()

        if current_node == end_node:
            continue

        for neighbour_node in graph[current_node]:
            new_heading = neighbour_node[0] - current_node[0], neighbour_node[1] - current_node[1]
            turns = calc_90deg_turns(heading_map[current_node], new_heading)
            new_cost = cost_map[current_node] + 1 + turns * 1000
            old_cost = cost_map.get(neighbour_node, math.inf)
            if new_cost < old_cost:
                heading_map[neighbour_node] = new_heading
                cost_map[neighbour_node] = new_cost
                frontier.append(neighbour_node)

    return cost_map

def find_shortest_path_nodes(cost_map, graph, end_node):
    frontier = deque()
    explored = set()

    frontier.append((end_node, cost_map[end_node], (1, 0)))
    frontier.append((end_node, cost_map[end_node], (-1, 0))) 
    frontier.append((end_node, cost_map[end_node], (0, 1))) 
    frontier.append((end_node, cost_map[end_node], (0, -1))) 
    explored.add(end_node)
    
    while frontier:
        current_node, current_cost, current_heading = frontier.popleft()
        explored.add(current_node)

        for neighbour_node in graph[current_node]:
            if neighbour_node in explored or neighbour_node not in cost_map:
                continue

            new_heading = neighbour_node[0] - current_node[0], neighbour_node[1] - current_node[1]
            turns = calc_90deg_turns(current_heading, new_heading)
            new_cost = current_cost - 1 - turns * 1000

            if new_cost == cost_map[neighbour_node] or new_cost == cost_map[neighbour_node] - 1000: 
                frontier.append((neighbour_node, new_cost, new_heading))

    return explored

def main():
    graph, start_node, end_node = build_node_graph("./day_16/input.txt")
    print("ORIGINAL GRAPH")
    visualize_graph(graph, graph)

    cost_map = calc_node_costs(graph, start_node, end_node)
    path_nodes = find_shortest_path_nodes(cost_map, graph, end_node)
    visualize_graph(graph, path_nodes)

    print(cost_map[end_node]) # Part 1 - 106512
    print(len(path_nodes)) # Part 2 - 563

if __name__ == "__main__":
    main()
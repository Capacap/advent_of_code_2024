import re
from copy import copy
from collections import deque


def parse_input(file_path):
    pattern = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
    results = []

    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")
        for line in lines:
            match = pattern.search(line)
            if match:
                p_x, p_y, v_x, v_y = map(int, match.groups())
                results.append((p_x, p_y, v_x, v_y))

    return results

class SimulationEntity:
    def __init__(self, pos, vel, id):
        self.pos_x: int = pos[0]
        self.pos_y: int = pos[1]
        self.vel_x: int = vel[0]
        self.vel_y: int = vel[1]
        self.id: int = id

class Simulation:
    def __init__(self):
        self.entities = []
        self.max_x = 0
        self.max_y = 0
        self.entity_clusters = []

    def add_entity(self, px, py, vx, vy):
        self.entities.append(SimulationEntity((px, py), (vx, vy), len(self.entities)))

    def step_simulation(self):
        self.move_entities()
        self.update_entity_clusters()

    def print(self):
        rows = [["-" for _ in range(self.max_x)] for _ in range(self.max_y)]

        for cluster in self.entity_clusters:
            symbol = str(min(len(cluster), 9))
            for entity in cluster:
                x = entity.pos_x
                y = entity.pos_y
                rows[y][x] = symbol

        for row in rows:
            print("".join(row))

    def move_entities(self):
        for entity in self.entities:
            entity.pos_x = (entity.pos_x + entity.vel_x) % self.max_x
            entity.pos_y = (entity.pos_y + entity.vel_y) % self.max_y

    def update_entity_clusters(self):
        pos_to_entities: dict[tuple, list[SimulationEntity]] = {}
        for entity in self.entities:
            xy = (entity.pos_x, entity.pos_y)
            if xy not in pos_to_entities:
                pos_to_entities[xy] = [entity]
            else:
                pos_to_entities[xy].append(entity)

        clusters: list[list[SimulationEntity]] = []
        forbidden: list[SimulationEntity] = []
        for entity in self.entities:
            if entity in forbidden:
                continue
            
            cluster = []
            frontier = deque([entity])
            while frontier:
                current = frontier.popleft()
                cluster.append(current)

                neighbours = []
                for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xy = (current.pos_x + d[0], current.pos_y + d[1])
                    neighbours.extend(pos_to_entities.get(xy, []))

                for neighbour in neighbours:
                    if neighbour == current:
                        continue

                    if neighbour in frontier:
                        continue

                    if neighbour in cluster:
                        continue

                    frontier.appendleft(neighbour)

            forbidden.extend(cluster)
            clusters.append(cluster)
        
        self.entity_clusters = clusters
        

def main():
    # Calculate the safety score of each quadrant after a 100 frames
    sim = Simulation()
    sim.max_x = 101
    sim.max_y = 103
    for input in parse_input("./day_14/input.txt"):
        px, py, vx, vy = input[0], input[1], input[2], input[3]
        sim.add_entity(px, py, vx, vy)

    for _ in range(100):
        sim.step_simulation()

    qx = 101 // 2
    qy = 103 // 2
    q0_n = 0
    q1_n = 0
    q2_n = 0
    q3_n = 0

    for e in sim.entities:
        x, y = e.pos_x, e.pos_y
        if x == qx or y == qy:
            continue
        if x < qx and y < qy:
            q0_n += 1
        elif x > qx and y < qy:
            q1_n += 1
        elif x < qx and y > qy:
            q2_n += 1
        elif x > qx and y > qy:
            q3_n += 1

    print(q0_n * q1_n * q2_n * q3_n) # Part 1 - 225648864

    # Search the first 10k frames for a large cluster of entities
    sim = Simulation()
    sim.max_x = 101
    sim.max_y = 103
    for input in parse_input("./day_14/input.txt"):
        px, py, vx, vy = input[0], input[1], input[2], input[3]
        sim.add_entity(px, py, vx, vy)

    max_cluster_size = 0
    max_cluster_size_frame = 0
    for i in range(10000):
        sim.step_simulation()

        frame_max_cluster_size = 0
        for c in sim.entity_clusters:
            frame_max_cluster_size = max(frame_max_cluster_size, len(c))

        if frame_max_cluster_size > max_cluster_size:
            max_cluster_size = frame_max_cluster_size
            max_cluster_size_frame = i + 1

    # Simulate until frame with largest cluster
    sim = Simulation()
    sim.max_x = 101
    sim.max_y = 103
    for input in parse_input("./day_14/input.txt"):
        px, py, vx, vy = input[0], input[1], input[2], input[3]
        sim.add_entity(px, py, vx, vy)

    for _ in range(max_cluster_size_frame):
        sim.step_simulation()

    sim.print() # Part 2 - 7847

    print(max_cluster_size_frame)


if __name__ == "__main__":
    main()
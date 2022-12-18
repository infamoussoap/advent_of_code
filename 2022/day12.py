import numpy as np

from utils.utils import readlines

FILENAME = 'data/day12.txt'


# Stolen from
# https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/
def BFS_SP(start, goal):
    explored = []

    queue = [[start]]

    if start == goal:
        return [start]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = node.neighbours

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return new_path
            explored.append(node)

    return []


class Node:
    def __init__(self, location, elevation_level):
        self.location = location
        self.elevation = elevation_level
        self.neighbours = []

    def add(self, node):
        if node not in self.neighbours:
            self.neighbours.append(node)

    def __repr__(self):
        return f"{self.location} : {self.elevation}"

    def __sub__(self, node):
        return self.elevation - node.elevation


class Start(Node):
    def __init__(self, location, elevation_level):
        super().__init__(location, elevation_level)


class End(Node):
    def __init__(self, location, elevation_level):
        super().__init__(location, elevation_level)


class Map:
    def __init__(self, elevation_levels):
        self.start, self.end, self.elevation_levels = self._parse_elevation_levels(elevation_levels)

        self._generate_graph()

    @staticmethod
    def _parse_elevation_levels(alpha_numeric_elevation_levels):
        n, m = alpha_numeric_elevation_levels.shape
        elevation_levels = np.zeros((n, m), dtype=object)

        for i in range(n):
            for j in range(m):
                val = alpha_numeric_elevation_levels[i, j]
                if val == 'S':
                    elevation_levels[i, j] = Start([i, j], -1)
                    start = elevation_levels[i, j]
                elif val == 'E':
                    elevation_levels[i, j] = End([i, j], ord('z') - ord('a'))
                    end = elevation_levels[i, j]
                else:
                    elevation_levels[i, j] = Node([i, j], ord(val) - ord('a'))

        return start, end, elevation_levels

    def _generate_graph(self):
        n, m = self.elevation_levels.shape

        for i in range(n):
            for j in range(m):
                current_node = self[i, j]
                new_positions = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]

                for new_i, new_j in new_positions:
                    if 0 <= new_i <= n - 1 and 0 <= new_j <= m - 1:
                        new_node = self[new_i, new_j]
                        if new_node.elevation <= current_node.elevation + 1:
                            current_node.add(new_node)

    def __getitem__(self, *args):
        return self.elevation_levels.__getitem__(*args)


def part1():
    lines = readlines(FILENAME)

    elevation_levels = np.array([[x for x in line.replace('\n', '')]
                             for line in lines])

    topography_map = Map(elevation_levels)

    start = topography_map.start
    end = topography_map.end

    path = BFS_SP(start, end)
    return len(path) - 1


def part2():
    lines = readlines(FILENAME)

    elevation_levels = np.array([[x for x in line.replace('\n', '')]
                                 for line in lines])

    topography_map = Map(elevation_levels)

    start = topography_map.start
    end = topography_map.end

    starting_positions = [x for x in topography_map.elevation_levels.flatten() if x.elevation == 1]

    paths = [len(BFS_SP(start, end)) for start in starting_positions]
    return sorted(paths)[0]


if __name__ == '__main__':
    print("Advent of Code 2022 Day 12")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

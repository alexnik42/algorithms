"""
solution(entrances, exits, path) takes an array of integers denoting where the entrances are, an array of integers denoting where the exits are located,
and an array of an array of integers of the corridors, returning the total capacity at each time step as an int.
"""

from collections import deque
from typing import List, Set
Vector = List[int]
Set = Set[int]


class Graph:
    def __init__(self, entrances: Vector, exits: Vector, paths: Vector) -> None:
        # Add single source and single target to paths size
        self.size = len(paths) + 2

        self.G = self.create_graph(set(entrances), set(exits), paths)

    def create_graph(self, entrances: Set, exits: Set, paths: Vector) -> Vector:
        G = [[]]

        # Append single source
        for node in range(self.size):
            G[0].append(float('inf') if node - 1 in entrances else 0)

        # Append middle nodes
        for node, row in enumerate(paths):
            G.append([0] + row + ([float('inf') if node in exits else 0]))

        # Append single target
        G.append([0 for _ in range(self.size)])

        return G

    def bfs(self, source: int, target: int, parent: Vector) -> bool:
        q = deque([source])
        visited = {source}

        while q:
            node = q.popleft()
            if node == target:
                return True
            for next_node, capacity in enumerate(self.G[node]):
                if next_node not in visited and capacity > 0:
                    visited.add(next_node)
                    parent[next_node] = node
                    q.append(next_node)

        return False

    def edmonds_karp(self, source: int, target: int) -> int:
        parent = [-1] * self.size
        total_capacity = 0

        while self.bfs(source, target, parent):
            current_capacity = float('inf')

            node = target
            while node != source:
                current_capacity = min(
                    current_capacity, self.G[parent[node]][node])
                node = parent[node]

            total_capacity += current_capacity

            node = target
            while node != source:
                self.G[parent[node]][node] -= current_capacity
                self.G[node][parent[node]] += current_capacity
                node = parent[node]

        return total_capacity


def solution(entrances: Vector, exits: Vector, paths: Vector) -> int:
    g = Graph(entrances, exits, paths)
    return g.edmonds_karp(0, g.size - 1)


if __name__ == '__main__':
    test1 = solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0],
                     [0, 0, 0, 8], [9, 0, 0, 0]])
    assert test1 == 6

    test2 = solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [
                     0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    assert test2 == 16

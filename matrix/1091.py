# 1091. Shortest Path in Binary Matrix

from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        if grid[0][0] == 1:
            return -1

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

        rows, cols = len(grid), len(grid[0])
        grid[0][0] = 1
        distance = [[0] * cols for _ in range(rows)]
        distance[0][0] = 1
        queue = deque()
        queue.append((0, 0))

        while queue:
            curr_x, curr_y = queue.popleft()
            for dir in directions:
                next_x, next_y = curr_x + dir[0], curr_y + dir[1]
                if 0 <= next_x < rows and 0 <= next_y < cols and grid[next_x][next_y] == 0:
                    grid[next_x][next_y] = 1    # 1 if visited
                    queue.append((next_x, next_y))
                    distance[next_x][next_y] = distance[curr_x][curr_y] + 1

        if distance[rows-1][cols-1] == 0:
            return -1
        else:
            return distance[rows-1][cols-1]
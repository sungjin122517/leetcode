from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        islands = 0

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            while queue:
                curr_i, curr_j = queue.popleft()
                # curr_i, curr_j = queue.pop() -> this will be dfs in iterative version
                if (curr_i, curr_j) not in visited:
                    visited.add((curr_i, curr_j))
                    for direction in directions:
                        next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                        if 0 <= next_i < rows and 0 <= next_j < cols and grid[next_i][next_j] == "1":
                            queue.append((next_i, next_j))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands




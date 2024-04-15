# BFS 미로 최단 거리 찾기

# 시작점부터 거리를 기록해놓는 2차원 리스트
# 왔던 길 다시 가지 않도록 visited 리스트를 사용

from collections import deque
from typing import List

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

def shortestPath(self, maze: List[List[str]]) -> int:
    rows, cols = len(maze), len(maze[0])
    maze[0][0] = 1
    distance = [[0] * cols for _ in range(rows)]
    queue = deque()
    queue.append((0, 0))

    while queue:
        curr_x, curr_y = queue.popleft()
        for dir in directions:
            next_x, next_y = curr_x + dir[0] + curr_y + dir[1]
            if 0 <= next_x < rows and 0 <= next_y < cols and maze[next_x][next_y] == 0:
                maze[next_x][next_y] = 1    # 1 if visited
                queue.append((next_x, next_y))
                distance[next_x][next_y] = distance[curr_x][curr_y] + 1

    if distance[rows-1][cols-1] == 0:
        return -1
    else:
        return distance[rows-1][cols-1]
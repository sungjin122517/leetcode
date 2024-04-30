# 2178. 미로: BFS

from collections import deque

rows, cols = map(int, input().split())
map = []
for i in range(rows):
    map.append(input())

directions = ((1, 0), (-1, 0), (0, -1), (0, 1))
visited = [[-1] * cols for _ in range(rows)]

q = deque()
q.append((0, 0))
visited[0][0] = 1
while q:
    curr_i, curr_j = q.popleft()
    for dir in directions:
        next_i, next_j = curr_i + dir[0], curr_j + dir[1]
        if 0 <= next_i < rows and 0 <= next_j < cols and visited[next_i][next_j] == -1 and map[next_i][next_j] == '1':
            q.append((next_i, next_j))
            visited[next_i][next_j] = visited[curr_i][curr_j] + 1

print(visited[rows-1][cols-1])
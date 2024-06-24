# 6593. 상범 빌딩: bfs

'''
배운점: index error를 방지하기 위해 x, y, z의 범위부터 확인하고, visited를 확인해야 한다.
'''

import sys
from collections import deque

def bfs():
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    queue = deque()
    queue.append([sz, sy, sx])
    
    while queue:
        cz, cy, cx = queue.popleft()
        if cx == ex and cy == ey and cz == ez:
            return "Escaped in {0} minute(s).".format(visited[cz][cy][cx])
        
        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nz = cz + dz[i]

            if 0 <= nx < col and 0 <= ny < row and 0 <= nz < level and visited[nz][ny][nx] == 0:
                if graph[nz][ny][nx] == "." or graph[nz][ny][nx] == "E":
                    visited[nz][ny][nx] = visited[cz][cy][cx] + 1
                    queue.append([nz, ny, nx])
    
    return "Trapped!"

# 여러개의 test case가 주어지므로 반복문 필요
while True:
    level, row, col = map(int, sys.stdin.readline().split())

    if level == 0 and row == 0 and col == 0:
        break

    graph = [[] * row for _ in range(level)]
    visited = [[[0 for _ in range(col)] for _ in range(row)] for _ in range(level)]

    for i in range(level):
        for _ in range(row):
            graph[i].append(list(map(str, sys.stdin.readline().strip())))
        sys.stdin.readline()
        
    # S, E 위치 확인
    for i in range(level):
        for j in range(row):
            for k in range(col):
                if graph[i][j][k] == "S":
                    sx, sy, sz = k, j, i
                elif graph[i][j][k] == "E":
                    ex, ey, ez = k, j, i

    print(bfs())

'''
if visited[nz][ny][nx] == 0 and 0 <= nx < col and 0 <= ny < row and 0 <= nz < level:

이렇게 하면, nz, ny, nz의 범위를 벗어나는 경우가 먼저 발생하여 index error가 발생할 수 있습니다.
'''
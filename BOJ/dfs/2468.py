# 2468. 안전 영역

import sys
sys.setrecursionlimit(10000)

level = int(input())
matrix = []
for _ in range(level):
    matrix.append(list(map(int, input().split())))
# visited = [[0]*level for _ in range(level)]
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
count = 0

# 물의 높이가 0일 때를 고려하여 1로 시작
answer = 1

def dfs(row, col, h):
    if visited[row][col]:
        return
    visited[row][col] = 1

    for dir in directions:
        nx, ny = row + dir[0], col + dir[1]
        if 0 <= nx < level and 0 <= ny < level and matrix[nx][ny] > h and not visited[nx][ny]:
            dfs(nx, ny, h)

for h in range(max(map(max, matrix)) + 1):
    visited = [[0]*level for _ in range(level)]
    count = 0
    for row in range(level):
        for col in range(level):
            if matrix[row][col] > h and not visited[row][col]:
                dfs(row, col, h)
                count += 1
    answer = max(answer, count)

print(answer)

# 10026. 적록색약: dfs

'''
1. R이랑 G를 구분해야하는데, dfs 한 번 돌려서 두가지 값을 다 구할 수 있나?
- 없다. G를 R로 변경하거나 조건문을 활용해서 서로 다른 dfs 함수를 두 번 구현해라.

배운점:
- python string is immutable
'''

import sys
sys.setrecursionlimit(10000)

num = int(input())
matrix = []
for i in range(num):
    matrix.append(list(input()))

# print(matrix)

ans1 = 0
ans2 = 0

visited = [[0]*num for _ in range(num)]
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

def dfs(i, j):
    if visited[i][j]:
        return
    
    visited[i][j] = 1
    for dir in directions:
        ni, nj = i + dir[0], j + dir[1]
        if 0 <= ni < num and 0 <= nj < num and matrix[i][j] == matrix[ni][nj]:
            dfs(ni, nj)

for i in range(num):
    for j in range(num):
        if not visited[i][j]:
            dfs(i, j)
            ans1 += 1

for i in range(num):
    for j in range(num):
        visited[i][j] = 0
        if matrix[i][j] == 'G':
            matrix[i][j] = 'R'

def dfs_blind(i, j):
    if visited[i][j]:
        return

    visited[i][j] = 1
    for dir in directions:
        ni, nj = i + dir[0], j + dir[1]
        if 0 <= ni < num and 0 <= nj < num and matrix[i][j] == matrix[ni][nj]:
            dfs_blind(ni, nj)

for i in range(num):
    for j in range(num):
        if not visited[i][j]:
            dfs_blind(i, j)
            ans2 += 1

print(ans1, ans2)


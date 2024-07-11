# 16234. 인구 이동: bfs

'''

'''

import sys
from collections import deque
input = sys.stdin.readline

n, left, right = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
    
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(row, col, visited):
    cnt = 1
    population = board[row][col]
    union = [(row, col)]
    
    queue = deque()
    queue.append((row, col))
    visited[row][col] = 1
    
    while queue:
        r, c = queue.popleft()
        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                diff = abs(board[r][c]-board[nr][nc])
                if left <= diff and diff <= right:
                    queue.append((nr, nc))
                    cnt += 1
                    population += board[nr][nc]
                    visited[nr][nc] = 1
                    union.append((nr, nc))
    
    # print(cnt)
    if cnt > 1:
        unionPop = population // cnt
        for i, j in union:
            board[i][j] = unionPop
        return True
    return False

ans = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    move_occured = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    move_occured = True
                    
    if not move_occured:
        break
    ans += 1

print(ans)
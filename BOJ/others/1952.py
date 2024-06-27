# 1952. 달팽이

'''
브론즈1

시계방향으로 꺾기
'''

import sys
input = sys.stdin.readline

row, col = map(int, input().split())
dir = [(0, 1), (1, 0), (0 ,-1), (-1, 0)] # 우하좌상 시계방향
visited = [[0 for _ in range(col)] for _ in range(row)]
idx = 0 # index to change direction
total = row * col
cnt = 0
r, c = 0, 0

for i in range(total):
    visited[r][c] = 1
    
    nr = r + dir[idx][0]
    nc = c + dir[idx][1]
    
    if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc]:
        r, c = nr, nc
    else:
        idx = (idx+1)%4
        r = r + dir[idx][0]
        c = c + dir[idx][1]
        cnt += 1
        
print(cnt-1)
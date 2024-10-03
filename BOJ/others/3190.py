# 3190. 뱀

'''
본인 몸 부딛혔을 때 어떻게 판단?
if element in deque
'''

import sys
from collections import deque

n = int(input())
k = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    ar, ac = r-1, c-1
    board[ar][ac] = 1
    
l = int(input())
snake_dir = {}
for _ in range(l):
    x, c = input().split()
    snake_dir[int(x)] = c
    
cnt = 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동남서북
idx = 0


queue = deque()
r, c = 0, 0

while True:
    queue.append((r, c))
    r += directions[idx][0]
    c += directions[idx][1]
    cnt += 1
    
    # 벽 부딛힘
    if r < 0 or r >= n or c < 0 or c >= n:
        break
    
    # 자기 자신 부딛힘
    if board[r][c] == 2:
        break
    
    # 사과 없을 때
    if board[r][c] == 0:
        i, j = queue.popleft()
        board[i][j] = 0
    
    board[r][c] = 2
    
    if cnt in snake_dir:
        if snake_dir[cnt] == 'D':
            idx = (idx + 1) % 4
        else:
            idx = (idx - 1) % 4
     
    
print(cnt)
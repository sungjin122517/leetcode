# 21610. 마법사 상어와 비바라기

'''
바구니에 물 저장
구름 계산이 복잡하네

pypy3 쓰면 시간 초과 안 남
'''

import sys

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

direction = [
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1)
]

cloud = [
    (n-1, 0),
    (n-1, 1),
    (n-2, 0),
    (n-2, 1)
]

lateral = [
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]

for _ in range(m):
    d, s = map(int, input().split())
    moved_cloud = []
    
    for y, x in cloud:
        ny = (y + direction[d-1][0] * s) % n
        nx = (x + direction[d-1][1] * s) % n
        board[ny][nx] += 1
        moved_cloud.append((ny, nx))
    
    for y, x in moved_cloud:
        cnt = 0
        for ly, lx in lateral:
            ny = y + ly
            nx = x + lx
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            elif board[ny][nx] > 0:
                cnt += 1
        board[y][x] += cnt
    
    new_cloud = []
    for y in range(n):
        for x in range(n):
            if (y, x) in moved_cloud or board[y][x] < 2:
                continue
            board[y][x] -= 2
            new_cloud.append((y, x))
    
    cloud = new_cloud

result = 0
for y in range(n):
    for x in range(n):
        result += board[y][x]
        
print(result)
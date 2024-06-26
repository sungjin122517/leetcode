# 14503. 로봇 청소기: 구현

'''
1. 현재 칸 청소
2. 주변 4칸 다 청소 되어있으면:
    a. 바라보는 방향 유지한 채로 한 칸 후진하고 1번으로 돌아가기
    b. 벽이여서 후진 못 하면 작동 멈춤
3. 청소되지 않은 빈 칸 있으면:
    a. 반시계 방향으로 90도 회전
    b. 앞쪽 칸이 청소되지 않았으면 전진
    c. 1번으로 돌아가기
'''

import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split()) # d = {0:북, 1:동, 2:남, 3:서}
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
room = []
for i in range(n):
    room.append(list(map(int, sys.stdin.readline().split())))

cnt = 0
while True:
    if room[r][c] == 0:
        cnt += 1
        room[r][c] = 2
        
    check = False    
    for i in range(4):
        d = (d+3)%4 # 반시계 방향으로 회전
        nr, nc = r + direction[d][0], c + direction[d][1]
        if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == 0:
            r, c = nr, nc
            check = True
            break
    
    if not check:   # 4방향 모두 청소되어 있거나 벽인 경우
        backDir = (d+2)%4
        br, bc = r + direction[backDir][0], c + direction[backDir][1]
        if 0 <= br < n and 0 <= bc < m and room[br][bc] != 1:
            r, c = br, bc
        else:
            break

print(cnt)
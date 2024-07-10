# 5427. 불: bfs (골드 4)

'''
bfs로 상근이 이동은 문제 없다.
여러개의 불은 어떻게 bfs 하나?
3d array로 불의 상태를 따로 관리?
b[w][h][0/1]
근데 여러개의 불은 어떡해?

- 2개의 bfs 구현
1. 먼저 불의 위치를 확인하고 불이 퍼지는 bfs 실행
2. 상근이의 bfs 실행
3. 불이 퍼진 시간을 기록해두고 상근이의 위치와 비교하여 가능 여부 판단

'''

import sys
input = sys.stdin.readline
from collections import deque

def bfs(f_s, queue, visit):
    while queue:
        ch, cw, time = queue.popleft()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dir in directions:
            nh, nw = ch + dir[0], cw + dir[1]
            if 0 <= nh < h and 0 <= nw < w:
                if b[nh][nw] == '.' or b[nh][nw] == '@':
                    if visit[nh][nw] > time + 1: # 불보다 사람이 더 빨리 도달할 수 있는 케이스를 찾음
                        visit[nh][nw] = time + 1
                        queue.append((nh, nw, visit[nh][nw]))
            elif f_s == 's':
                # print(visit)
                print(time + 1)
                return
    if f_s == 's':
        print("IMPOSSIBLE")

num = int(input())
for _ in range(num):
    w, h = map(int, input().split())
    b = []
    for _ in range(h):
        b.append(list(input().rstrip()))
    
    visit = [[1e9 for _ in range(w)] for _ in range(h)]
    # fire = [[0 for _ in range(w)] for _ in range(h)]
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
    ph, pw = 0, 0
    # posFire = []
    fqueue = deque()
    squeue = deque()

    for i in range(h):
        for j in range(w):
            if b[i][j] == '@':
                squeue.append((i, j, 0))
            elif b[i][j] == '*':
                fqueue.append((i, j, 0))
    
    bfs('f', fqueue, visit)
    print(visit)
    bfs('s', squeue, visit)
    print(visit)
    
    # queue = deque()
    # queue.append((ph, pw, 0))
    # visit[ph][pw] = 0
    
    # while queue:
    #     ch, cw, time = queue.popleft()
        
    #     # if ch == 0 or ch == h-1 or cw == 0 or cw == w-1:
    #     #     print(person[ch][cw])
    #     #     sys.exit()
            
    #     for d in directions:
    #         nh, nw = ch + d[0], cw + d[1]
    #         if 0 <= nh < h and 0 <= nw < w:
    #             if person[nh][nw] == 0 and b[nh][nw] == '.':
    #                 queue.append((nh, nw))
    #                 person[nh][nw] = person[ch][cw] + 1
    #         else:
    #             print('TIME')
    #             sys.exit()
    
    # print('IMPOSSIBLE')
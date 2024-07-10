# 2636. 치즈: 구현

'''
1. queue에 회색 넣는다 (r, c, time)
2. 둘러쌓인 부위는 (r, c, time+1) 해서 집어넣고, 녹는 부위는 새로운 큐에 넣는다 cqueue

2번이 틀렸다. 녹게 되는 테두리를 어떻게 찾냐?
- 정답: 외부 공기와 접촉한 치즈만을 녹이려면, 값이 0인 부분에 대해서만 bfs를 진행하면 된다!!!!

풀이:
결국 전체 판을 n시간에 거쳐서 탐색 해야한다.
예를 들어, 3시간만에 다 녹는다 치면 전체 판을 3번 탐색 -> bfs 총 3번
1. 판의 초기 상태에서 치즈의 갯수를 cnt에 저장한다.
2. bfs 함수로 녹인 치즈의 갯수(meltCnt)를 찾고, cnt에서 뺀다.
3. cnt가 0이 되면 탐색을 멈추고 시간과 meltCnt를 print
    마지막 meltCnt가 다 녹기 직전 남은 cnt 갯수
'''

import sys
input = sys.stdin.readline
from collections import deque

row, col = map(int, input().split())

# def isMelt(r, c):
#     directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
#     for d in directions:
#         nr, nc = r + d[0], c + d[1]
#         if board[nr][nc] == 0:
#             return True
#     return False

def bfs(): # 녹인 치즈 갯수 반환
    bqueue = deque()
    cqueue = deque()
    bqueue.append((0, 0))

    while bqueue:
        r, c = bqueue.popleft()
        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc]:
                visited[nr][nc] = 1
                if board[nr][nc] == 0:
                    bqueue.append((nr, nc))
                elif board[nr][nc] == 1:
                    cqueue.append((nr, nc))
    
    for r, c in cqueue:
        board[r][c] = 0
    return len(cqueue)

board = []
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
cnt = 0
# bqueue = deque()
# cqueue = deque()
for i in range(row):
    board.append(list(map(int, input().split())))
    cnt += sum(board[i])    # 전체 치즈 갯수 카운트?! 1 갯수만큼 더해준다고?
    # for j in range(col):
    #     if board[i][j] == 1:
    #         bqueue.append((i, j, 0))

time = 1
while True:
    visited = [[0 for _ in range(col)] for _ in range(row)]
    meltCnt = bfs()
    cnt -= meltCnt
    if cnt == 0:
        print(time, meltCnt)
        break
    time += 1

# while bqueue:
#     r, c, time = bqueue.popleft()
#     if isMelt(r, c):
#         cqueue.append((r, c))
#     else:
#         bqueue.append((r, c, time+1))
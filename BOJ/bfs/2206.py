# 2206. 벽 부수고 이동하기: bfs

'''
0: 이동가능, 1: 벽
(1, 1) -> (n, m) 최단경로 이동.
시작과 끝 점 카운트에 포함
벽 한 개까지 부실수 있음! backtracking?
근데 recursion이 아닌데 백트래킹 사용할 수 있나?

0번 세계: 벽을 부수지 않은 세계
1번 세계: 벽을 부순 세계
0->1 가능, 1->0 불가능

배운점:
- "벽을 부순적이 있는지에 대한 상태"도 queue에 함께 넣어서 문제를 풀어야한다.
- visited[x][y][벽부심여부=0/1]
'''

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input().strip())
    
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 벽 부수기 status 관리용 3차원 리스트
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1


while queue:
    x, y, isBroken = queue.popleft()

    if x == n-1 and y == m-1:
        print(visited[x][y][isBroken])
        sys.exit()
    
    for d in dir:
        nx = x + d[0]
        ny = y + d[1]
        # if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '0' and not visited[nx][ny]
        if 0 <= nx < n and 0 <= ny < m:
            # 벽 만났을 때
            if board[nx][ny] == '1' and not isBroken:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            # 벽이 아니고 방문하지 않은 경우
            elif board[nx][ny] == '0' and not visited[nx][ny][isBroken]:
                visited[nx][ny][isBroken] = visited[x][y][isBroken] + 1
                queue.append((nx, ny, isBroken))

print(-1)
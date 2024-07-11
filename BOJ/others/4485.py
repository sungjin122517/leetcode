# 4485. 녹색 옷 입은 애가 젤다지?: 다익스트라

'''
다익스트라 활용하여 minimum cost 찾기
예제들 찾아보니 다들 dictionary 형태의 그래프던데, n*m 형태의 그래프에서는 적용 어떻게 하냐?

bfs처럼 4개 방향 다 탐색하고, 간선 저장하는 2d list 따로 만들어서 비교해가며 구현하면 된다.
'''

import sys
import heapq
input = sys.stdin.readline

t = 1
while 1:
    n = int(input())
    if not n:
        break

    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    weight = [[float('inf') for _ in range(n)] for _ in range(n)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    queue = []
    heapq.heappush(queue, [board[0][0], 0, 0])
    weight[0][0] = board[0][0]

    while queue:
        dist, x, y = heapq.heappop(queue)
        
        if dist > weight[x][y]:
            continue
        
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < n:
                ndist = dist + board[nx][ny]
                if ndist < weight[nx][ny]:
                    weight[nx][ny] = ndist
                    heapq.heappush(queue, [ndist, nx, ny])

    print('Problem {}: {}'.format(t, weight[n-1][n-1]))

    t += 1
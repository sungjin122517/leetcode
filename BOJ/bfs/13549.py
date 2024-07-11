# 숨바꼭질 3

'''
가장 빠른 시간: bfs
directions = -1, +1, *2

관건: 가중치가 다름 (순간이동할 때는 0, 나머지는 1)
그러므로 다익스트라 이용

1. priority queue 사용
2. while priority queue empty, 비용 작은 순으로 pq에서 꺼낸다.

음 그냥 BFS 사용해도 된다.
근데 일반적인 dfs, bfs는 간선의 가중치가 모두 같아야한다.
그렇기 때문에 bfs를 사용하되, queue에서 꺼낸 노드가 목표 지점일 때, queue에 들어있는 모든 노드를 확인해서 empty 할 때까지 bfs 탐색을 종료해서는 안 됨.
'''

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0] * 100001
cnt = [0] * 100001
queue = deque()
queue.append(n)

while queue:
    pos = queue.popleft()
    if pos == k:
        print(cnt[pos])
        break
    
    for x, t in [(pos*2, 0), (pos-1, 1), (pos+1, 1)]:
        ntime = cnt[pos] + t
        if 0 <= x <= 100000 and visited[x] == 0:
            # print(npos, ntime)
            visited[x] = 1
            cnt[x] = ntime
            queue.append(x)

# print(visited[k])
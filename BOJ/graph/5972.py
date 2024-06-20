# 5972. 택배 배송: graph

'''
dijkstra
- use of priority queue: 지금까지 발견된 가장 짧은 거리의 노드에 대해서 먼저 계산할 수 있음
- dictionary 이용하여 graph 표현
    - 양방향으로 저장해줘라 그래프

'''

import heapq

n, m = map(int, input().split())
INF = float("inf") # 무한대 상수
graph = [[] for _ in range(n+1)]
distances = [INF for _ in range(n+1)]
for _ in range(m):
    start, end, dist = map(int, input().split())
    graph[start].append((end, dist))
    graph[end].append((start, dist))

def dijkstra(graph, start):
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        cur_d, cur_dest = heapq.heappop(queue)  # 탐색할 노드와 거리

        if cur_d > distances[cur_dest]: # 기존에 있는 거리보다 길다면 볼 필요도 없음
            continue

        for new_dest, new_d in graph[cur_dest]:
            dist = cur_d + new_d
            if dist < distances[new_dest]:
                distances[new_dest] = dist
                heapq.heappush(queue, [dist, new_dest])
    
    return distances

ans = dijkstra(graph, 1)
print(ans[n])



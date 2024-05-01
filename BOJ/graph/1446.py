# 1446. 지름길

# 그래프를 어떻게 그러야함?

'''
다익스트라 알고리즘: dp를 활용한 최단 경로 탐색 알고리즘
음의 간선을 포함할 수 없습니다.
'''

import heapq

n, dist = map(int, input().split())
distances = [float('inf')] * (dist+1)

# initialize graph
graph = [[] for _ in range(dist+1)]
for i in range(dist):
    graph[i].append((i+1, 1))

# 지름길로 graph 갱신
for i in range(n):
    start, end, d = map(int, input().split())
    if end > dist:
        continue
    graph[start].append((end, d))

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q) # dist는 여태까지의 거리
        # print('dist:', dist, 'now:', now)
        if dist > distances[now]:
            # print('dist > distances[now]', dist, distances[now])
            continue
        for node in graph[now]:
            cost = dist + node[1]
            # print('cost:', cost, 'distances[node[0]]:', distances[node[0]])
            if cost < distances[node[0]]: # 현재 거리가 end 값보다 더 작으면 지름길로 갱신
                distances[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
                # print('heappush')

dijkstra(0)
print(distances[dist])
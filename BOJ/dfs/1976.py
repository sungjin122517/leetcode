# 1976. 여행 가자

'''
graph + bfs?
dictionary로 카운트 할 생각 했는데, bfs 사용하면 다른 경로로 여러번 방문도 가능해서
안 된다.
그리고 bfs로 방문처리 하면, 그냥 특정 path와 상관없이 방문 가능한거여서 안 된다.

해답: graph + dfs
모든 지역이 연결되어 있는지를 확인하는 문제??
'''

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = {}
visited = [0 for _ in range(n+1)]
cnt = 0

for i in range(1, n+1):
    graph[i] = []
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            graph[i].append(j+1)

plan = list(map(int, input().split()))

def dfs(c):
    visited[c] = 1
    for g in graph[c]:
        if not visited[g]:
            dfs(g)

for p in plan:
    if not visited[p]:
        cnt += 1
        dfs(p)

if cnt == 1:
    print('YES')
else:
    print('NO')
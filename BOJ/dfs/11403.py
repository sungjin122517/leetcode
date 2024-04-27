# 11403. 경로 찾기: DFS Graph

import sys
sys.setrecursionlimit(10000)

num = int(input())

graph = {}
for i in range(num):
    graph[i] = []
    data = list(map(int, input().split()))
    # for loop of data with index
    for idx, d in enumerate(data):
        if d == 1:
            graph[i].append(idx)
    # print(graph[i])


ans = []
visited = [0 for _ in range(num)]

def dfs(node):    
    for n in graph[node]:
        # print(n)
        if visited[n] == 0:
            visited[n] = 1
            dfs(n)
            # ans.append((node, n)

for i in range(num):
    visited = [0 for _ in range(num)]
    dfs(i)
    for j in range(num):
        print(visited[j], end=' ')
    print()


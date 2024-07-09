# 9466. 텀 프로젝트: dfs (골드 3)

'''
1 -> 3
2 -> 1
3 -> 3
4 -> 7
5 -> 3
6 -> 4
7 -> 6

2 -> 1 -> 3 (X)
3 -> 3 (O)
6 -> 4 -> 7 -> 6 ... (O)

사이클이 이루어져야 한 팀
자기 자신을 선택해도 한 팀

output: 프로젝트 팀에 속하지 못한 학생들의 수

vertex = 7
edges = [[1, 3], [2, 1], ... , [7, 6]]
'''

import sys
input = sys.stdin.readline

num = int(input())
for _ in range(num):
    v = int(input())
    graph = list(map(int, input().split()))
    graph.insert(0, 0)
    visited = [0 for _ in range(v+1)]
    finished = [0 for _ in range(v+1)]
    
    global cnt
    cnt = v
    
    def dfs(node):
        global cnt
        visited[node] = 1
        cycleList.append(node)
        nxt = graph[node]
        # if not visited[v] and v == nxt:
        #     cnt += 1
        #     visited[v] = 1
        #     finished[v] = 1
        #     print(v, nxt)
        #     return
        if not visited[nxt]:
            dfs(nxt)
        elif not finished[nxt]:
            # print(cycleList)
            cnt -= len(cycleList[cycleList.index(nxt):]) # 혼자 팀을 이루는 사람 때문에 인덱스 사용해서 카운트
        finished[node] = 1
        
    for i in range(1, v+1):
        if not visited[i]:
            cycleList = []
            dfs(i)

    print(cnt)


# non-directed graph에서 사이클 찾기
'''
finised 대신 parent 개념 도입

1: [2]
2: [1, 3, 4]
3: [2, 4]
4: [2, 3]

1 -> 2 -> 3 -> 4 -> 2 (O)

dfs(node, parent)
dfs(1, 0)
    dfs(2, 1)
        dfs(3, 2)
            dfs(4, 3)
                dfs(2, 4) -> return
            return
        return
    return
'''

graph = [[], [2], [1, 3, 4], [2, 4], [2, 3]]
visited = [0 for _ in range(5)]

global isCycle
isCycle = False

def dfs(node, parent):
    global isCycle
    visited[node] = 1
    for v in graph[node]:
        if not visited[v]:
            dfs(v, node)
        elif v != parent:
            isCycle = True
# 2644. 촌수계산 (BFS)

'''
하나의 노드에 대해서 연결되어있는 여러개의 노드 list 유지

e.g. 1: [2, 3, 5]

bfs 코드가 간결하다

시작점부터 몇 번만에 도달하는지 세면서 촌수를 계산한다.

n 사이즈의 list를 유지.
'''

from collections import deque

numPerson = int(input())
p1, p2 = map(int, input().split())

numRelationship = int(input())

relationship = [[] for _ in range(numPerson+1)]

for i in range(numRelationship):
    parent, child = map(int, input().split())
    relationship[parent].append(child)
    relationship[child].append(parent)

count = [0] * (numPerson+1)

def bfs(node):
    queue = deque()
    queue.append(node)

    while queue:
        curr = queue.popleft()
        for c in relationship[curr]:
            if count[c] == 0:
                queue.append(c)
                count[c]  = count[curr] + 1

bfs(p1)

print(count[p2] if count[p2] > 0 else -1)


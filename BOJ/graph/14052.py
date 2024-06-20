# 14052. 연구소

'''
3개의 벽을 어떤 기준으로 세워야하는가?
백트래킹 찾아보기
'''

from collections import deque
import copy

row, col = map(int, input().split())
graph = []
for i in range(row):
    for j in range(col):
        graph.append(list(map(int, input().split())))

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

# spread virus via bfs
def bfs():
    queue = deque()
    # 원래의 그래프는 유지시킴 (deep copy)
    tmp_graph = copy.deepcopy(graph)

    # add virus position to queue
    for i in range(row):
        for j in range(col):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        cx, cy = queue.popleft()
        for dir in directions:
            nx, ny = cx + dir[0], cy + dir[1]
            if 0 <= nx < row and 0 <= ny < col and tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))

    global answer
    cnt = 0

    for i in range(row):
        cnt += tmp_graph[i].count(0)
    
    answer = max(answer, cnt)

# backtracking to build wall
def makeWall(cnt):
    # 벽 세 개가 세워지면 퍼트려본다
    if cnt == 3:
        bfs()
        return
    
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 0:
                graph[i][j] = 1 # 벽 세우고
                makeWall(cnt+1) # 다시 두 번째 벽 세우러 간다
                graph[i][j] = 0 # 다시 벽을 허문다 (backtracking)


answer = 0
makeWall(0)
print(answer)
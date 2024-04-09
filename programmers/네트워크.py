from collections import deque


def solution(n, computers):
    visited = [False]*n

    def bfs(computers, start, visited):
        queue = deque()
        queue.append(start)
        visited[start] = True
        while queue:
            v = queue.popleft()
            for i in range(len(computers[v])):
                if i == v:
                    continue
                if not visited[i] and computers[v][i] == 1:
                    queue.append(i)
                    visited[i] = True

    answer = 0

    for com in range(n):
        if not visited[com]:
            bfs(computers, com, visited)
            answer += 1

    return answer
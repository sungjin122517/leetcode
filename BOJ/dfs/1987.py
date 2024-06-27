# 1987. 알파벳: dfs

'''
주어진 조건에서, 최대 몇 칸 움직일 수 있는지 찾는 문제
분기별로 최장 거리를 찾아야 하므로, dfs로 풀이

배운점:
- input = sys.stdin.readline 사용하면 간편함.
- ord() 함수를 사용하여 문자를 아스키코드로 변환할 수 있음.
- strip() 함수를 사용하여 문자열 양쪽 공백 제거 가능 + split() 함수와 함께 사용 가능.
'''

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10000)

row, col = map(int, input().split())
board = []
# visited = [[0 for _ in range(col)] for _ in range(row)]
visited = [0 for _ in range(26)]
for i in range(row):
    board.append(list(input().strip()))
    
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
maxDist = 0

# cnt = 0
def dfs(r, c, cnt):

    global maxDist
    maxDist = max(maxDist, cnt)
    visited[ord(board[r][c]) - 65] = 1

    for d in dirs:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < row and 0 <= nc < col and not visited[ord(board[nr][nc]) - 65]:
            dfs(nr, nc, cnt+1)
            # 최장 거리를 비교해야 하기 때문에, 방문을 완료했을 때 최적인지 아닌지 모르므로 백트래킹하여 최적의 거리 검색.
            visited[ord(board[nr][nc]) - 65] = 0 # backtracking

dfs(0, 0, 1)
print(maxDist)
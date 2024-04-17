# 1012. 유기농 배추: DFS


import sys
sys.setrecursionlimit(10000)

n = int(input())

for i in range(n):
    cols, rows, num = map(int, input().split())
    field = [[0] * cols for _ in range(rows)]
    
    for j in range(num):
        col, row = map(int, input().split())
        field[row][col] = 1

    visited = set()
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def dfs(col, row):
        if (col, row) in visited:
            return
        visited.add((col, row))

        for dir in directions:
            next_col, next_row = col + dir[0], row + dir[1]
            if 0 <= next_col < cols and 0 <= next_row < rows and field[next_row][next_col] == 1:
                dfs(next_col, next_row)

    count = 0
    for col in range(cols):
        for row in range(rows):
            if field[row][col] == 1 and (col, row) not in visited:
                dfs(col, row)
                count += 1

    print(count)
    






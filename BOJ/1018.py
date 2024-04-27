# 1018. 체스판 다시 칠하기: Brute Force

# 칠할 부분을 찾는 시작점 찾기

chess = [ ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'] ]

n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(input())
ans = float('inf')

def count(x, y):
    # 체스 판과 비교해서 몇개나 다른지 세기
    cnt = 0
    for i in range(8):
        for j in range(8):
            if chess[i][j] != board[i+x][j+y]:
                cnt += 1

    # 좌상단이 W로 시작하거나 B로 시작하기 때문에, B로 시작하는 체스판일 경우에는 64-cnt
    return min(cnt, 64-cnt)

for i in range(n-8+1):
    for j in range(m-8+1):
        ans = min(ans, count(i, j))

print(ans)
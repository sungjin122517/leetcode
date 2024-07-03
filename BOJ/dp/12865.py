# 12865. 평범한 배낭: dp (골드5)

'''
1d? -> 시간초과 
2d? -> row: 배낭의 최대 허용 중량, col: i번째 아이템까지 살펴보았을 때

점화식?
dp[i][j] = 배낭의 최대 무게가 i이고, j번째 아이템까지 살펴봤을 때의 최대 가치
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 백트래킹: 시간초과
# dp = [0] * (k+1)
# for _ in range(n):
#     w, v = map(int, input().split())
#     dp[w] = v

# for i in range(1, k+1):
#     for j in range(1, i):
#         dp[i] = max(dp[i], dp[j] + dp[i-j])
        
# print(dp[k])

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
items = [[0, 0]]
for _ in range(n):
    w, v = map(int, input().split())
    items.append([w, v])

for i in range(1, k+1):
    for j in range(1, n+1):
        w, v = items[j][0], items[j][1]

        if i < w:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-w][j-1] + v)

print(dp[k][n])


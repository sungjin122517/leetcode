# 4811. 알약: dp

'''
N = 1000 -> O(n^3)

2d dp array
dp[w][h] = 큰 알약 w개와 작은 알약 h개를 먹을 수 있는 경우의 수
어떤 경우에서든 w >= h

점화식: dp[w][h] = dp[w-1][h] + dp[w][h-1]

https://kimtaehyun98.tistory.com/67
'''

import sys

while True:
    n = int(sys.stdin.readline())
    if n==0:
        break

    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for h in range(n+1):
        for w in range(n+1):
            if h > w:
                continue
            if h == 0:
                dp[w][h] = 1
                # print('dp[{}][{}] = {}'.format(w, h, dp[w][h]))
            else:
                dp[w][h] = dp[w-1][h] + dp[w][h-1]
                # print('dp[{}][{}] = {}'.format(w, h, dp[w][h]))


    print(dp[n][n])
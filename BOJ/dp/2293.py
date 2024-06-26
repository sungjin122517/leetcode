# 2293. 동전 1

'''
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.
'''

import sys

num, target = map(int, sys.stdin.readline().split())
coins = []
for _ in range(num):
    coins.append(int(sys.stdin.readline()))
coins.sort()

dp = [0]*(target+1)
dp[0] = 1

for i in range(num):
    for j in range(coins[i], target+1):
        dp[j] = dp[j] + dp[j - coins[i]]

print(dp[target])
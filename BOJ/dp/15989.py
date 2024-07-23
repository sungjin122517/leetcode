# 15989. 1, 2, 3 더하기 4

'''
https://velog.io/@dhelee/%EB%B0%B1%EC%A4%80-15989%EB%B2%88-123-%EB%8D%94%ED%95%98%EA%B8%B0-4-Python-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8DDP

1만 써서 합이 되는 경우는 모두 한 가지씩 가지고 있다. 때문에 dp 배열을 초기화할 때 1을 넣어놓는다.
우선 2가 추가되는 경우: dp[i] = dp[i] + dp[i-2]
3이 추가되는 경우: dp[i] = dp[i] + dp[i-3]
순서대로 갱신해주면 된다.

https://velog.io/@jkh9615/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-15989-1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0-4-Java
2차원 배열도 사용할 수 있다.
'''

import sys
input = sys.stdin.readline

cnt = int(input())

'''
# 겹치는 거 신경 안 쓸 때
for _ in range(cnt):
    n = int(input())
    dp = [0] * (n+1)
    
    for i in range(1, n+1):
        for j in range(1, 4):
            if i > j:
                dp[i] += dp[i-j]
            elif i == j:
                dp[i] += 1
                
    print(dp[n])
'''

for _ in range(cnt):
    n = int(input())
    dp = [1] * (n+1)

    for i in range(2, n+1):
        dp[i] += dp[i-2]
    
    for i in range(3, n+1):
        dp[i] += dp[i-3]
    
    print(dp[n])
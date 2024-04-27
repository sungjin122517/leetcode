# 1463. 1로 만들기: DP

num = int(input())

dp = [0] * (num+1)

for i in range(2, num+1):
    three = two = negOne = float('inf')
    if (i%3 == 0):
        three = 1 + dp[i//3]
    if (i%2 == 0):
        two = 1 + dp[i//2]
    negOne = 1 + dp[i-1]
    # get min among three, two, and negOne
    dp[i] = min(three, two, negOne)

print(dp[num])
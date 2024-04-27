# 제곱수의 합: dp

num = int(input())

# ans = [float('inf') for _ in range(num+1)]
# ans[1] = 1
# for i in range(2, num+1):
#     # check if i is square number
#     if int(i**0.5) == i**0.5:
#         ans[i] = 1
#         continue
    
#     for j in range(i-1, 0, -1):
#         ans[i] = min(ans[i], ans[j] + ans[i-j])

# print(ans[num])

# 결과: 시간 초과

def sum(num):
    dp = [0] * (num+1)
    for i in range(1, num+1):
        dp[i] = i
        if int(i**0.5) == i**0.5:
            dp[i] = 1
            continue

        for j in range(1, int(i**0.5)+1):
            dp[i] = min(dp[i], dp[i - j*j] + 1)
    
    return dp[num]

print(sum(num))
# 11052. 카드 구매하기

'''
카드 with 8가지 등급
카드팩 종류: 카드 1개 포함 카드팩, 카드 2개 포함 카드팩, ... , 카드 n개 포함 카드팩 총 n가지

돈 최대한 많이 지불해 카드 n개 구매하려고 한다.

output: 돈 최댓값
'''

n = int(input())
price = list(map(int, input().split()))
price.insert(0, 0)
dp = [0] * (n+1)

# dp[0] = price[0]
for i in range(1, n+1):
    for j in range(1, i+1):
        # print('i:', i, 'j:', j, 'dp[i]:', dp[i], 'price[j]:', price[j], 'dp[i-j]:', dp[i-j])
        dp[i] = max(dp[i], price[j] + dp[i-j])

print(dp[n])



# 2493. 탑: stack

'''
n: 500,000 -> O(n)

dp 인줄 알았지만 아니다.
stack 활용

본인보다 바로 앞이 아닌, 앞 전체를 확인해야했다. 그래서 dp가 아님.
본인보다 작은 element들은 더이상 비교할 필요가 없었기 때문에 stack에서 완전 제거할 수 있었다.
'''

import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
# tower.insert(0, 0)

# dp = [0] * (n+1)

# for i in range(2, n+1):
#     if tower[i-1] > tower[i]:
#         dp[i] = i-1
#     else:
#         dp[i] = dp[i-1]

# # check if every dp element is 0
# if not any(dp):
#     print(0)
# else:
#     print(*dp[1:])

# stack 활용
stack = []
ans = [0] * n

# (index, height)
stack.append((0, tower[0]))
for i in range(1, n):

    # 본인 앞이 본인보다 높은 탑 찾기 위해 계속 탐색
    while stack:
        if stack[-1][1] >= tower[i]:
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    
    stack.append((i, tower[i]))

print(*ans)
# 2631. 줄세우기

'''
숫자를 순서대로 배치하기 위해 옮겨야할 최소 횟수 찾기.
각 숫자의 위치 인덱스를 저장해서, 바로 다음 수가 자기보다 앞에 있으면 위치 변경.

e.g. 3 7 5 2 6 1 4
위치 변경해야할 숫자는 7, 2, 1, 4

n = 200 -> O(n^3)

해답: dp
가장 긴 증가하는 부분수열을 구해서 그 길이를 n에서 빼주면 된다.
'''

import sys

n = int(input())
# kid = [-1 for _ in range(n+1)]
# for i in range(1, n+1):
#     kid[int(input())] = i

num = []
for _ in range(n):
    num.append(int(input()))
    
dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j]+1)
        
ans = n - max(dp)
print(ans)
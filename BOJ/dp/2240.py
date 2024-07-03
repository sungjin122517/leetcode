# 2240. 자두나무: dp

'''
감이 아예 안 온다.
우선 그리디는 아니다. 반대편 나무에 자두가 떨어진다고 해서 곧장 달려가면 손해보는 상황이 생길수도 있다(예제처럼).

dp와 memoization.
무조건 점화식부터 생각해라.
현재 위치, 남은 이동 횟수, 현재 시간 = 자두 최대 개수
dp[pos][cnt][time] = value
'''

import sys
input = sys.stdin.readline

t, w = map(int, input().split())
arr = [int(input()) for _ in range(t)]

dp = [[[-1 for _ in range(t+1)] for _ in range(w+1)] for _ in range(3)]

# 초기 위치에서 자두가 떨어지는 첫 번째 경우
dp[1][0][0] = 0
if arr[0] == 1:
    dp[1][0][1] = 1
else:
    dp[2][1][1] = 1

for time in range(t):
    for cnt in range(w+1):
        for pos in range(1, 3):
            if dp[pos][cnt][time] >= 0:
                npos = arr[time + 1] if time + 1 < t else 0
                
                # 현재 위치에 자두가 떨어짐
                if pos == npos:
                    dp[pos][cnt][time+1] = dp[pos][cnt][time] + 1
                else:
                    # 움직여서 자두 받음
                    if cnt < w:
                        # 움직여서 받기 vs (?) 중에 더 큰 거 비교
                        dp[npos][cnt-1][time+1] = max(dp[npos][cnt-1][time+1], dp[pos][cnt][time] + 1)
                    # 안 움직임
                    dp[pos][cnt][time+1] = dp[pos][cnt][time]

max_plums = 0
for cnt in range(w+1):
    for pos in range(1, 3):
        max_plums = max(max_plums, dp[pos][cnt][t])
           
print(max_plums)
# 첫 번째 줄에 n과 k가 공백을 사이에 두고 주어진다.
# 다음 n개의 줄에는 집의 위치가 주어지는데, 이 중 i(1 ≤ i ≤ n)번째 줄에는 X_i와 Y_i가 공백을 사이에 두고 주어진다.
from itertools import combinations
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

n, k = map(int, input().split())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

# def calculateDistance(h1, h2):
#     # get absolute value of h1[0] - h2[0] and h1[1] - h2[1]
#     return abs(h1[0] - h2[0]) + abs(h1[1] - h2[1])

# 집과 대피소의 최대 거리 구하기
INF = float("INF")
def max_dist(combination):
    ans = 0
    for i in range(n):
        minDist = INF
        for comb in combination:
            dist = abs(x[i] - x[comb]) + abs(y[i] - y[comb])
            # i번째 집에서 가장 가까운 대피소의 거리
            minDist = min(minDist, dist)
        ans = max(ans, minDist)
    return ans

minmin = INF
for comb in combinations(range(n), k):
    minmin = min(minmin, max_dist(comb))

# 조합을 이용하여 n개의 집에서 k개의 대피소 정하기

print(minmin)

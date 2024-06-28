# 2559. 수열: two pointer

'''
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))
start = 0
end = start + k - 1
# total = 0
# for i in range(k):
#     total += temp[i]
total = sum(temp[:k])
maxTemp = total

while end < n-1:
    total -= temp[start]
    start += 1
    end += 1
    total += temp[end]
    
    maxTemp = max(maxTemp, total)

print(maxTemp)
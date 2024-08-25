# 1027. 고층 건물: brute force

import sys

n = int(input())
building = list(map(int, input().split()))

maxCnt = 0

for i in range(n):
    cnt = 0
    x1 = i+1
    
    # right
    maxGrad = None
    for r in range(i+1, n):
        x2 = r+1
        grad = (building[r]-building[i])/(x2-x1)
        if maxGrad is None or grad > maxGrad:
            maxGrad = grad
            cnt += 1
    
    # left
    minGrad = None
    for l in range(i-1, -1, -1):
        x2 = l+1
        grad = (building[l]-building[i])/(x2-x1)
        if minGrad is None or grad < minGrad:
            minGrad = grad
            cnt += 1
     
    if maxCnt < cnt:
        maxCnt = cnt
  
print(maxCnt)
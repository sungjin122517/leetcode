# 2531. 회전 초밥: sliding window

'''
답 안 보고 혼자 풀었다!!
'''

import sys

n, d, k, c = map(int, input().split())

sushi = []
for _ in range(n):
    sushi.append(int(input()))

start, end = 0, k-1

cnt = 0
num = [0 for _ in range(d+1)]
for i in range(k):
    num[sushi[i]] += 1
    if num[sushi[i]] == 1:
        cnt += 1
# coupon
num[c] += 1
if num[c] == 1:
    cnt += 1
        
maxCnt = cnt
while start < n:
    num[sushi[start]] -= 1
    if num[sushi[start]] == 0:
        cnt -= 1
    start += 1
    
    end += 1
    num[sushi[end % n]] += 1
    if num[sushi[end % n]] == 1:
        cnt += 1
    
    maxCnt = max(maxCnt, cnt)
 
print(maxCnt)
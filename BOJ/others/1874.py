# 1874. 스택 수열

'''
n=100,000 -> O(nlogn)

[4 3 6 8 7 5 2 1]
1 2 3 4 pop pop
1 2 5 6 pop
1 2 5 7 8 pop pop pop pop pop

[1 2 5 3 4]
1 pop
2 pop
3 4 5 pop
'''

import sys
from collections import deque
input = sys.stdin.readline

cnt = int(input())
arr = []
for _ in range(cnt):
    arr.append(int(input()))
idx = 0

queue = deque()
ans = []

for i in range(1, cnt+1):
    queue.append(i)
    ans.append('+')
    while queue and queue[-1] == arr[idx]:
        queue.pop()
        ans.append('-')
        idx += 1

    # print(queue)

if queue:
    print('NO')
else:
    for a in ans:
        print(a)
# 12851. 숨바꼭질 2: bfs

'''
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

---

queue: (n, k)
언제 순간이동 하고, 언제 +1 -1 하는지 내가 설계 해야하는가? NO
'''

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()
queue.append(n)
ways = [0]*100001
cnt, result = 0, 0

while queue:
    a = queue.popleft()
    tmpCnt = ways[a]
    if a == k:  # 둘이 만났을 때
        result = tmpCnt
        cnt += 1
        continue

    for i in [a+1, a-1, a*2]:
        if 0 <= i < 100001 and (ways[i] == 0 or ways[i] == ways[a]+1):
            ways[i] = ways[a] + 1
            queue.append(i)

print(result)
print(cnt)
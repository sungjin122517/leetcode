# 15686. 치킨 배달

'''
백트래킹
'''

import sys
# from collections import deque

n, m = map(int, input().split())

city = []
chicken = []
house = []
chickenIdx = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            house.append((i, j))
        elif temp[j] == 2:
            chicken.append((i, j))
    
    city.append(temp)

# direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def close(idx, cnt): # 요구사항이 m개인 만큼 치킨집을 폐업해보자
    global minDist

    print(chickenIdx, cnt)
    
    if idx > len(chicken):
        return
    if cnt == m:
        print('im here')
        totalDist = 0
        for r, c in house:
            dist = float('inf')
            for i in chickenIdx:
                rr, cc = chicken[i]
                dist = min(dist, abs(rr-r)+abs(cc-c))
            totalDist += dist
        minDist = min(minDist, totalDist)
        print(minDist)
        return
    
    chickenIdx.append(idx)
    close(idx+1, cnt+1)
    chickenIdx.pop()
    close(idx+1, cnt)
    

minDist = float('inf')
close(0, 0)
print(minDist)
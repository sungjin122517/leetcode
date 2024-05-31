# 11000. 강의실 배정: greedy interval

'''
minimum end time에 대한 기록을 계속 남겨둬야하기 때문에, 현재 진행중인 수업들 목록을 유지해야한다.
heap에는 end time만 집어 넣는다

배운점:
- greedy interval: use priority queue(heapq) to maintain min value and replace
'''

import heapq
import sys

num = int(input())
classes = []

for i in range(num):
    classes.append(list(map(int, sys.stdin.readline().split())))

# sort classes array by start time in ascending order
classes.sort(key=lambda x: x[0])

# last = minimum end time
# count, last = 1, classes[0][1]

# for i in range(1, num):
#     last = min(last, classes[i][1])
#     if classes[i][0] >= last:
#         continue
#     count += 1

# print(count)

heap = [classes[0][1]]

for i in range(1, num):
    if classes[i][0] < heap[0]:
        heapq.heappush(heap, classes[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, classes[i][1])

print(len(heap))
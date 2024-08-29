# 14891. 톱니바퀴

import collections

'''
first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))
fourth = list(map(int, input().split()))

start1, start2, start3, start4 = 0, 0, 0, 0

k = int(input())
for _ in range(k):
    num, direction = map(int, input().split())
    
    # rotate(direction)
    
def rotateFirst(d):
    if d == 1: # clockwise
        if start1 == 0:
            start1 = 7
        else:
            start1 -= 1
    else:
        start1 = (start1+1)%8

    if first[2] != second[6]:
'''

wheels = []
for _ in range(4):
    wheels.append(collections.deque(list(input())))

k = int(input())
rotate = [list(map(int, input().split())) for _ in range(k)]

def left(num, direction):
    if num < 0:
        return
    if wheels[num][2] != wheels[num+1][6]:
        left(num-1, -direction)
        wheels[num].rotate(direction)

def right(num, direction):
    if num > 3:
        return
    if wheels[num][6] != wheels[num-1][2]:
        right(num+1, -direction)
        wheels[num].rotate(direction)

for i in range(k):
    w = rotate[i][0] - 1
    d = rotate[i][1]
    left(w-1, -d)
    right(w+1, -d)
    wheels[w].rotate(d)

ans = 0

if wheels[0][0] == '1':
    ans += 1
if wheels[1][0] == '1':
    ans += 2
if wheels[2][0] == '1':
    ans += 4
if wheels[3][0] == '1':
    ans += 8

print(ans)
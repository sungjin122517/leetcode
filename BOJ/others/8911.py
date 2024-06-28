# 8911. 거북이: 구현, 시뮬레이션

'''
F: 한 눈금 앞으로
B: 한 눈금 뒤로
L: 왼쪽으로 90도 회전
R: 오른쪽으로 90도 회전

거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형의 넓이를 구하는 프로그램을 작성하시오.
단, 직사각형이 안 만들어지고 선분으로 이루어진 영역이라면 0을 반환해라.

좌상, 우하 max 구해서 넓이 구하기
단, 좌상 우하 중에 x나 y 좌표가 같으면 0 반환

E: (1, 0)
W: (-1, 0)
S: (0, -1)
N: (0, 1)

clockwise: NESW
anti-clockwise: NWSE

내 구현 방법은 너무 어렵게 됐다.
그냥 direction 변수 하나로 방향을 바꿀 수 있네.

북:0, 동:1, 남:2, 서:3 해서
오른쪽으로 회전하면 +1, 왼쪽으로 회전하면 -1 하면 된다.
'''

import sys
input = sys.stdin.readline

# front = {
#     'E': (1, 0),
#     'W': (-1, 0),
#     'S': (0, -1),
#     'N': (0, 1),
# }

# def right(direction):
#     switcher = {
#         'N': 'E',
#         'E': 'S',
#         'S': 'W',
#         'W': 'N'
#     }

#     return switcher.get(direction)

# def left(direction):
#     switcher = {
#         'N': 'W',
#         'W': 'S',
#         'S': 'E',
#         'E': 'N'
#     }

#     return switcher.get(direction)

front = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 북동남서

num = int(input())

for _ in range(num):
    direction = 0
    lx, ty = 0, 0
    rx, by = 0, 0
    x, y = 0, 0 

    path = input()
    
    for i in range(len(path)):
        p = path[i]
        if p == 'F':
            x, y = x + front[direction][0], y + front[direction][1]
        elif p == 'B':
            x, y = x - front[direction][0], y - front[direction][1]
        elif p == 'L':
            if direction == 0:
                direction = 3
            else:
                direction -= 1
        elif p == 'R':
            direction = (direction + 1) % 4

        # 얘네 매번 업데이트 하면서 runtime이 오래 걸린다.
        # 차라리 visited_x, visited_y 집합을 사용해서 좌표를 저장하고, 마지막에 한 번에 최소값과 최대값을 계산해라.
        lx, ty = min(lx, x), max(ty, y)
        rx, by = max(rx, x), min(by, y)

    width = rx - lx
    height = ty - by
    print(width * height)
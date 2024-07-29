# 7682. 틱택토: 구현

'''
count(x) < count(o): invalid

해답:
그냥 구현 문제였다. 내가 게임의 룰을 잘못 이해했다.
가로, 세로, 대각선이라는게 오목처럼의 모양이었다.
'''

import sys

# directions = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
# visited = [[0 for _ in range(3)] for _ in range(3)]

# def dfs(r, c, cnt):
#     global found
#     visited[r][c] = 1

#     for d in directions:
#         nr, nc = r + d[0], c + d[1]
#         if 0 <= nr < 3 and 0 <= nc < 3 and not visited[nr][nc] and board[r][c] == board[nr][nc]:
#             cnt += 1
#             if cnt == 3:
#                 print('valid')
#                 found = True
#                 return
#             dfs(nr, nc, cnt)

# while True:
#     found = False
#     visited = [[0 for _ in range(3)] for _ in range(3)]
    
#     ttt = input()
#     if ttt == 'end':
#         sys.exit()
    
#     if ttt.count('X') < ttt.count('O') or abs(ttt.count('X') - ttt.count('O') > 1):
#         print('invalid')
#         continue
    
#     board = []
#     board.append(ttt[:3])
#     board.append(ttt[3:6])
#     board.append(ttt[6:])
    
#     for i in range(3):
#         for j in range(3):
#             if not visited[i][j] and board[i][j] != '.':
#                 dfs(i, j, 1)
#                 if found:
#                     break
#         if found:
#             break
    
#     if not found:
#         print('invalid')

def checkX():
    for i in range(3):
        # 가로
        if board[i][0] == 'X':
            if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                return True
            
        # 세로
        if board[0][i] == 'X':
            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                return True
    
    if board[0][0] == 'X':
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return True

    if board[0][2] == 'X':
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return True
    
    return False

def checkO():
    for i in range(3):
        # 가로
        if board[i][0] == 'O':
            if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                return True
            
        # 세로
        if board[0][i] == 'O':
            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                return True
    
    if board[0][0] == 'O':
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return True

    if board[0][2] == 'O':
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return True
    
    return False


while True:
    ttt = input()
    if ttt == 'end':
        sys.exit()

    board = []
    board.append(ttt[:3])
    board.append(ttt[3:6])
    board.append(ttt[6:])

    x = checkX()
    o = checkO()

    if x and not o and ttt.count('X') == ttt.count('O') + 1:
        print('valid') # x가 이긴 경우
    elif not x and o and ttt.count('X') == ttt.count('O'):
        print('valid') # o가 이긴 경우
    elif not x and not o and ttt.count('X') == 5 and ttt.count('O') == 4:
        print('valid') # 비긴 경우
    else:
        print('invalid')





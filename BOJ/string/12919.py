# 12919. A와 B 2

'''
두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다. 문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.
1. 문자열의 뒤에 A를 추가한다.
2. 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.

greedy가 아니여서 뭔가 dp인거 같은데..

해답:
T에서 조건에 맞게 문자를 제거하여 S로 만드는 방식 -> 거꾸로 생각하기?
'''

import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

def dfs(t):
    if S == t:
        print(1)
        sys.exit()
    
    if len(t) == 0:
        return 0
    
    if t[0] == 'B':
        dfs(t[1:][::-1])

    if t[-1] == 'A':
        dfs(t[:-1]) # 마지막 제거
        
dfs(T)
print(0)

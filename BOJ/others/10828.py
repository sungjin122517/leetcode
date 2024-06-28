# 10828. 스택

'''
실버4

정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

배운점:
- sys.stdin.readline() 은 입력을 받을 때 줄바꿈 문자를 포함하기 때문에 strip()을 사용해야 한다.
- Stack이라는 클래스를 만들어서 구현할 수도 있다.
'''

import sys
input = sys.stdin.readline
from collections import deque

queue = deque()

def stack(cmd):
    # print(cmd)
    # print(len(cmd))

    if cmd == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.pop())
    
    elif cmd == 'size':
        print(len(queue))
    
    elif cmd == 'empty':
        print(1) if not queue else print(0)
    
    elif cmd == 'top':
        print(-1) if not queue else print(queue[-1])
    
    else:
        lst = list(cmd.split(' '))
        num = int(lst[1])
        queue.append(num)

cnt = int(input())
for _ in range(cnt):
    stack(input().strip())


# class stack 만들기
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, num):
        self.stack.append(num)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        return 0 if self.stack else 1
    
    def top(self):
        return self.stack[-1] if self.stack else -1
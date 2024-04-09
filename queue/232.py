from collections import deque


class MyQueue:

    def __init__(self):
        self.stack = deque()
        self.temp = deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        # while len(self.stack) > 1:
        #     self.temp.append(self.stack.pop())
        # result = self.stack.pop()
        # while len(self.temp) > 0:
        #     self.stack.append(self.temp.pop())
        
        # return result

        if not self.temp:
            while self.stack:
                self.temp.append(self.stack.pop())
        
        return self.temp.pop()

        

    def peek(self) -> int:
        # while len(self.stack) > 1:
        #     self.temp.append(self.stack.pop())
        # result = self.stack.pop()
        # self.temp.append(result)
        # while len(self.temp) > 0:
        #     self.stack.append(self.temp.pop())
        
        # return result
        if not self.temp:
            while self.stack:
                self.temp.append(self.stack.pop())

        return self.temp[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.temp) == 0
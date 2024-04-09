# 622. Design circular queue

class ListNode:
    def __init__(self, val, next, prev):
        self.val, self.next, self.prev = val, next, prev

class MyCircularQueue:
    # intuitive to use linked list
    # array: need to set the size

    def __init__(self, k: int):
        # left and right are dummy nodes
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right
        

    def enQueue(self, value: int) -> bool:
        if self.space == 0:
            return False
        
        add = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = add
        self.right.prev = add
        self.space -= 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val
        

    def isEmpty(self) -> bool:
        return self.left.next == self.right
        

    def isFull(self) -> bool:
        return self.space == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
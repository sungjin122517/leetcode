# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if head.next == None:
        #     return None
        
        # countPtr, ptr1 = head, head
        # count = 1
        # while countPtr.next:
        #     countPtr = countPtr.next
        #     count += 1
        # for i in range(1, count-n):
        #     ptr1 =  ptr1.next
        # deletePtr = ptr1.next
        # ptr1.next = deletePtr.next
        # deletePtr.next = None

        # return head

        # make gap between two pointers to n
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next



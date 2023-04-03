# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print(l1.next.val)

solve = Solution()

l1 = ListNode(val=2)
l2 = ListNode(val=3)
l3 = ListNode(val=4)
l4 = ListNode(val=5)
l5 = ListNode(val=6)

l1.next = l4
l4.next = l3
l4.next = l5
l5.next = l3

solve.addTwoNumbers(l1, l2)
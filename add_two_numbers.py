# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbersOpt(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            current.next = ListNode(val)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        aux1 = l1
        aux2 = l2
        
        string1 = ''
        string2 = ''

        while aux1 != None:
            string1 += str(aux1.val)
            aux1 = aux1.next

        while aux2 != None:
            string2 += str(aux2.val)
            aux2 = aux2.next

        print(string1, string2)

        result = int(string1) + int(string2)

        print(result)

        newNode = ListNode(val=str(result)[len(str(result))-1])
        print('vla: ', newNode.val)

        aux3 = newNode
        list = []

        for i in range(len(str(result))-2, -1, -1):
            node = ListNode()
            node.val = str(result)[i]
            aux3.next = node
            aux3 = node
            list.append(int(str(result)[i]))


        self.printLinkedList(newNode)

        return newNode


    def printLinkedList(self, sll: Optional[ListNode]) -> str:
        aux = sll
        print(aux.val)
        while aux.next != None:
            aux = aux.next
            print(aux.val)

solve = Solution()

l1 = ListNode(val=2)
l2 = ListNode(val=3)
l3 = ListNode(val=4)
l33 = ListNode(val=4)
l4 = ListNode(val=5)
l5 = ListNode(val=6)



l1.next = l3
l3.next = l2

l4.next = l5
l5.next = l33

test = solve.addTwoNumbersOpt(l1, l4)
print(test)
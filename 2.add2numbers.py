# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        l3 = ListNode(0)
        temp = l3
        totalSum = 0
        
        while l1 or l2 or carry:
            if l1:
                totalSum += l1.val
                l1 = l1.next
            if l2:
                totalSum += l2.val
                l2 = l2.next
            totalSum += carry
            carry = totalSum // 10
            temp.next = ListNode(totalSum % 10)
            totalSum = 0
            temp = temp.next
        return l3.next
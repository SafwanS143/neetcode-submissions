# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carryOver = 0
        newHead = None
        prev = None

        while curr1 or curr2 or carryOver != 0:
            sum = carryOver

            if curr1: 
                sum += curr1.val
                curr1 = curr1.next
            
            if curr2:
                sum += curr2.val
                curr2 = curr2.next
            
            if len(str(sum)) > 1:
                nodeVal = int(str(sum)[-1])
                carryOver = int(str(sum)[:-1])
            
            else:
                nodeVal = sum
                carryOver = 0

            
            currNode = ListNode(nodeVal)
            if newHead is None: newHead = currNode
            if prev: prev.next = currNode
            prev = currNode

        return newHead


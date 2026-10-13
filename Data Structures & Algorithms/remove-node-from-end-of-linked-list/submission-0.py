# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        lengthList = 0
        while curr:
            lengthList += 1
            curr = curr.next

        curr = head
        newHead = head
        for i in range(lengthList - n - 1):
            curr = curr.next

        if lengthList - n == 0: newHead = newHead.next
        curr.next = curr.next.next if curr.next else None

        return newHead
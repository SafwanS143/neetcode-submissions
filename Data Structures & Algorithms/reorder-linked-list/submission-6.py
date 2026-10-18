# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None: return None
        start = end = head
        stack = []

        while end is not None:
            stack.append(end)
            end = end.next
        end = stack.pop()

        for i in range(len(stack)):
            if i % 2 == 0:
                temp = start.next
                start.next = end
                start = temp
            
            else:
                end.next = start
                end = stack.pop()

        start.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return 
        
        start = None

        def reverse(node, prev):
            nonlocal start

            if node.next is None:
                node.next = prev
                start = node
                return

            reverse(node.next, node)

            node.next = prev

        reverse(head, None)
        return start

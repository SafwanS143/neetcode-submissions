# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        
        fast = head.next
        slow = head
        
        while fast and slow and fast != slow:
            fast = fast.next.next if fast.next else None
            slow = slow.next


        if slow == fast:
            return True
        
        else:
            return False
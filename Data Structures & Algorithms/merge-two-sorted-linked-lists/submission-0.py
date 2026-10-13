# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0, None)
        curr = head

        def pushNext(curr, listNode):
            temp = listNode.next
            curr.next = listNode

            curr = curr.next
            listNode = temp

            return curr, listNode

        while list1 and list2:
            if list1.val <= list2.val:
                curr, list1 = pushNext(curr, list1)

            else:
                curr, list2 = pushNext(curr, list2)
        
        while list1:
            curr, list1 = pushNext(curr, list1)
        while list2:
            curr, list2 = pushNext(curr, list2)

        return head.next
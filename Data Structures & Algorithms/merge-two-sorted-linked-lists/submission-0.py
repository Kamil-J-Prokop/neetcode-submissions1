# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy
        l1_current = list1
        l2_current = list2

        while l1_current is not None and l2_current is not None:
            if l1_current.val < l2_current.val:
                tail.next = l1_current
                l1_current = l1_current.next
            else:
                tail.next = l2_current
                l2_current = l2_current.next
            
            tail = tail.next
        
        if l1_current is not None:
            tail.next = l1_current
        else:
            tail.next = l2_current

        return dummy.next
        
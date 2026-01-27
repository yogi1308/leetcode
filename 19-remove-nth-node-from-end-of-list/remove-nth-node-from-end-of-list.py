# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = dummy = ListNode(0, head)
        r = head
        gap = 0
        while r:
            if gap >= n:
                l = l.next
            r = r.next
            gap += 1
        l.next = l.next.next
        return dummy.next

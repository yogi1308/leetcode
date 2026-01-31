# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = r = head
        lcurr = rcurr = 1
        lpos, rpos = left, right
        while True:
            if lcurr != lpos:
                l = l.next
                lcurr += 1
            if rcurr != rpos:
                r = r.next
                rcurr += 1
            if lcurr == lpos and rcurr == rpos:
                temp = l.val
                l.val = r.val
                r.val = temp

                l = l.next
                lcurr += 1
                lpos += 1
                
                r = head
                rcurr = 1
                rpos -= 1
            if lpos >= rpos: break
        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l1 = []
        curr = head 
        counter = 0
        new_head = dummy = ListNode(0)
        while curr:
            l1.insert(0, curr)
            counter += 1
            curr = curr.next
            if counter == k:
                counter = 0
                dummy.next, l1_tail = self.reverse(l1)
                dummy = l1_tail
        if len(l1) > 0:
            dummy.next = l1.pop(-1)

        return new_head.next




    
    def reverse(self, nodes):
        new_head = nodes.pop(0)
        curr = new_head
        for i in range(len(nodes)):
            curr.next = nodes.pop(0)
            curr = curr.next
        tail = curr
        curr.next = None
        return new_head, tail


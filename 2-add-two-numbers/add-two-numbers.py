# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr, l2_curr = l1, l2
        dummy = curr = ListNode(0)
        carry = 0
        while l1_curr or l2_curr:
            sum_val =  carry
            if l1_curr: 
                sum_val += l1_curr.val
                l1_curr = l1_curr.next
            if l2_curr: 
                sum_val += l2_curr.val
                l2_curr = l2_curr.next
            if sum_val >= 10:
                carry = 1    
            curr.next = ListNode(sum_val % 10)
            curr = curr.next
            if sum_val < 10: carry = 0
        if carry != 0: curr.next = ListNode(carry)
        return dummy.next
            

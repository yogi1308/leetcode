# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printList(self, head):
        curr = head
        while curr:
            print(curr.val, end=", ")
            curr = curr.next
        print("\n")
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        
        list2 = None
        mid = length // 2 if length % 2 == 0 else (length // 2) + 1
        curr = head
        curr_pos = 1
        while curr_pos < mid:
            curr = curr.next
            curr_pos += 1

        list2 = curr.next
        curr.next = None

        curr2 = list2
        prev = None
        while curr2:
            temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = temp
        list2 = prev

        curr = head
        curr2 = list2
        while curr2 and curr:
            temp = curr.next
            temp2 = curr2.next
            curr.next = curr2
            curr2.next = temp
            curr = temp
            curr2 = temp2
        
        self.printList(curr)
        


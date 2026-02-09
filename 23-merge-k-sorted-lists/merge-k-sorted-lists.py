# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        arr = []
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                arr.append(curr.val)
                curr = curr.next
        arr = sorted(arr)
        curr = dummy
        for i in range(len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next
        return dummy.next



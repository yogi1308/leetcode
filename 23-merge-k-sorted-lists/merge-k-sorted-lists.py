# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        hash_map = {}
        for i in range(len(lists)):
            if lists[i] is not None:
                hash_map[i] = lists[i]
        while len(hash_map) > 0:
            min_arr = []
            for vals in hash_map:
                min_arr.append(hash_map[vals].val)
            min_val = min(min_arr)
            new_node = ListNode(min_val)
            curr.next = new_node
            curr = curr.next
            for vals in hash_map:
                if hash_map[vals].val == min_val:
                    hash_map[vals] = hash_map[vals].next
                    if hash_map[vals] is None: hash_map.pop(vals)
                    break
        return dummy.next



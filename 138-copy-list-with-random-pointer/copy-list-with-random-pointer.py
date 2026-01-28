"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copies = {}
        curr = head
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copies[curr].next = None if curr.next is None else copies[curr.next]
            copies[curr].random = None if curr.random is None else copies[curr.random]
            curr = curr.next
        return copies[head]
        
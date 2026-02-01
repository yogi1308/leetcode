class ListNode:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self, length = 10000):
        self.set = [ListNode(0) for i in range(length)]
        self.length = length
        

    def add(self, key: int) -> None:
        idx = key % self.length
        curr = self.set[idx]
        while curr.next:
            if curr.next.val == key: return 
            curr = curr.next
        curr.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        idx = key % self.length
        curr = self.set[idx]
        while curr.next:
            if curr.next.val == key: 
                curr.next = curr.next.next
                return
            curr = curr.next
        

    def contains(self, key: int) -> bool:
        idx = key % self.length
        curr = self.set[idx]
        while curr.next:
            if curr.next.val == key: 
                return True
            curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
class ListNode:
    def __init__(self, key, value, prev = None, next = None) -> None:
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        #left = lru, right = mru
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = node
        node.next = next
        node.prev = prev
        next.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        else:
            if len(self.cache) == self.cap:
                lru = self.left.next
                self.cache.pop(lru.key)
                self.remove(lru)
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
            




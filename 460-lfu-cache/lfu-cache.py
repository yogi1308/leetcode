class Node:
    def __init__(self, key, value, freq = 1, next = None, prev = None):
        self.key = key
        self.val = value
        self.freq = freq
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self) -> None:
        self.left = self.right = Node(None, None)
        self.left.next, self.right.prev = self.right, self.left
        self.size = 0

    def __str__(self) -> str:
        return_str = ""
        curr = self.left.next
        while curr:
            return_str += f"({curr.key}, {curr.value})"
            curr = curr.next
        return return_str

    def remove(self, node):
        next, prev = node.next, node.prev
        prev.next, next.prev = next, prev
        self.size -= 1
    
    def removeLRU(self):
        lru = self.left.next
        new_connection = self.left.next.next
        self.left.next = new_connection
        new_connection.prev = self.left
        self.size -= 1
        return lru


    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next
        self.size += 1

class LFUCache:

    def __init__(self, capacity: int):
        self.cache_freq = {}
        self.cache_keys = {}
        self.cap = capacity
        
    def get(self, key: int) -> int:
        if key in self.cache_keys:
            node = self.cache_keys[key]
            curr_list = self.cache_freq[node.freq]
            curr_list.remove(node)
            if curr_list.size == 0: self.cache_freq.pop(node.freq)
            node.freq += 1
            if node.freq in self.cache_freq:
                self.cache_freq[node.freq].insert(node)
                return node.val
            else:
                self.cache_freq[node.freq] = LinkedList()
                self.cache_freq[node.freq].insert(node)
                return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_keys:
            node = self.cache_keys[key]
            curr_list = self.cache_freq[node.freq]
            curr_list.remove(node)
            if curr_list.size == 0: self.cache_freq.pop(node.freq)
            node.freq += 1
            node.val = value
            if node.freq in self.cache_freq:
                self.cache_freq[node.freq].insert(node)
                return
            else:
                self.cache_freq[node.freq] = LinkedList()
                self.cache_freq[node.freq].insert(node)
                return
        
        else:
            node = Node(key, value)
            if len(self.cache_keys) == self.cap:
                min_freq = min(self.cache_freq)
                lru = self.cache_freq[min_freq].removeLRU()
                if self.cache_freq[min_freq].size == 0: self.cache_freq.pop(min_freq)
                self.cache_keys.pop(lru.key)
            if 1  not in self.cache_freq:
                self.cache_freq[1] = LinkedList()
            self.cache_freq[1].insert(node)
            self.cache_keys[key] = node
        return

    


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
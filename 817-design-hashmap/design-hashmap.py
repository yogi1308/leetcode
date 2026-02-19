class MyHashMap:

    def __init__(self):
        self.data = [-1] * 1000000
        

    def put(self, key: int, value: int) -> None:
        idx = key % 1000000
        self.data[idx] = value
        
    def get(self, key: int) -> int:
        idx = key % 1000000
        return self.data[idx]
        
    def remove(self, key: int) -> None:
        idx = key % 1000000
        self.data[idx] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
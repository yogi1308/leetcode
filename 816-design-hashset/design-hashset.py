class MyHashSet:

    def __init__(self):
        self.vals = []
        

    def add(self, key: int) -> None:
        if key not in self.vals: self.vals.append(key)
        

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.vals.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.vals else False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
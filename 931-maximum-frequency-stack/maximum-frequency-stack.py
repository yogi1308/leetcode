class FreqStack:

    def __init__(self):
        self.vals = []
        self.count_group = {}
        max_count = 0
        

    def push(self, val: int) -> None:
        self.vals.append(val)
        val_count = self.vals.count(val)
        if val_count in self.count_group:
            self.count_group[val_count].append(val)
        else:
            self.count_group[val_count] = [val]
            self.max_count = val_count


        
    def pop(self) -> int:
        popped_value = self.count_group[self.max_count].pop()
        if len(self.count_group[self.max_count]) == 0: 
            self.count_group.pop(self.max_count)
            self.max_count -= 1
        for i in range(len(self.vals) - 1, -1, -1):
            if self.vals[i] == popped_value:
                self.vals.pop(i)
                break
        return popped_value
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
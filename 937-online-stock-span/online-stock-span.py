class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        count = 1
        curr = -1
        while True:
            if not self.stack or abs(curr) > len(self.stack) or price < self.stack[curr][0]:
                self.stack.append((price, count))
                return count
            else:
                count += self.stack[curr][1]
                curr -= self.stack[curr][1]
            

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
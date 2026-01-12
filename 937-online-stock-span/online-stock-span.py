class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        curr = -1
        while True:
            if not self.stack or abs(curr) > len(self.stack) or price < self.stack[curr][0]:
                self.stack.append((price, abs(curr)))
                return abs(curr)
            else:
                curr -= self.stack[curr][1]
            

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        curr = 1
        while self.stack and self.stack[-1][0] <= price:
            curr += self.stack[-1][1]
            self.stack.pop()
            
        self.stack.append((price, abs(curr)))
        return abs(curr)

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
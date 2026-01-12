class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        curr = -1
        while self.stack and abs(curr) <= len(self.stack) and price >= self.stack[curr][0]:
            curr -= self.stack[curr][1]
            
        self.stack.append((price, abs(curr)))
        return abs(curr)

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
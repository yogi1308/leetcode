class ListNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    

class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.head = None
        self.curr_size = 0
        

    def enQueue(self, value: int) -> bool:
        if self.curr_size < self.size:
            new_head = ListNode(value, self.head)
            self.head = new_head
            self.curr_size += 1
            return True
        else: return False
        

    def deQueue(self) -> bool:
        if not self.head: return False
        if self.curr_size == 1:
            self.head = None
            self.curr_size -= 1
            return True
        
        prev = curr = self.head
        while curr.next:
            prev = curr
            curr = curr.next
        prev.next = None
        self.curr_size -= 1
        return True

    def Front(self) -> int:
        if not self.head: return -1
        prev = curr = self.head
        while curr:
            prev = curr
            curr = curr.next
        return prev.val


    def Rear(self) -> int:
        return self.head.val if self.head else -1

    def isEmpty(self) -> bool:
        return True if self.curr_size == 0 else False
        

    def isFull(self) -> bool:
        return False if self.curr_size < self.size else True
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
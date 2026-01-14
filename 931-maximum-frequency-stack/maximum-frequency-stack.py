class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.stacks = [[]]

    def push(self, val: int) -> None:
        valCnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valCnt
        if valCnt == len(self.stacks):
            self.stacks.append([])
        self.stacks[valCnt].append(val)

    def pop(self) -> int:
        res = self.stacks[-1].pop()
        self.cnt[res] -= 1
        if not self.stacks[-1]:
            self.stacks.pop()
        return res
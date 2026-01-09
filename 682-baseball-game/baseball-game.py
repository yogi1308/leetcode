class Solution:
    def calPoints(self, operations: List[str]) -> int:
        recordStack = []
        for score in operations:
            if score.isnumeric():
                recordStack.append(int(score))
            elif "-" in score:
                recordStack.append(int(score))
            elif recordStack and score == "+":
                recordStack.append(recordStack[-1] + recordStack[-2])
            elif recordStack and score == "D":
                recordStack.append(recordStack[-1] * 2)
            elif recordStack and score == "C":
                recordStack.pop()

        return sum(recordStack)
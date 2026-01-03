class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 3: return int(tokens[0])
        stack = []
        for num in tokens:
            if num == "+": stack.append(int(stack.pop()) + int(stack.pop()))
            elif num == "-": 
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b - a)
            elif num == "*": stack.append(int(stack.pop()) * int(stack.pop()))
            elif num == "/": 
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(int(b / a))
            else: stack.append(int(num))
        return stack[0]
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i].isalnum() or s[i] == '[':
                if stack and s[i].isnumeric() and stack[-1].isnumeric():
                    stack[-1] += s[i]
                else: stack.append(s[i])
            else:
                br_str = ""
                while stack[-1] != '[':
                    br_str = stack.pop() + br_str
                stack.pop() # open bracket
                count = stack.pop()
                for i in range(int(count)):
                    stack.append(br_str)

        return "".join(stack)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if not stack or temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
                continue

            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped_index = stack.pop()
                result[popped_index] = i - popped_index
            stack.append(i)

        return result
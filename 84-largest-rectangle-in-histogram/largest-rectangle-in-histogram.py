class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(-69)
        for i in range(len(heights)):
            if not stack or heights[i] >= stack[-1][1]:
                stack.append([i, heights[i]])
            elif heights[i] < stack[-1][1]:
                idx = 0
                while len(stack) != 0 and heights[i] < stack[-1][1]:
                    [j, h] = stack.pop()
                    if max_area < (h * (i - j)): max_area = h * (i - j)
                    idx = j
                stack.append([idx, heights[i]])
        return max_area

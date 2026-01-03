class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        left_pos = 0
        right_pos = len(height) - 1
        left_max = height[left_pos]
        right_max = height[right_pos]
        total_water = 0

        while left_pos < right_pos:
            if left_max < right_max or left_max == right_max:
                left_pos += 1
                left_max = max(left_max, height[left_pos])
                total_water += left_max - height[left_pos]
                print(left_max - height[left_pos])

            elif right_max < left_max:
                right_pos -= 1
                right_max = max(right_max, height[right_pos])
                total_water += right_max - height[right_pos]
                print(right_max - height[right_pos])

        return total_water
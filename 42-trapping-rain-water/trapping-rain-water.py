class Solution:
    def trap(self, height: List[int]) -> int:
        left_max_arr = [0]
        right_max_arr = [0]
        total_water = 0

        for i in range(1, len(height)):
            left_max_arr.append(max(left_max_arr[len(left_max_arr) - 1], height[i - 1]))
            right_max_arr.insert(0, max(right_max_arr[0], height[len(height) - i]))

        for i in range(len(height)):
            if height[i] < min(left_max_arr[i], right_max_arr[i]):
                total_water += min(left_max_arr[i], right_max_arr[i]) - height[i]

        return total_water
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

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
// ideal solution with two pointers
// Time complexity: O(n)
// Space complexity: O(1)



// class Solution:
//    def trap(self, height: List[int]) -> int:
//        left_max_arr = [0]
//        right_max_arr = [0]
//        total_water = 0

//        for i in range(1, len(height)):
//            left_max_arr.append(max(left_max_arr[len(left_max_arr) - 1], height[i - 1]))
//            right_max_arr.insert(0, max(right_max_arr[0], height[len(height) - i]))

//        for i in range(len(height)):
//            if height[i] < min(left_max_arr[i], right_max_arr[i]):
//                total_water += min(left_max_arr[i], right_max_arr[i]) - height[i]

//        return total_water
// Time complexity: O(n)
// Space complexity: O(n)


// class Solution:
//    def trap(self, height: List[int]) -> int:
//        total_water = 0
//        trapped = []
//        for curr_pos in range(1, len(height)):
//            max_left = 0
//            for idx in range(curr_pos - 1, -1, -1):
//                max_left = max(max_left, height[idx])

//            max_right = 0
//            for idx in range(curr_pos + 1, len(height), 1):
//                max_right = max(max_right, height[idx])

//            if height[curr_pos] < min(max_left, max_right):
//                total_water += min(max_left, max_right) - height[curr_pos]
//                trapped.append(min(max_left, max_right) - height[curr_pos])
//        print(trapped)
//        return total_water
// My original brute force solution
// Time complexity: O(n^2)
// Space complexity: O(1)

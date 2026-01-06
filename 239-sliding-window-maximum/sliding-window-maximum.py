from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we need to keep track of the max number in window of k
        # sort of like a CNN kernel
        # this is a monotonic queue
        q = deque()
        # when we add a new element, we pop right until we see a >= elem
        # then, when we move the window, we pop left one if the elems are equal.
        # the biggest element will be on the left. 
        for num in nums[:k]:
            while q and q[-1] < num:
                q.pop()
            q.append(num)

        out = [q[0]]

        for i, num in enumerate(nums[k:]):
            if q[0] == nums[i]:
                q.popleft()
            while q and q[-1] < num:
                q.pop()
            q.append(num)
            out.append(q[0])
        
        return out

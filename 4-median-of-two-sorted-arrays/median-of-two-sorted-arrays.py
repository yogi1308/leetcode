class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shorter, longer = [], []
        if len(nums1) <= len(nums2): 
            longer = nums2
            shorter = nums1
        else: 
            longer = nums1
            shorter = nums2
        for num in shorter:
            l, r = 0, len(longer) - 1
            while l <= r:
                mid = ((r - l) // 2) + l
                if mid + 1 == len(longer): 
                    longer.append(num)
                    break
                elif num < longer[mid] and mid == 0: 
                    longer.insert(0, num)
                    break
                elif longer[mid] < num < longer[mid + 1] or longer[mid] == num:
                    longer.insert(mid + 1, num)
                    break
                elif longer[mid] < num:
                    l = mid + 1
                elif longer[mid] > num:
                    r = mid - 1
                else: l = mid + 1
                
        if len(longer) % 2 == 1:
            return longer[len(longer) // 2]
        else:
            return (longer[len(longer) // 2] + longer[(len(longer) // 2) - 1]) / 2
                
                


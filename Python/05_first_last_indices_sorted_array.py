"                       Shree Krishnaya Namaha          "

class Solution:
    def searchRange(self, nums, target):
        target_idx = [-1, -1]
        elem_found = self.binSeracTgthMinMaxIdx(nums, target)
        if elem_found != -1: 
            target_idx[0] = elem_found
            target_idx[1] = self.binSeracTgthMinMaxIdx(nums, target, False)
        return target_idx
       
    def binSeracTgthMinMaxIdx(self, nums, target, find_min_idx=True):
        """
        
        """
        low = 0
        high = len(nums)
        found = False
        while low < high:
            mid = (high + low) // 2
            # The tgt is in lower half
            if target < nums[mid] or (find_min_idx and target == nums[mid]):
                high = mid
            else:
                low = mid + 1
            if target == nums[mid]:
                found = True
        if found:
            return low if find_min_idx else low - 1
        else:
            return -1

# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().searchRange(arr, x))

arr = [1, 4] 
x = 4
print(Solution().searchRange(arr, x))
# [1, 4]
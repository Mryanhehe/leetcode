from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i , j = 0 ,0
        if not nums:
            return 0
        while j < len(nums):
            while j < len(nums) and nums[j] == val:
                j+=1
            if j < len(nums):
                nums[i] = nums[j]
                i += 1
                j += 1
        return i

print(Solution().removeElement([0,1,2,2,3,0,4,2],2))



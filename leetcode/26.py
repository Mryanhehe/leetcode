from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i , j = 0 , 1
        if not nums:
            return 0
        for i in range(len(nums)):
            if j<len(nums):
                while nums[i] == nums[j]:
                    j+=1
                    if j >= len(nums):
                        return i+1
                nums[i+1] = nums[j]
                j+=1
            else:
                return i+1
        # return nums


print(Solution().removeDuplicates([1,1]))
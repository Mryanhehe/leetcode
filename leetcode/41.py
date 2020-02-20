from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        i = 1
        while True:
            if i in nums:
                nums.remove(i)
                i+=1
            else:return i

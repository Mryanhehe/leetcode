from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        start ,end = 0,len(nums)-1
        mid = 0
        if nums[start] < target or nums[end] < target:
            return [-1,-1]
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                break
            if nums[mid] < target:
                start = mid + 1
            else:end = start - 1


        return [-1,-1]
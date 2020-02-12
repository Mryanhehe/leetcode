from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        if nums[0] > target or nums[len(nums)-1] < target:
            return [-1,-1]
        left = 0
        ret = []
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if left == len(nums):
            left = -1
        if nums[left] != target:
            left = -1
        ret.append(left)
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        left -= 1
        if nums[left] != target:
            left = -1
        ret.append(left)
        return ret
print(Solution().searchRange([1] , 1))


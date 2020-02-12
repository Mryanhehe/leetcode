from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left ,right = 0 ,len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid
        if nums[left-1] == target:
            return left-1
        else:return left
print(Solution().searchInsert([1,3,5,6] , 5))

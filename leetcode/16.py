from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        print(nums)
        s = float('inf')
        m = float('inf')
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                left = i+1
                right = len(nums) - 1
                while left < right:
                    ans = nums[i] + nums[left] + nums[right]
                    if ans == target:
                        return target
                    if abs(ans-target) < s:
                        s = abs(ans-target)
                        m = ans
                    if ans > target:
                        right -= 1
                        while left < right and nums[right] == nums[right+1]:
                            right -=1
                    if ans < target:
                        left +=1
                        while left < right and nums[left] == nums[left-1]:
                            left+=1
        return m
so = Solution()
print(so.threeSumClosest(nums=[-1,2,1,-4],target=4))
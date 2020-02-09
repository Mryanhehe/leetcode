from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        ans = []
        nums = sorted(nums)
        # print(nums)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                for k in range(i+1,len(nums)):
                    if k == i + 1 or nums[k] != nums[k-1]:
                        right = len(nums) - 1
                        left = k+1
                        while left < right:
                            s = nums[i] + nums[k] + nums[left] + nums[right]
                            if s == target:
                                ans.append([nums[i] , nums[k],nums[left],nums[right]])
                                left +=1
                                right -= 1
                                while left < right and nums[left] == nums[left-1]:
                                    left +=1
                                while left < right and nums[right] == nums[right+1]:
                                    right -=1
                            elif s > target:
                                right -=1
                            else:left +=1
        return ans
        pass

so = Solution()
print(so.fourSum([-1,-5,-5,-3,2,5,0,4],-7))
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        begin,end ,ans = 0,1 ,0
        while end < len(nums):
            pos = 0
            for i in range(begin,end):
                pos = max(nums[i] + i , pos)
            begin = end
            end = pos+1
            ans += 1
        return ans
print(Solution().jump([1,2]))

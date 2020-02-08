from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        co = sorted(nums)
        print(co)
        ret = []
        for i in range(len(co)):
            if i==0 or co[i] != co[i-1]:
                left = i+1
                right = len(co)-1
                while left < right:
                    s = co[i] + co[left]+co[right]
                    if s == 0:
                        ret.append([co[i],co[left],co[right]])
                        left += 1
                        right -=1
                        while left < right and co[left] == co[left-1]:
                            left +=1
                        while left < right and co[right] == co[right+1]:
                            right -=1
                    elif s>0:
                        right -=1
                    else:left+=1
        return ret


so = Solution()
print(so.threeSum([-1,0,1,2,-1,-4]))
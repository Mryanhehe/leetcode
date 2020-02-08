from functools import lru_cache
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i , j = 0,len(height)-1
        res = 0
        while i<j:
            res = max(res,(j-i) * min(height[j],height[i]))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return res
        pass




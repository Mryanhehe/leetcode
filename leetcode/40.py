from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        candidates = sorted(candidates)
        n = len(candidates)
        def helper(copy , res_sum , tmp):
            if res_sum == target:
                res.append(tmp)
                return
            if res_sum > target:
                return
            for i in range(len(copy)):
                if i > 0 and copy[i] == copy[i-1]:
                    continue
                helper(copy[i+1:],res_sum+copy[i] , tmp + [copy[i]])
        helper(candidates,0,[])
        return res

print(Solution().combinationSum2([10,1,2,7,6,1,5],8))

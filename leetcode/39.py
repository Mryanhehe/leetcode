from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates = sorted(candidates)
        if not candidates:
            return ret
        n = len(candidates)
        def helper(i,res_sum,tmp:List[int]):
            if i == n or res_sum > target:
                return
            if res_sum == target:
                ret.append(tmp)
                return
            helper(i , res_sum +  candidates[i] , tmp.append(candidates[i]))
            helper(i+1,res_sum,tmp)
        helper(0,0,[])
        return ret


        return ret
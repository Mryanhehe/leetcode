from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        if m == 0 and n == 0 :
            return True
        @lru_cache(None)
        def check(i,j):
            # 如果s到头了
            if i == m:
                while j < n and p[j] == '*':
                    j += 1
                return (j==n)
            if j == n:
                return False
            if s[i] == p[j] or p[j] == '?':
                return check(i+1,j+1)
            elif p[j] == '*':
                return check(i+1,j) or check(i,j+1)
            else:
                return False
        return check(0,0)
print(Solution().isMatch('acdcb','a*c?b'))




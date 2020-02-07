class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        ## checking from right to left
        from functools import lru_cache
        @lru_cache(None)
        def check(i,j):
            if j==-1:
                return (i==-1)
            if i==-1:
                if p[j]=="*" and j>=1:
                    return check(i,j-2)
                else:
                    return False
            if p[j] =="*" and j>=1:
                return (s[i]==p[j-1] or p[j-1]==".") and (check(i-1,j) or check(i-1,j-2)) or check(i,j-2)
            if p[j]=="." or s[i]==p[j]:
                return check(i-1,j-1)
            else:
                return False
        return check(n-1,m-1)
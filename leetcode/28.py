class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        j = 0
        for i in range(len(haystack)-len(needle)+1):
            while haystack[i+j] == needle[j] and j < len(needle):
                j += 1
                if j == len(needle):
                    return i
            j = 0
        return -1
        pass
print(Solution().strStr("a","a"))
class Solution:
    def reverse(self, x: int) -> int:
        if x <= -2147483648 or x >= 2147483647:
            print('yes')
            return 0

        m = str(abs(x))
        s = m[::-1]
        s1 = int(s)
        if x > 0 :
            if s1 > 2147483647:
                return 0
            return s1
        else:
            if s1 > 2147483648:
                return 0
            return 0-s1
        pass

s = Solution()
print(s.reverse(-1563847412))

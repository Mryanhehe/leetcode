import re
class Solution:

    def myAtoi(self, str: str) -> int:
        str = str.strip()
        # print(str)
        pattern = "[0-9\-\+]*"
        try:
            ans = re.match(pattern, str).group()
            if ans[0] == '-':
                flag = -1
            else:
                flag = 1
            ans = re.sub('-','',ans)
            ans = re.sub('\+','',ans)
            ans = int(ans) * flag
            if ans > 2**31 -1:
                return 2**31 - 1
            elif ans >0:
                return ans
            if ans < -2**31:
                return -2**31
            else:
                return ans
        except:
            return 0;
        pass
    # def convert(self,s):
    #     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'-':'-'}
    #     return digits.get(s,'')
    #     pass
    # def fn(self,x,y):
    #     return x
so = Solution()
print(so.myAtoi('   -42-'))
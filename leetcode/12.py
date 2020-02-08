class Solution:
    def intToRoman(self, num: int) -> str:
        # digits = {1000: 'M', 900: 'C', 500: 'D', 400: 'CD', 100: 'C',
        #           90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        values = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        co = num
        a = [0]*13
        i = 0
        while co:
            m = int(co/nums[i])
            co = co % nums[i]
            # print(m,co)
            a[i] = m
            i+=1
        # print(len(a),len(values))
        print(a)
        print(values)
        ret = dict(zip(values,a))
        print(ret)
        return ''.join(item[0]*item[1] for item in ret.items())


so = Solution()
print(so.intToRoman(1994))
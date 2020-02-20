from  functools import reduce
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = []
        if not num1 or not num2:
            return ''
        if num1 == '0' or num2 == '0':
            return '0'

        # 保证num1>num2
        if len(num1) < len(num2):
            num1 , num2 = num2 , num1
        #     将num2逆序
        num2 = num2[::-1]
        co_num1 = num1[::-1]
        for i,s in enumerate(num2):
            m = [0] * i if i > 0 else []
            for j,sm in enumerate(co_num1):
                ret = self.fn(s) * self.fn(sm)
                if j == 0:
                    m.append(ret % 10)
                    carry = ret // 10
                else:
                    ret += carry
                    carry = ret // 10
                    m.append(ret % 10)
            m.append(carry)
            res.append(m)
        size = len(res[-1])
        print(res)
        m1 = []
        carry = 0
        for i in range(size):
            su = 0
            for ans in res:
                if i >= len(ans):
                    su += 0
                else:su += ans[i]
            su += carry
            m1.append(su % 10)
            carry = su // 10
        k = reduce(lambda x, y: str(x) + str(y) , m1[::-1])
        if k[0] == '0':
            k = k[1:]
        return k

    def fn(self, s):
        digis = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digis[s]
print(Solution().multiply('111111111111','2132124124'))







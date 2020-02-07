class Solution:
    def convert(self, s: str, numRows: int) -> str:
        num = len(s)
        s_copy = s
        sizes = [1] * num
        if numRows > 1:
            for i in range(0,num , 2 * numRows - 2):
                print(i)
                for j in range(numRows):
                    try:
                        sizes[i + numRows-1 - j] = numRows - j
                        sizes[i + numRows - 1 + j] = numRows - j
                    except:
                        print('')

            print(sizes)
            m = []
            for i in range(numRows):
                for j in range(num):
                    if sizes[j] == i+1:
                        m.append(s_copy[j])
            print(''.join(m))
            return sizes
        else:
            return s
s = Solution()
s.convert('PAYPALISHIRING',1)
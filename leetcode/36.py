from typing import List
from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 每行的个数
        rows = []
        for i in range(9):
            rows.append(Counter())
        # 每列的个数
        cols = []
        for i in range(9):
            cols.append(Counter())
        # 每个区域的个数
        box = []
        for i in range(9):
            box.append(Counter())
        for i in range(9):
            for j in range(9):
                if not board[j][i]=='.':
                    rows[j][board[j][i]] += 1
                    cols[i][board[j][i]] += 1
                    box[(j//3) * 3 + (i//3)][board[j][i]] += 1
            for k in '123456789':
                if rows[i][k] > 1 or cols[i][k] >1 or box[i][k] > 1:
                    return False
        return True

print(Solution().isValidSudoku(
    [["7",".",".",".","4",".",".",".","."],
     [".",".",".","8","6","5",".",".","."],
     [".","1",".","2",".",".",".",".","."],
     [".",".",".",".",".","9",".",".","."],
     [".",".",".",".","5",".","5",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".","2",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."]]))



__author__ = 'Jia'
'''
The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a
queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        # [l, m, n] means the first row's queen is in index l ...
        tmp = []
        queenList = [-1 for i in range(n)]
        self.solveNQueensRec(queenList, 0, n, tmp)
        result = []
        for q in tmp:
            result.append(self.buildResult(q))
        return result

    def solveNQueensRec(self, queenList, row, length, result):
        if row >= length:
            l = list(queenList)
            result.append(l)
        for col in range(length):
            if self.isValid(queenList, row, col):
                queenList[row] = col
                self.solveNQueensRec(queenList, row + 1, length, result)

    def isValid(self, queenList, row, col):
        r = 0
        while r < row:
            pre = queenList[r]
            if pre == col or pre == col - row + r or pre == col + row - r:
                return False
            r += 1
        return True

    def buildResult(self, queenList):
        result = []
        for index in queenList:
            s = ['.' for i in range(len(queenList))]
            s[index] = 'Q'
            result.append(''.join(s))
        return result

s = Solution()
result = s.solveNQueens(9)
for l in result:
    print ()
    for s in l:
        print s
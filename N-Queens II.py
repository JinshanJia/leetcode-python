__author__ = 'Jia'
'''
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        queenList = [-1 for i in range(n)]
        return self.totoalNQueensRec(0, queenList)

    def totoalNQueensRec(self, row, queenList):
        if row >= len(queenList):
            return 1
        col = 0
        result = 0
        while col < len(queenList):
            if self.isValid(row, col, queenList):
                queenList[row] = col
                result += self.totoalNQueensRec(row + 1, queenList)
            col += 1
        return result

    def isValid(self, row, col, queenList):
        r = 0
        while r < row:
            pre = queenList[r]
            if pre == col or pre == col + (row - r) or pre == col - (row - r):
                return False
            r += 1
        return True
__author__ = 'Jia'
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        row, col = self.findNextPoint(board, -1, -1)
        self.solveSudokuRec(board, row, col)

    def solveSudokuRec(self, board, currRow, currCol):
        if currRow == -1:
            return True
        nextRow, nextCol = self.findNextPoint(board, currRow, currCol)
        for i in range(1, 10):
            if self.isNumberValid(board, currRow, currCol, i):
                board[currRow][currCol] = str(i)
                if self.solveSudokuRec(board, nextRow, nextCol):
                    return True
        board[currRow][currCol] = '.'
        return False

    def isNumberValid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == str(num):
                return False

        for i in range(9):
            if board[i][col] == str(num):
                return False

        squareRow = row / 3
        squareCol = col / 3
        for i in range(3):
            for j in range(3):
                if board[squareRow * 3 + i][squareCol * 3 + j] == str(num):
                    return False
        return True

    def findNextPoint(self, board, currRow, currCol):
        if currRow == -1:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return i, j
            return -1, -1
        for i in range(currCol + 1, 9):
            if board[currRow][i] == '.':
                return currRow, i
        for i in range(currRow + 1, 9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j
        return -1, -1

s = Solution()
board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
]

s.solveSudoku(board)
for l in board:
    print l
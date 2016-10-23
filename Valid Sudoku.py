__author__ = 'Jia'
'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        colCheck = []
        for a in range(9):
            l = [0 for a in range(9)]
            colCheck.append(l)
        for i in range(9):
            rowCheck = [0 for a in range(9)]
            if i % 3 == 0:
                sqrCheck = []
                for a in range(3):
                    l = [0 for a in range(9)]
                    sqrCheck.append(l)
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j]) - 1
                if rowCheck[num] != 0 or colCheck[j][num] != 0 or sqrCheck[j / 3][num] != 0:
                    return False
                rowCheck[num] += 1
                colCheck[j][num] += 1
                sqrCheck[j / 3][num] += 1
        return True


s = Solution()
board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '4', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
]
print s.isValidSudoku(board)
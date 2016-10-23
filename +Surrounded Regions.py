__author__ = 'Jia'
'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''
import collections
class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if len(board) == 0 or len(board[0]) == 0:
            return
        queue = collections.deque()
        for i in range(len(board)):
            if board[i][0] == 'O':
                board[i][0] = 'V'
                queue.append([i, 0])
            if board[i][len(board[0]) - 1] == 'O':
                board[i][len(board[0]) - 1] = 'V'
                queue.append([i, len(board[0]) - 1])
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                board[0][i] = 'V'
                queue.append([0, i])
            if board[len(board) - 1][i] == 'O':
                board[len(board) - 1][i] = 'V'
                queue.append([len(board) - 1, i])
        while len(queue) != 0:
            [row, col] = queue.popleft()
            if row - 1 >= 0 and board[row - 1][col] == 'O':
                board[row - 1][col] = 'V'
                queue.append([row - 1, col])
            if row + 1 < len(board) and board[row + 1][col] == 'O':
                board[row + 1][col] = 'V'
                queue.append([row + 1, col])
            if col - 1 >= 0 and board[row][col - 1] == 'O':
                board[row][col - 1] = 'V'
                queue.append([row, col - 1])
            if col + 1 < len(board[0]) and board[row][col + 1] == 'O':
                board[row][col + 1] = 'V'
                queue.append([row, col + 1])
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 'O' if board[i][j] == 'V' else 'X'

s = Solution()
board = [["O"]]
s.solve(board)
print board
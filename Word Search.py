__author__ = 'Jia'
'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if word is None or len(word) == 0:
            return True
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return False
        searched = [[False] * len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.existRec(board, searched, word, 0, i, j):
                        return True
        return False

    def existRec(self, board, searched, word, index, row, col):
        if index == len(word) - 1:
            return True
        searched[row][col] = True
        if row - 1 >= 0 and not searched[row - 1][col] and word[index + 1] == board[row - 1][col]:
            if self.existRec(board, searched, word, index + 1, row - 1, col):
                return True
        if row + 1 < len(board) and not searched[row + 1][col] and word[index + 1] == board[row + 1][col]:
            if self.existRec(board, searched, word, index + 1, row + 1, col):
                return True
        if col - 1 >= 0 and not searched[row][col - 1] and word[index + 1] == board[row][col - 1]:
            if self.existRec(board, searched, word, index + 1, row, col - 1):
                return True
        if col + 1 < len(board[0]) and not searched[row][col + 1] and word[index + 1] == board[row][col + 1]:
            if self.existRec(board, searched, word, index + 1, row, col + 1):
                return True
        searched[row][col] = False
        return False

s = Solution()
board = [
  "ABCE",
  "SFCS",
  "ADEE"
]

# board = ['aa']
# word = "ABCCED"
word = "SEE"
# word = "ABCB"
print s.exist(board, word)
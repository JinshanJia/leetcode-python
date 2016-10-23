__author__ = 'Jia'
'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0 for i in range(n)] for j in range(n)]
        self.generateMatrixRec(matrix, 0, 1, n)
        return matrix

    def generateMatrixRec(self, matrix, index, startNum, length):
        if startNum > length * length:
            return
        # upper row
        curr = index
        while curr < length - index:
            matrix[index][curr] = startNum
            startNum += 1
            curr += 1
        # right col
        curr = index + 1
        while curr < length - index:
            matrix[curr][length - index - 1] = startNum
            startNum += 1
            curr += 1
        # lower row
        curr = length - index - 2
        while length - index - 1 != index and curr >= index:
            matrix[length - index - 1][curr] = startNum
            startNum += 1
            curr -= 1
        # left col
        curr = length - index - 2
        while length - index - 1 != index and curr > index:
            matrix[curr][index] = startNum
            startNum += 1
            curr -= 1
        self.generateMatrixRec(matrix, index + 1, startNum, length)


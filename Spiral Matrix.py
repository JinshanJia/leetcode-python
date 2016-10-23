__author__ = 'Jia'
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        result = []
        self.spiralOrderRec(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1, result)
        return result

    def spiralOrderRec(self, matrix, upperR, lowerR, leftC, rightC, result):
        if upperR > lowerR or leftC > rightC:
            return
        indexR = upperR
        indexC = leftC
        # append upperRow
        while indexC <= rightC:
            result.append(matrix[indexR][indexC])
            indexC += 1
        # append rightC
        indexR = upperR + 1
        indexC = rightC
        while indexR <= lowerR:
            result.append(matrix[indexR][indexC])
            indexR += 1
        # append lowerR
        indexR = lowerR
        indexC = rightC - 1
        while indexR != upperR and indexC >= leftC:
            result.append(matrix[indexR][indexC])
            indexC -= 1
        # append lowerR
        indexR = lowerR - 1
        indexC = leftC
        while indexC != rightC and indexR >= upperR + 1:
            result.append(matrix[indexR][indexC])
            indexR -= 1
        self.spiralOrderRec(matrix, upperR + 1, lowerR - 1, leftC + 1, rightC - 1, result)


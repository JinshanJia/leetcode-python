__author__ = 'Jia'
'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        self.rotateRec(matrix, 0, len(matrix) - 1)
        return matrix

    def rotateRec(self, matrix, smaller, larger):
        if smaller >= larger:
            return
        i = 0
        while i < larger - smaller:
            tmp = matrix[smaller + i][larger]
            matrix[smaller + i][larger] = matrix[smaller][smaller + i]
            matrix[smaller][smaller + i] = matrix[larger - i][smaller]
            matrix[larger - i][smaller] = matrix[larger][larger - i]
            matrix[larger][larger - i] = tmp
            i += 1
        self.rotateRec(matrix, smaller + 1, larger - 1)

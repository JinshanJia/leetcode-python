__author__ = 'Jia'
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        matrix = [
            [0 for i in range(n)] for j in range(m)
        ]
        for i in range(n):
            matrix[0][i] = 1
        for i in range(m):
            matrix[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[-1][-1]
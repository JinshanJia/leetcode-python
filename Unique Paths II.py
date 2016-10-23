__author__ = 'Jia'
'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        matrix = [
            [0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))
        ]
        matrix[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1 or matrix[0][i - 1] == 0:
                matrix[0][i] = 0
            else:
                matrix[0][i] = 1
        for j in range(1, len(obstacleGrid)):
            if obstacleGrid[j][0] == 1 or matrix[j - 1][0] == 0:
                matrix[j][0] = 0
            else:
                matrix[j][0] = 1
        for j in range(1, len(obstacleGrid)):
            for i in range(1, len(obstacleGrid[0])):
                if obstacleGrid[j][i] == 1:
                    matrix[j][i] = 0
                else:
                    matrix[j][i] = matrix[j - 1][i] + matrix[j][i - 1]
        return matrix[-1][-1]
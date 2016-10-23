__author__ = 'Jia'
'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
'''

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        result = 0
        heights = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for j in range(len(matrix[0])):
            heights[0][j] = int(matrix[0][j])
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    heights[i][j] = 0
                else:
                    heights[i][j] = heights[i - 1][j] + 1
        for i in range(len(heights)):
            result = max(result, self.maxArea(heights[i]))
        return result

    def maxArea(self, l):
        h = list(l)
        h.append(0)
        stack = []
        result = 0
        for i in range(len(h)):
            while len(stack) != 0 and h[stack[-1]] > h[i]:
                index = stack.pop()
                if len(stack) != 0:
                    result = max(result, (i - 1 - stack[-1]) * h[index])
                else:
                    result = max(result, i * h[index])
            stack.append(i)
        return result

s = Solution()
matrix = [
    "1"
]
print s.maximalRectangle(matrix)
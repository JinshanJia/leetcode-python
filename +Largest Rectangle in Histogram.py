__author__ = 'Jia'
'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area
of largest rectangle in the histogram.
For example,
Given height = [2,1,5,6,2,3],
return 10.
'''

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        h = list(height)
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
__author__ = 'Jia'
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are
drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a
container, such that the container contains the most water.

Note: You may not slant the container.
'''

class Solution:
    # @return an integer
    def maxArea(self, height):
        if height is None:
            return 0
        left = 0
        right = len(height) - 1
        result = 0
        preLHeight = 0
        preRHeight = 0
        while left < right:
            preLHeight = height[left]
            preRHeight = height[right]
            result = max(result, (right - left) * min(preLHeight, preRHeight))
            if preLHeight < preRHeight:
                while height[left] <= preLHeight and left < right:
                    left += 1
            else:
                while height[right] <= preRHeight and left < right:
                    right -= 1

        return result

s = Solution()
height = [3,2,1,5,6,0,3]
print s.maxArea(height)
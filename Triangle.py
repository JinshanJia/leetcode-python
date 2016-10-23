__author__ = 'Jia'
'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row
below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if triangle is None or len(triangle) == 0:
            return 0
        result = list(triangle[0])
        for row in range(1, len(triangle)):
            tmp = list(triangle[row])
            tmp[0] += result[0]
            tmp[-1] += result[-1]
            for i in range(1, len(tmp) - 1):
                tmp[i] += min(result[i - 1], result[i])
            result = tmp
        return min(result)

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

s = Solution()
print s.minimumTotal(triangle)
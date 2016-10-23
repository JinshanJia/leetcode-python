__author__ = 'Jia'
'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows <= 0:
            return []
        result = [[1]]
        count = 1
        while count < numRows:
            tmp = [1]
            pre = result[-1]
            for i in range(len(pre) - 1):
                tmp.append(pre[i] + pre[i + 1])
            tmp.append(1)
            result.append(tmp)
            count += 1
        return result
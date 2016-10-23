__author__ = 'Jia'
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        return self.combineRec(n, 1, k)

    def combineRec(self, n, startNum, k):
        result = []
        if k == 1:
            for i in range(startNum, n + 1):
                result.append([i])
            return result
        for i in range(startNum, n - k + 2):
            later = self.combineRec(n, i + 1, k - 1)
            for l in later:
                tmp = [i]
                tmp.extend(l)
                result.append(tmp)
        return result
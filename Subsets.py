__author__ = 'Jia'
'''
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S = sorted(S)
        result = []
        for i in range(1, len(S) + 1):
            result.extend(self.subSetsOfSpecificNum(S, 0, i))
        result.append([])
        return result

    def subSetsOfSpecificNum(self, S, startIndex, num):
        result = []
        if num == 1:
            for i in S[startIndex:]:
                result.append([i])
            return result
        for i in range(startIndex, len(S) - num + 1):
            later = self.subSetsOfSpecificNum(S, i + 1, num - 1)
            for l in later:
                tmp = [S[i]]
                tmp.extend(l)
                result.append(tmp)
        return result

    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets2(self, S):
        S = sorted(S)
        result = [[]]
        for i in range(len(S)):
            for j in range(len(result)):
                tmp = list(result[j])
                tmp.append(S[i])
                result.append(tmp)
        return result


s = Solution()
print s.subsets2([1,2,3])

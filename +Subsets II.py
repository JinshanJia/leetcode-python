__author__ = 'Jia'
'''
Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        result = []

        def subsetsWithDupRec(S, startIndex, length):
            result = []
            pre = None
            if length == 0:
                return [[]]
            for i in range(startIndex, len(S) + 1 - length):
                if S[i] != pre:
                    tmp = subsetsWithDupRec(S, i + 1, length - 1)
                    for l in tmp:
                        toAdd = [S[i]]
                        toAdd.extend(l)
                        result.append(toAdd)
                pre = S[i]
            return result

        for i in range(0, len(S) + 1):
            result.extend(subsetsWithDupRec(S, 0, i))
        return result

    def subsetsWithDup2(self, S):
        S.sort()
        result = [[]]
        pre = S[0]
        preSize = 0
        for i in range(len(S)):
            tmpSize = preSize
            preSize = len(result)
            if S[i] != pre:
                pre = S[i]
                tmpSize = 0
            for j in range(tmpSize, len(result)):
                tmp = list(result[j])
                tmp.append(S[i])
                result.append(tmp)
        return result

s = Solution()
S = [1, 1, 2, 3, 3]
print s.subsetsWithDup2(S)

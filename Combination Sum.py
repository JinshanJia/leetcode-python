__author__ = 'Jia'
'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate
numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = self.combinationSumRec(candidates, target, 0)
        return result

    def combinationSumRec(self, candidates, target, startIndex):
        if startIndex >= len(candidates) or target < candidates[startIndex]:
            return []
        currNum = candidates[startIndex]
        if target == currNum:
            return [[target]]
        r1 = self.combinationSumRec(candidates, target - currNum, startIndex)
        r2 = self.combinationSumRec(candidates, target, startIndex + 1)
        result = []
        for l in r1:
            tmp = [currNum]
            tmp.extend(l)
            result.append(tmp)
        result.extend(r2)
        return result

s = Solution()
l = [2,3,6,7]
print s.combinationSum(l, 6)
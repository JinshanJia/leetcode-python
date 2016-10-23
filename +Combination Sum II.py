__author__ = 'Jia'
'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the
candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.combinationSumRec(candidates, target, 0)

    def combinationSumRec(self, candidates, target, index):
        if index >= len(candidates) or candidates[index] > target:
            return []
        currNum = candidates[index]
        if currNum == target:
            return [[currNum]]

        nextUndupIndex = index + 1
        while nextUndupIndex < len(candidates) and candidates[nextUndupIndex] == currNum:
            nextUndupIndex += 1
        result = self.combinationSumRec(candidates, target, nextUndupIndex)
        r2 = self.combinationSumRec(candidates, target - currNum, index + 1)
        for l in r2:
            tmp = [currNum]
            tmp.extend(l)
            result.append(tmp)
        return result

s = Solution()
l = [10,1,2,7,6,1,5, 1]
print s.combinationSum2(l, 8)
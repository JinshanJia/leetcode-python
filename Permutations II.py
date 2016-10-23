__author__ = 'Jia'
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        return self.permuteUniqueRec(num, 0)

    def permuteUniqueRec(self, num, startIndex):
        if startIndex >= len(num):
            return [[]]
        result = []
        searched = {}
        for i in range(startIndex, len(num)):
            if num[i] in searched.keys():
                continue
            searched[num[i]] = 1
            self.swap(num, i, startIndex)
            tmp = self.permuteUniqueRec(num, startIndex + 1)
            for l in tmp:
                r = [num[startIndex]]
                r.extend(l)
                result.append(r)
            self.swap(num, i, startIndex)
        return result

    def swap(self, num, a, b):
        tmp = num[a]
        num[a] = num[b]
        num[b] = tmp

s = Solution()
num = [1,2,1,2]
print s.permuteUnique(num)
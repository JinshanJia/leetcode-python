__author__ = 'Jia'
'''
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        return self.permuteRec(num, 0)

    def permuteRec(self, num, startIndex):
        if startIndex == len(num):
            return [[]]
        result = []
        for i in range(startIndex, len(num)):
            self.swap(num, startIndex, i)
            tmp = self.permuteRec(num, startIndex + 1)
            for l in tmp:
                r = [num[startIndex]]
                r.extend(l)
                result.append(r)
            self.swap(num, startIndex, i)
        return result

    def swap(self, num, a, b):
        tmp = num[a]
        num[a] = num[b]
        num[b] = tmp

s = Solution()
num = [1,2]
print s.permute(num)
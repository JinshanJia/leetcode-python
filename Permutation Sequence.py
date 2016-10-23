__author__ = 'Jia'
'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        l = [i for i in range(1, n + 1)]
        factorial = [1 for i in range(10)]
        for i in range(2, 10):
            factorial[i] = factorial[i - 1] * i
        return self.getPermutationRec(l, factorial, k, "")

    def getPermutationRec(self, l, factorial, k, result):
        length = len(l)
        if length == 0:
            return result
        f = factorial[length - 1]
        tmp = (k - 1) / f
        result += str(l[tmp])
        l.pop(tmp)
        k -= tmp * f
        return self.getPermutationRec(l, factorial, k, result)

s = Solution()
print s.getPermutation(2, 2)
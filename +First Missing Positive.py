__author__ = 'Jia'
'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        index = 0
        while index < len(A):
            currNum = A[index]
            if currNum <= 0 or currNum > len(A) or currNum == index + 1 or A[currNum - 1] == currNum:
                index += 1
                continue
            tmp = A[currNum - 1]
            A[currNum - 1] = currNum
            A[index] = tmp

        for i in range(len(A)):
            if A[i] != i + 1:
                return i + 1
        return len(A) + 1

l = [3,4,2,1]
s = Solution()
print s.firstMissingPositive(l)
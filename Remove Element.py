__author__ = 'Jia'
'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if A is None or len(A) == 0:
            return 0
        toIndex = 0
        for i in range(len(A)):
            if A[i] != elem:
                A[toIndex] = A[i]
                toIndex += 1
        return toIndex

s = Solution()
A = [1,2,3,1,3,2,5]
print s.removeElement(A, 5)
print A
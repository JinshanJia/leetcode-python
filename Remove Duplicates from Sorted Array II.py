__author__ = 'Jia'
'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
'''
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A is None:
            return 0
        if len(A) <= 2:
            return len(A)
        toInsert = 1
        count = 1
        for index in range(1, len(A)):
            if A[index] != A[index - 1]:
                count = 1
            else:
                count += 1
            if count <= 2:
                A[toInsert] = A[index]
                toInsert += 1
        return toInsert

__author__ = 'Jia'
'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
'''
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A is None or len(A) == 0:
            return 0
        index = 0
        for i in range(1, len(A)):
            if A[i] != A[index]:
                index += 1
                A[index] = A[i]
        return index + 1

s = Solution()
A = [1,2,3,4,4]
print s.removeDuplicates(A)
print A
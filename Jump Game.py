__author__ = 'Jia'
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        maxIndex = A[0]
        index = 0
        while index <= maxIndex < len(A) - 1:
            maxIndex = max(index + A[index], maxIndex)
            index += 1
        if maxIndex >= len(A) - 1:
            return True
        else:
            return False
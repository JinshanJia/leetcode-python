__author__ = 'Jia'
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if A is None or len(A) == 0:
            return 0
        left = [0 for i in range(len(A))]
        right = [0 for i in range(len(A))]
        left[0] = A[0]
        right[- 1] = A[-1]
        for i in range(0, len(A)):
            left[i] = max(left[i - 1], A[i])
        for i in range(len(A) - 2, -1, -1):
            right[i] = max(right[i + 1], A[i])

        result = 0
        for i in range(len(A)):
            k = min(left[i], right[i])
            if A[i] < k:
                result += k - A[i]
        return result

    # @param A, a list of integers
    # @return an integer
    def trap2(self, A):
        left = 0
        right = len(A) - 1
        result = 0
        while left < right:
            if A[left] < A[right]:
                k = left + 1
                while A[k] < A[left]:
                    result += A[left] - A[k]
                    k += 1
                left = k
            else:
                k = right - 1
                while A[k] < A[right]:
                    result += A[right] - A[k]
                    k -= 1
                right = k
        return result
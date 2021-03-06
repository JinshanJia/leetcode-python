__author__ = 'Jia'
'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The
number of elements initialized in A and B are m and n respectively.
'''
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        A.extend(B)
        indexA = m - 1
        indexB = n - 1
        index = m + n - 1
        while indexA >= 0 and indexB >= 0:
            if A[indexA] > B[indexB]:
                A[index] = A[indexA]
                indexA -= 1
            else:
                A[index] = B[indexB]
                indexB -= 1
            index -= 1
        while indexA >= 0:
            A[index] = A[indexA]
            indexA -= 1
            index -= 1
        while indexB >= 0:
            A[index] = B[indexB]
            indexB -= 1
            index -= 1

s = Solution()
A = []
B = [1]
s.merge(A, len(A), B, len(B))
print A
__author__ = 'Jia'

# There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if (len(A) + len(B)) % 2 == 0:
            return (self.findKthRecursion(A, len(A), 0, B, len(B), 0, (len(A) + len(B)) / 2) +
                    self.findKthRecursion(A, len(A), 0, B, len(B), 0, (len(A) + len(B)) / 2 + 1)) / 2.
        else:
            return self.findKthRecursion(A, len(A), 0, B, len(B), 0, (len(A) + len(B)) / 2 + 1)

    def findKthRecursion(self, A, Alength, startA, B, Blength, startB, k):
        if Alength > Blength:
            return self.findKthRecursion(B, Blength, startB, A, Alength, startA, k)
        if Alength == 0:
            return B[startB + k - 1]
        if k == 1:
            if A[startA] > B[startB]:
                return B[startB]
            else:
                return A[startA]
        kA = min(k / 2, Alength)
        kB = k - kA
        if A[startA + kA - 1] > B[startB + kB - 1]:
            return self.findKthRecursion(A, Alength, startA, B, Blength - kB, startB + kB, k - kB)
        else:
            return self.findKthRecursion(A, Alength - kA, startA + kA, B, Blength, startB, k - kA)

A = [2,3,4]
B = [1]
s = Solution()
print s.findMedianSortedArrays(A, B)
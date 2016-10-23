__author__ = 'Jia'
'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if A is None:
            return [-1, -1]
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if A[mid] < target:
                left = mid + 1
            elif A[mid] > target:
                right = mid - 1
            else:
                return [self.findLeftPoint(A, target, left, mid - 1), self.findRightPoint(A, target, mid + 1, right)]
        return [-1, -1]

    def findLeftPoint(self, A, target, left, right):
        if left > right:
            return right + 1
        mid = left + (right - left) / 2
        if A[mid] == target:
            return self.findLeftPoint(A, target, left, mid - 1)
        return self.findLeftPoint(A, target, mid + 1, right)

    def findRightPoint(self, A, target, left, right):
        if left > right:
            return left - 1
        mid = left + (right - left) / 2
        if A[mid] == target:
            return self.findRightPoint(A, target, mid + 1, right)
        return self.findRightPoint(A, target, left, mid - 1)

list = [5, 7, 7, 8, 8, 8, 10, 10]
s = Solution()
print s.searchRange(list, 10)
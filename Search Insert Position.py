__author__ = 'Jia'
'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        return self.searchInsertRec(A, target, 0, len(A) - 1)

    def searchInsertRec(self, A, target, left, right):
        if left > right:
            return 0
        mid = left + (right - left) / 2
        if A[mid] == target:
            return mid
        if A[mid] > target:
            if mid == left:
                return left
            return self.searchInsertRec(A, target, left, mid - 1)
        if mid == right:
            return right + 1
        return self.searchInsertRec(A, target, mid + 1, right)

s = Solution()
l = []
print s.searchInsert(l, 0)
__author__ = 'Jia'
'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''
class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        return self.searchRec(A, target, 0, len(A) - 1)

    def searchRec(self, A, target, lower, upper):
        if lower > upper:
            return False
        mid = lower + (upper - lower) / 2
        if A[mid] == target:
            return True
        if A[lower] < A[mid]:
            if A[lower] <= target < A[mid]:
                return self.searchRec(A, target, lower, mid - 1)
            else:
                return self.searchRec(A, target, mid + 1, upper)
        elif A[lower] > A[mid]:
            if target >= A[lower] or target < A[mid]:
                return self.searchRec(A, target, lower, mid - 1)
            else:
                return self.searchRec(A, target, mid + 1, upper)
        elif A[mid] > A[upper]:
            if target > A[mid] or target <= A[upper]:
                return self.searchRec(A, target, mid + 1, upper)
            else:
                return False
        elif A[mid] < A[upper]:
            if A[mid] < target <= A[upper]:
                return self.searchRec(A, target, mid + 1, upper)
            else:
                return False
        else:
            return self.searchRec(A, target, mid + 1, upper) or self.searchRec(A, target, lower, mid - 1)


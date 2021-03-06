__author__ = 'Jia'
'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if A is None:
            return -1
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                return mid
            # pivot is in the right part
            if A[mid] >= A[left]:
                if A[mid] > target >= A[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if A[mid] < target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

s = Solution()
A = [2,3,4,2]
t = 2
print s.search(A, t)
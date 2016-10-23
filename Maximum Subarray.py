__author__ = 'Jia'
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is
more subtle.
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if A is None or len(A) == 0:
            return 0
        result = A[0]
        tmp = result
        for i in range(1, len(A)):
            if tmp <= 0:
                tmp = max(tmp, A[i])
            else:
                tmp += A[i]
            result = max(tmp, result)
        return result

    def maxSubArray2(self, A):
        return self.maxSubArrayRec(A, 0, len(A) - 1)

    def maxSubArrayRec(self, A, left, right):
        if left == right:
            return A[left]
        mid = left + (right - left) / 2
        leftResult = self.maxSubArrayRec(A, left, mid)
        rightResult = self.maxSubArrayRec(A, mid + 1, right)
        midResult = self.maxMid(A, left, right, mid)
        return max(leftResult, max(rightResult, midResult))

    def maxMid(self, A, left, right, mid):
        leftP = mid - 1
        leftResult = 0
        tmp = 0
        while leftP >= left:
            tmp += A[leftP]
            leftResult = max(leftResult, tmp)
            leftP -= 1
        rightP = mid + 1
        rightResult = 0
        tmp = 0
        while rightP <= right:
            tmp += A[rightP]
            rightResult = max(rightResult, tmp)
            rightP += 1
        return leftResult + rightResult + A[mid]



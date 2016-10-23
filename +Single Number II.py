__author__ = 'Jia'
'''
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        oneTime = 0
        twoTime = 0
        threeTime = 0
        for n in A:
            twoTime |= (oneTime & n)
            oneTime ^= n
            threeTime = oneTime & twoTime
            oneTime ^= threeTime
            twoTime ^= threeTime
            print oneTime, twoTime, threeTime
        return oneTime

s = Solution()
A = [1,2,3,2,2,3,3]
print s.singleNumber(A)
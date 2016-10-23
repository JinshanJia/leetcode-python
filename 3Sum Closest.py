__author__ = 'Jia'
'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.
For example, given array S = {-1 2 1 -4}, and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if num is None or len(num) < 3:
            return target
        num.sort()
        result = num[0] + num[1] + num[2] - target
        for index in range(len(num)):
            left = index + 1
            right = len(num) - 1
            while left < right:
                tmp = num[index] + num[left] + num[right] - target
                result = tmp if abs(tmp) < abs(result) else result
                if tmp == 0:
                    return target
                if tmp < 0:
                    left += 1
                else:
                    right -= 1
        return result + target

s = Solution()
num = [0,1,2]
print s.threeSumClosest(num, 3)
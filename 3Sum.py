__author__ = 'Jia'
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the
array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if num is None or len(num) == 0:
            return []
        num.sort()
        result = []
        pre = num[0]
        for index in range(len(num)):
            if pre == num[index] and index != 0:
                continue
            left = index + 1
            right = len(num) - 1
            pre = num[index]
            preLeft = -1
            preRight = -1
            while left < right:
                if num[left] + num[right] + num[index] > 0:
                    right -= 1
                elif num[left] + num[right] + num[index] < 0:
                    left += 1
                elif num[left] + num[right] + num[index] == 0:
                    if num[left] != preLeft or num[right] != preRight:
                        result.append([num[index], num[left], num[right]])
                    preLeft = num[left]
                    preRight = num[right]
                    left += 1
                    right -= 1
        return result

s = Solution()
num = [0, 0, 0]
print s.threeSum(num)
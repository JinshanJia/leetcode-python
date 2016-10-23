__author__ = 'Jia'
'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        dict = {}
        result = 0
        for i in num:
            if i in dict:
                continue
            length = 1
            dict[i] = length
            if i + 1 in dict:
                highest = i + dict[i + 1]
                lowest = i - dict[i] + 1
                length = highest - lowest + 1
                dict[highest] = length
                dict[lowest] = length
            if i - 1 in dict:
                lowest = i - dict[i - 1]
                highest = i + dict[i] - 1
                length = highest - lowest + 1
                dict[lowest] = length
                dict[highest] = length
            result = max(result, length)
        return result
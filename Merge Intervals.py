__author__ = 'Jia'
'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if intervals is None or len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals, key = lambda interval: interval.start)
        for i in intervals:
            print i.start, i.end
        result = [intervals[0]]
        index = 1
        while index < len(intervals):
            tmp = result.pop()
            result.extend(self.mergeTwoIntervals(tmp, intervals[index]))
            index += 1
        return result

    # i1's start must be smaller or equal to i2's start
    def mergeTwoIntervals(self, i1, i2):
        #cannot merge
        if i1.end < i2.start:
            return [i1, i2]
        # i1 larger than i2
        if i1.end >= i2.end:
            return [i1]
        return [Interval(i1.start, i2.end)]

s = Solution()
i1 = Interval(1, 4)
i2 = Interval(0, 4)
intervals = [i1, i2]
result = s.merge(intervals)
for i in result:
    print i.start, i.end
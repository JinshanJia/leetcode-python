__author__ = 'Jia'
'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if intervals is None or len(intervals) == 0:
            return [newInterval]
        intervals = sorted(intervals, key = lambda interval: interval.start)
        if newInterval.start < intervals[0].start:
            result = [newInterval]
            newInterval = None
            index = 0
        else:
            result = [intervals[0]]
            index = 1
        while index < len(intervals):
            tmp = result[-1]
            if newInterval is None:
                if tmp.end < intervals[index].start:
                    result.append(intervals[index])
                elif tmp.end < intervals[index].end:
                    tmp.end = intervals[index].end
            else:
                if newInterval.start >= intervals[index].start:
                    result.append(intervals[index])
                elif tmp.end < newInterval.start:
                    result.append(newInterval)
                    newInterval = None
                    index -= 1
                else:
                    tmp.end = max(tmp.end, newInterval.end)
                    newInterval = None
                    index -= 1
            index += 1
        if newInterval is not None:
            tmp = result[-1]
            if tmp.end < newInterval.start:
                result.append(newInterval)
            elif tmp.end < newInterval.end:
                tmp.end = newInterval.end
        return result


__author__ = 'Jia'
'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''
import collections
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        queue = collections.deque([1])
        count = 0
        while count < rowIndex:
            preSize = len(queue)
            while preSize > 1:
                out = queue.popleft()
                queue.append(out + queue[0])
                preSize -= 1
            queue.append(1)
            count += 1
        return list(queue)

s = Solution()
for i in range(10):
    print s.getRow(i)
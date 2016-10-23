__author__ = 'Jia'
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n <= 1:
            return 1
        index = 2
        pre1 = 1
        pre2 = 1
        curr = pre1 + pre2
        while index < n:
            pre1 = pre2
            pre2 = curr
            curr = pre1 + pre2
            index += 1
        return curr

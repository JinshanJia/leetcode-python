__author__ = 'Jia'
# Implement pow(x, n).

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 1:
            return x
        if n >= 0:
            return self.pow_helper(x, n)
        else:
            return 1 / self.pow_helper(x, -n)

    def pow_helper(self, x, n):
        if n == 0:
            return 1
        mid = n / 2
        v = self.pow_helper(x, mid)
        if mid * 2 == n:
            return v * v
        return v * v * x

s = Solution()
import datetime
t = datetime.datetime.now()
print s.pow(1, 20000000)
print datetime.datetime.now() - t
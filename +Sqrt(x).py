__author__ = 'Jia'
'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x <= 1:
            return x
        min = 0
        max = x
        while min < max - 1:
            mid = min + (max - min) / 2
            result = x / mid
            if result == mid:
                return mid
            elif result < mid:
                max = mid
            else:
                min = mid
        return min

    def sqrt2(self, x):
        if x <= 1:
            return x
        half = x / 2.
        while int(half) != int(x / half):
            half = (half + x / half) / 2
        return int(half)

s = Solution()
print s.sqrt2(17)
__author__ = 'Jia'
'''
Divide two integers without using multiplication, division and mod operator.
'''
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0:
            return
        absDividend = abs(dividend)
        absDivisor = abs(divisor)
        if absDividend < absDivisor:
            return 0
        count = 0
        current = 1
        while absDividend >= absDivisor:
            absDividend -= absDivisor
            absDivisor <<= 1
            count += current
            current <<= 1
        while current > 0 and absDividend > 0:
            while absDividend < absDivisor:
                current >>= 1
                absDivisor >>= 1
            absDividend -= absDivisor
            count += current

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return count
        else:
            return -count


s = Solution()
print s.divide(10, 6)
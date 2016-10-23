__author__ = 'Jia'
'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        carry = 0
        index = 0
        result = []
        while index < len(a) and index < len(b):
            num1 = int(a[len(a) - 1 - index])
            num2 = int(b[len(b) - 1 - index])
            tmp = num1 + num2 + carry
            result.append(str(tmp % 2))
            carry = tmp / 2
            index += 1
        while index < len(a):
            num1 = int(a[len(a) - 1 - index])
            tmp = num1 + carry
            result.append(str(tmp % 2))
            carry = tmp / 2
            index += 1
        while index < len(b):
            num1 = int(b[len(b) - 1 - index])
            tmp = num1 + carry
            result.append(str(tmp % 2))
            carry = tmp / 2
            index += 1
        if carry == 1:
            result.append(str(1))
        result.reverse()
        return ''.join(result)

s = Solution()
print s.addBinary('10', '110')
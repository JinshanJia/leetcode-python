__author__ = 'Jia'
'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        result = []
        index = 0
        carry = 0
        if digits is None or len(digits) == 0:
            return [1]
        digits[-1] += 1
        while index < len(digits):
            digits[len(digits) - 1 - index] += carry
            if digits[len(digits) - 1 - index] >= 10:
                carry = 1
                digits[len(digits) - 1 - index] -= 10
            else:
                carry = 0
                break
            index += 1
        if carry == 1:
            result.append(1)
        result.extend(digits)
        return result

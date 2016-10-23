__author__ = 'Jia'
'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @return a string
    def intToRoman(self, num):
        baseNumber = [1000, 500, 100, 50, 10, 5, 1]
        baseCharacter = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        result = ""
        i = 0
        while num > 0 and i < len(baseNumber):
            remaining = num / baseNumber[i]
            num -= remaining * baseNumber[i]
            if remaining == 9:
                result += baseCharacter[i] + baseCharacter[i - 2]
                continue
            if remaining == 4:
                result += baseCharacter[i] + baseCharacter[i - 1]
                continue
            if remaining >= 5:
                result += baseCharacter[i - 1]
                remaining -= 5
            while remaining > 0:
                result += baseCharacter[i]
                remaining -= 1
            i += 2
        return result

s = Solution()
print s.intToRoman(1990)
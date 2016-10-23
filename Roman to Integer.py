__author__ = 'Jia'
'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution:
    # @return an integer
    def romanToInt(self, s):
        baseCharacter = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        pre = 0
        result = 0
        for i in range(len(s) - 1, -1, -1):
            current = baseCharacter[s[i]]
            if current >= pre:
                result += current
            else:
                result -= current
            pre = current
        return result

s = Solution()
print s.romanToInt("MCMXC")
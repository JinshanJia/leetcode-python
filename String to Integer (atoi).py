__author__ = 'Jia'
'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what
are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather
all the input requirements up front.

###################
Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is
found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no
effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of
representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

'''
class Solution:
    INT_MAX = 2147483647
    # @return an integer
    def atoi(self, str):
        if str is None:
            return 0
        isNegative = False
        result = 0
        index = 0
        while index < len(str) and str[index] == " ":
            index += 1
        if index >= len(str):
            return 0
        if str[index] == "-":
            isNegative = True
            index += 1
        elif str[index] == "+":
            isNegative = False
            index += 1
        if index >= len(str):
            return 0
        for c in str[index:]:
            if not c.isdigit():
                return result if not isNegative else -1 * result
            result = result * 10 + int(c)
            if result > self.INT_MAX:
                return self.INT_MAX if not isNegative else -1 - self.INT_MAX
        return result if not isNegative else -1 * result





s = Solution()
l = [None, "  1", "  +1a", "  -20 ", "+0", "-0", "10101010101010101011010101010101010101010101010101010110101010101010101010101010101010101101010101010101010101010101010101011010101010101010"]


for string in l:
    print s.atoi(string)
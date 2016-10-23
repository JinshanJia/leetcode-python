__author__ = 'Jia'
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if s is None or len(s) == 0:
            return 0
        prepre = 1
        pre = 0 if s[-1] == '0' else 1
        result = pre
        index = len(s) - 2
        while index >= 0:
            if s[index] == '0':
                result = 0
            elif s[index] > '2' or (s[index] == '2' and s[index + 1] > '6'):
                result = pre
            else:
                result = pre + prepre
            prepre = pre
            pre = result
            index -= 1
        return result

s = Solution()
print s.numDecodings("1234")
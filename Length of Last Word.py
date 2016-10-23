__author__ = 'Jia'
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word
in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
'''
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s is None or len(s) == 0:
            return 0
        count = 0
        index = len(s) - 1
        while index >= 0 and s[index] == ' ':
            index -= 1
        while index >= 0 and s[index] != ' ':
            index -= 1
            count += 1
        return count

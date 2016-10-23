__author__ = 'Jia'
'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
'''
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        result = []
        index = len(s) - 1
        while index >= 0:
            if s[index] == ' ':
                index -= 1
                continue
            currIndex = index
            while currIndex >= 0 and s[currIndex] != ' ':
                currIndex -= 1
            result.append(s[currIndex + 1:index + 1])
            index = currIndex - 1
        return ' '.join(result)
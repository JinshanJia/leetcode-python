#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jia'

'''
Implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        pIndex = len(p) - 1
        sIndex = len(s) - 1
        while pIndex >= 0 and sIndex >= 0 and p[pIndex] != '*':
            if p[pIndex] != '.' and s[sIndex] != p[pIndex]:
                return False
            pIndex -= 1
            sIndex -= 1
        s = s[:sIndex + 1]
        p = p[:pIndex + 1]
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1:
            return len(s) == 1 and (p[0] == '.' or s[0] == p[0])
        if p[1] != '*':
            return len(s) != 0 and (p[0] == '.' or s[0] == p[0]) and self.isMatch(s[1:], p[1:])
        index = 0
        while index < len(s) and (s[index] == p[0] or p[0] == '.'):
            if self.isMatch(s[index:], p[2:]):
                return True
            index += 1
        return self.isMatch(s[index:], p[2:])



so = Solution()
print so.isMatch('aaa', 'ab*ac*a')

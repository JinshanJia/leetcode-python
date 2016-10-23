__author__ = 'Jia'
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution:
    # @return a boolean
    def isValid(self, s):
        if s is None or len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False

        stack = []
        d = {'(': ')', '[': ']', '{': '}'}

        for c in s[:]:
            if c in d:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                start = stack.pop()
                if d[start] != c:
                    return False
        return len(stack) == 0

s = Solution()
print s.isValid("((({{[]}})))")
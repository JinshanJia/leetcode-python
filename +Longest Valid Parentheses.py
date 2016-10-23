__author__ = 'Jia'
'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if s is None:
            return 0
        stack = []
        last = -1
        result = 0
        index = 0
        while index < len(s):
            if s[index] == "(":
                stack.append(index)
            elif len(stack) != 0:
                stack.pop()
                if len(stack) == 0:
                    result = max(result, index - last)
                else:
                    result = max(result, index - stack[-1])
            else:
                last = index
            index += 1
        return result


s = Solution()
print s.longestValidParentheses("(()")
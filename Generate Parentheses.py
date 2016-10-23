__author__ = 'Jia'
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n <= 0:
            return [""]
        result = []
        tmp = ["("]
        leftnums = [1]
        while len(tmp) != 0:
            s = tmp.pop()
            num = leftnums.pop()
            if len(s) == 2 * n:
                result.append(s)
            elif num == n:
                s += ")"
                tmp.append(s)
                leftnums.append(num)
            elif num * 2 == len(s):
                s += "("
                tmp.append(s)
                leftnums.append(num + 1)
            else:
                a = s + "("
                tmp.append(a)
                leftnums.append(num + 1)
                b = s + ")"
                tmp.append(b)
                leftnums.append(num)
        return result

s = Solution()
print s.generateParenthesis(4)
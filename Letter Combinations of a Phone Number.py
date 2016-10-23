__author__ = 'Jia'
'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z'],
                 '0': [' ']}
        result = [""]
        if digits is None:
            return result
        tmp = []
        for d in digits:
            for l in result:
                for c in phone[d]:
                    s = l + c
                    tmp.append(s)
            result = tmp
            tmp = []
        return result

s = Solution()
print s.letterCombinations("22")
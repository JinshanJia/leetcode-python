__author__ = 'Jia'
'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid
dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''
import sets
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        # dp[i] stores the result of s[i:], it is a list of lists of integers,
        # wich means after which index to insert space
        dp = [[] for i in range(len(s) + 1)]
        dp[-1] = [[]]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i : j + 1] in dict:
                    for l in dp[j + 1]:
                        tmp = [j]
                        tmp.extend(l)
                        dp[i].append(tmp)

        result = []
        for l in dp[0]:
            pre = 0
            tmp = []
            for i in l:
                tmp.append(s[pre:i + 1])
                pre = i + 1
            result.append(' '.join(tmp))
        return result

s = Solution()
string = "ab"
dict = sets.Set(["a", "b"])
print s.wordBreak(string, dict)
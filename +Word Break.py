__author__ = 'Jia'
'''
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one
or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        #dp[i][j] means s[i:j + 1] whether can be segmented
        dp = [[None for j in range(len(s))] for i in range(len(s))]

        def wordBreakRec(s, i, j):
            if dp[i][j] is not None:
                return dp[i][j]
            if s[i:j + 1] in dict:
                dp[i][j] = True
                return True
            if i == j:
                dp[i][j] = s[i] in dict
                return dp[i][j]
            for index in range(i, j):
                if wordBreakRec(s, i, index) and wordBreakRec(s, index + 1, j):
                    dp[i][j] = True
                    return True
            dp[i][j] = False
            return False
        return wordBreakRec(s, 0, len(s) - 1)

    def wordBreak2(self, s, dict):
        result = [False] * (len(s) + 1)
        result[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(result)):
                result[i] = s[i:j] in dict and result[j]
                if result[i]:
                    break
        print result
        return result[0]

s = Solution()
string = 'a'
dict = {}
print s.wordBreak2(string, dict)
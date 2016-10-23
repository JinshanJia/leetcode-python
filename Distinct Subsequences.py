__author__ = 'Jia'
'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of
"ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        # dp[i][j] means the distinct subsequences number of T[i:] and S[j:]
        dp = [[0 for j in range(len(S) + 1)] for i in range(len(T) + 1)]
        for j in range(len(S) + 1):
            dp[-1][j] = 1
        for i in range(len(T)):
            dp[i][-1] = 0
        for i in range(len(T) - 1, -1, -1):
            for j in range(len(S) - 1, -1, -1):
                if S[j] == T[i]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
        return dp[0][0]

__author__ = 'Jia'
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # dp[i][j] means whether s[i][j + 1] is palindrome
        dp = [[False for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s) - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
        for i in range(len(s) - 3, -1, -1):
            for j in range(i + 2, len(s)):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
        # cut[i] means the minimum number of cuts for s[:i + 1]
        cut = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if dp[0][i]:
                continue
            cut[i] = i
            for j in range(i):
                if dp[j + 1][i]:
                    cut[i] = min(cut[i], cut[j] + 1)
        return cut[len(s) - 1]

s = Solution()
print s.minCut('cdd')
__author__ = 'Jia'
'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        # dp[i][j] means whether s3[i + j:] is interleaving of s1[i:] s2[j:]
        dp = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        dp[-1][-1] = True
        for i in range(len(s1) - 1, -1, -1):
            dp[i][-1] = dp[i + 1][-1] and s3[len(s2) + i] == s1[i]
        for j in range(len(s2) - 1, -1, -1):
            dp[-1][j] = dp[-1][j + 1] and s3[len(s1) + j] == s2[j]
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s3[i + j] == s1[i]:
                    if dp[i + 1][j]:
                        dp[i][j] = True
                if s3[i + j] == s2[j]:
                    if dp[i][j + 1]:
                        dp[i][j] = True
        return dp[0][0]

s = Solution()
s1 = "a"
s2 = "b"
s3 = "a"
print s.isInterleave(s1, s2, s3)

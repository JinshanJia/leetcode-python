__author__ = 'Jia'
'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''
class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        # dp[i][j][k] means whether s1[i: i + k] and s2[j: j + k] is scramble
        dp = [[[None for k in range(len(s1) + 1)] for j in range(len(s1))] for i in range(len(s1))]
        return self.isScrambleRec(s1, 0, s2, 0, len(s1), dp)

    def isScrambleRec(self, s1, s1start, s2, s2start, length, dp):
        if dp[s1start][s2start][length] is not None:
            return dp[s1start][s2start][length]
        if length == 1:
            dp[s1start][s2start][length] = s1[s1start] == s2[s2start]
            return dp[s1start][s2start][length]
        dp[s1start][s2start][length] = False
        for partition in range(1, length):
            if self.isScrambleRec(s1, s1start + partition, s2, s2start + partition, length - partition, dp) and \
                    self.isScrambleRec(s1, s1start, s2, s2start, partition, dp):
                dp[s1start][s2start][length] = True
                break
            if self.isScrambleRec(s1, s1start + partition, s2, s2start, length - partition, dp) and \
                    self.isScrambleRec(s1, s1start, s2, s2start + length - partition, partition, dp):
                dp[s1start][s2start][length] = True
                break
        return dp[s1start][s2start][length]

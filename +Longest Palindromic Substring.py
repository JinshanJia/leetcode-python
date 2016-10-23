__author__ = 'Jia'
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
# and there exists one unique longest palindromic substring.

class Solution:
    # @return a string
    def longestPalindrome_DP(self, s):
        #isP[i][j] means s[j:i + 1] is palindrome
        isP = [[False for j in range(len(s))] for j in range(len(s))]

        for i in range(len(s) - 1):
            isP[i][i] = True
            isP[i + 1][i] = True if s[i] == s[i + 1] else False
        isP[len(s) - 1][len(s) - 1] = True
        for i in range(2, len(s)):
            for j in range(i - 2, -1, -1):
                if isP[i - 1][j + 1] and s[i] == s[j]:
                    isP[i][j] = True
        list = [0, -1]

        for i in range(len(s)):
            for j in range(i + 1):
                if isP[i][j] and i - j > list[1] - list[0]:
                    list = [j, i]

        return s[list[0]:list[1] + 1]

    def longestPalindrome(self, s):
        result = ""
        for i in range(len(s) - 1):
            temp1 = self.expandFromCenter(s, i, i)
            if len(result) < len(temp1):
                result = temp1
            temp2 = self.expandFromCenter(s, i, i + 1)
            if len(result) < len(temp2):
                result = temp2
        temp1 = self.expandFromCenter(s, len(s) - 1, len(s) - 1)
        if len(result) < len(temp1):
            result = temp1
        return result

    def expandFromCenter(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

s = Solution()
string = "aabbb"
print string
print s.longestPalindrome(string)
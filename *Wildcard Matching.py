__author__ = 'Jia'
'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false
'''

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        # dp[i][j] means whether s[i:] p[j:] matches
        dp = [
            [False for j in range(len(p) + 1)] for i in range(len(s) + 1)
            ]
        dp[-1][-1] = True
        for j in range(len(p) - 1, -1, -1):
            dp[-1][j] = dp[-1][j + 1] and p[j] == '*'

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(p) - 1, -1, -1):
                if p[j] != '*':
                    if p[j] == s[i] or p[j] == '?':
                        dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp[i + 1][j] or dp[i][j + 1]
        return dp[0][0]

    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch2(self, s, p):
        sIndex = len(s) - 1
        pIndex = len(p) - 1
        while sIndex >= 0 and pIndex >= 0 and p[pIndex] != '*':
            if s[sIndex] != p[pIndex] and p[pIndex] != '?':
                return False
            sIndex -= 1
            pIndex -= 1
        if sIndex < 0 or pIndex < 0:
            return sIndex == pIndex
        pLength = 0
        index = 0
        while index <= pIndex:
            if p[pIndex] != '*':
                pLength += 1
            index += 1
        return self.isMatchRec(s[:sIndex + 1], p[:pIndex + 1], pLength)

    d1 = {}
    d2 = {}
    def isMatchRec(self, s, p, pLength):
        if len(p) == 0:
            return len(s) == 0
        if pLength > len(s):
            return False
        pIndex = 0
        while pIndex < len(p) and p[pIndex] != '*':
            if pIndex >= len(s) or (s[pIndex] != p[pIndex] and p[pIndex] != '?'):
                return False
            pLength -= 1
            pIndex += 1
        index = pIndex
        pIndex += 1
        while pIndex < len(p) and p[pIndex] == '*':
            pIndex += 1
        if pIndex == len(p):
            return True
        while index < len(s):
            hash = str(str(s[index:] + p[pIndex:]).__hash__())
            self.d1[hash] = s[index:] + p[pIndex:]
            if hash in self.d2.keys():
                self.d2[hash] += 1
            else:
                self.d2[hash] = 1
            if self.isMatchRec(s[index:], p[pIndex:], pLength):
                return True
            index += 1
        print "*********"
        print self.d1
        print "d2"
        print self.d2
        print "*********"
        return self.isMatchRec(s[index:], p[pIndex:], pLength)




s = Solution()
print s.isMatch("abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb", "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb")
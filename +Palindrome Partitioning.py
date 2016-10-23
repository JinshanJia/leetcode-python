__author__ = 'Jia'
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
'''
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # dp[i][j] means whether s[i:j + 1] is palindrome or not
        dp = [[False for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s) - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
        for i in range(len(s) - 3, -1, -1):
            for j in range(i + 2, len(s)):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
        resultArray = [None for i in range(len(s) + 1)]
        resultArray[len(s)] = [[]]

        def generateResult(index):
            if resultArray[index] is not None:
                return resultArray[index]
            result = []
            for j in range(index, len(s)):
                if dp[index][j]:
                    tmp = generateResult(j + 1)
                    for l in tmp:
                        r = [s[index: j + 1]]
                        r.extend(l)
                        result.append(r)
            resultArray[index] = result
            return resultArray[index]

        return generateResult(0)

s = Solution()
print s.partition('a')
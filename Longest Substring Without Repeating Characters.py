__author__ = 'Jia'
# Given a string, find the length of the longest substring without repeating characters. For example, the longest
# substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest
# substring is "b", with the length of 1.

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        d = {}
        result = 0
        temp = 0
        prePoint = 0
        for i in range(len(s)):
            if s[i] in d:
                result = max(result, temp)
                t = d[s[i]]
                for j in range(prePoint, t + 1):
                    del d[s[j]]
                    temp -= 1
                prePoint = t + 1
            d[s[i]] = i
            temp += 1
        return max(result, temp)

s = Solution()
string = "bbbbb"
print s.lengthOfLongestSubstring(string)
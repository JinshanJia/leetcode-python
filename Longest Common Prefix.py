__author__ = 'Jia'
'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs is None or len(strs) == 0:
            return ""
        shortest = strs[0]
        for s in strs:
            if len(s) < len(shortest):
                shortest = s
        for s in strs:
            shortest = self.commonPrefix(s, shortest)
        return shortest

    def commonPrefix(self, s1, s2):
        s = ""
        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                return s
            s += s1[i]
        return s

s = Solution()
strs = ['asdfg','asdfgadsf','asdfgafewf']
print s.longestCommonPrefix(strs)
__author__ = 'Jia'
'''
Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
'''
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if needle is None or haystack is None:
            return None
        if len(needle) > len(haystack):
            return None
        if len(needle) == 0:
            return haystack
        index = 0
        while index < len(haystack) - len(needle) + 1:
            i = 0
            while i < len(needle) and haystack[index + i] == needle[i]:
                i += 1
            if i == len(needle):
                return haystack[index:]
            index += 1
        return None

s = Solution()
haystack = "bab"
needle = "a"
print s.strStr(haystack, needle)
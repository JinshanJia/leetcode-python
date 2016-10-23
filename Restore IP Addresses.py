__author__ = 'Jia'
'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        result = []
        for i in range(min(len(s), 3)):
            si = s[:i + 1]
            if not self.isValidIP(si):
                continue
            for j in range(i + 1, min(len(s), i + 1 + 3)):
                sj = s[i + 1:j + 1]
                if not self.isValidIP(sj):
                    continue
                for k in range(j + 1, min(len(s), j + 1 + 3)):
                    sk = s[j + 1:k + 1]
                    sr = s[k + 1:]
                    if self.isValidIP(sk) and self.isValidIP(sr):
                        result.append(si + '.' + sj + '.' + sk + '.' + sr)
        return result

    def isValidIP(self, s):
        if s is None or len(s) == 0:
            return False
        if s[0] == '0' and len(s) != 1:
            return False
        return int(s) <= 255

s = Solution()
print s.restoreIpAddresses("1010101")
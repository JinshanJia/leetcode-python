__author__ = 'Jia'
'''
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of
substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if S is None or L is None or len(S) == 0 or len(L) == 0:
            return []
        length = len(L[0])
        total = len(L) * length
        orignalDict = {}
        self.setDict(orignalDict, L)
        result = []
        for i in range(length):
            index = i
            tempDict = dict(orignalDict)
            while len(tempDict) != 0 and index <= len(S) - total:
                currentIndex = index
                while currentIndex <= len(S) - length:
                    tmpS = S[currentIndex:currentIndex + length]
                    if tmpS in tempDict.keys():
                        self.minusElement(tempDict, tmpS)
                        currentIndex += length
                        if len(tempDict) == 0:
                            result.append(index)
                    elif tmpS in orignalDict.keys():
                        while S[index:index + length] != tmpS:
                            self.addElement(tempDict, S[index:index + length])
                            index += length
                        self.addElement(tempDict, tmpS)
                        index += length
                    else:
                        index = currentIndex + length
                        tempDict = dict(orignalDict)
                        break
        return result

    def addElement(self, d, s):
        if s in d.keys():
            d[s] += 1
        else:
            d[s] = 1

    def minusElement(self, d, s):
        if d[s] != 1:
            d[s] -= 1
        else:
            d.__delitem__(s)

    def setDict(self, d, l):
        for s in l:
            if s in d.keys():
                d[s] += 1
            else:
                d[s] = 1

s = Solution()
print s.findSubstring("abababab", ["a","b","a"])

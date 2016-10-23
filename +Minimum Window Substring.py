__author__ = 'Jia'
'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity
O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''

class Solution:
    # @return a string
    def minWindow(self, S, T):
        tTable = {}
        for c in T[:]:
            if c in tTable:
                tTable[c] += 1
            else:
                tTable[c] = 1
        hasFound = {}
        count = 0
        left = 0
        right = 0
        result = S
        while right < len(S):
            c = S[right]
            if c in tTable:
                if c in hasFound and hasFound[c] >= tTable[c]:
                    hasFound[c] += 1
                elif c in hasFound:
                    count += 1
                    hasFound[c] += 1
                else:
                    count += 1
                    hasFound[c] = 1
            if count == len(T):
                while left <= right:
                    c = S[left]
                    if c not in tTable:
                        left += 1
                    elif hasFound[c] > tTable[c]:
                        hasFound[c] -= 1
                        left += 1
                    else:
                        break
                if right - left + 1 < len(result):
                    result = S[left:right + 1]
            right += 1
        if count < len(T):
            return ""
        return result


__author__ = 'Jia'
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 0 or nRows == 1 or nRows >= len(s):
            return s
        result = ""
        index = 0
        # line 0
        while index < len(s):
            result += s[index]
            index += nRows * 2 - 2
        for i in range(1, nRows - 1):
            index = i
            count = 0
            while index < len(s):
                result += s[index]
                if count % 2 == 0:
                    index += nRows - 1 - i + nRows - 2 - (i - 1)
                else:
                    index += i + i
                count += 1
        index = nRows - 1
        # line nRows - 1
        while index < len(s):
            result += s[index]
            index += nRows * 2 - 2
        return result

s = Solution()
print s.convert("PAYPALISHIRING", 2)
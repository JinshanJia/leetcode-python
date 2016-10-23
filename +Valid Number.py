__author__ = 'Jia'
'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before
implementing one.
considered:
+
-
1.0
0.1
2e+3.0
2e3
2.+2


Cases that failed
" "
"3."
".1"
"."
". 1"
"+.8"
"1 4"
'''
import re

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        if s is None:
            return False
        return re.match("[\+\-]?(\.[0-9]+|[0-9]+\.|[0-9]+\.[0-9]+|[0-9]+)([eE][\+\-]?[0-9]+)?$", s.strip()) is not None

s = Solution()
print s.isNumber("2e2")
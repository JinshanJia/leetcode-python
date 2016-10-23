__author__ = 'Jia'
'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''
class Solution:
    # @return a string
    def countAndSay(self, n):
        if n <= 0:
            return ""
        return self.countAndSayRec(n)

    def countAndSayRec(self, n):
        if n == 1:
            return "1"
        preResult = self.countAndSayRec(n - 1)
        pre = preResult[0]
        count = 1
        index = 1
        result = ""
        while index < len(preResult):
            if pre != preResult[index]:
                result += str(count) + pre
                pre = preResult[index]
                count = 1
            else:
                count += 1
            index += 1

        result += str(count) + pre
        return result

s = Solution()
for i in range(8):
    print s.countAndSay(i)
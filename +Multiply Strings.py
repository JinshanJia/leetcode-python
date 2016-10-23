__author__ = 'Jia'
'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply2(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        l1 = []
        l2 = []
        for i in range(-1, -len(num1) - 1, -1):
            l1.append(int(num1[i]))
        for i in range(-1, -len(num2) - 1, -1):
            l2.append(int(num2[i]))

        r = [0 for i in range(len(num1) + len(num2))]

        for i in range(len(num1)):
            for j in range(len(num2)):
                r[i + j] += l1[i] * l2[j]
        result = ""
        for i in range(len(r) - 1):
            result = str(r[i] % 10) + result
            r[i + 1] += r[i] / 10
        result = str(r[-1]) + result if r[-1] != 0 else result
        return result


    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if len(num1) < len(num2):
            return self.multiply(num2, num1)
        result = ""
        index = -1
        while -index <= len(num2):
            mul = self.oneNumbermultiply(num1, int(num2[index]), -index - 1)
            result = self.add(result, mul)
            index -= 1
        return result


    def add(self, num1, num2):
        length = min(len(num1), len(num2))
        index = -1
        carry = 0
        result = ""
        while -index <= length:
            tmp = int(num1[index]) + int(num2[index]) + carry
            add = tmp % 10
            carry = tmp / 10
            result = str(add) + result
            index -= 1
        while -index <= len(num1):
            tmp = int(num1[index]) + carry
            add = tmp % 10
            carry = tmp / 10
            result = str(add) + result
            index -= 1
        while -index <= len(num2):
            tmp = int(num2[index]) + carry
            add = tmp % 10
            carry = tmp / 10
            result = str(add) + result
            index -= 1
        if carry != 0:
            result = str(carry) + result
        return result

    def oneNumbermultiply(self, num1, oneNum, zeroNum):
        carry = 0
        result = ""
        for c in num1:
            currNum = int(c)
            tmp = currNum * oneNum + carry
            mul = tmp % 10
            carry = tmp / 10
            result = str(mul) + result
        if carry != 0:
            result = str(carry) + result
        for i in range(zeroNum):
            result += '0'
        return result

s = Solution()
num1 = "1"
num2 = "10"
print s.multiply2(num1, num2)

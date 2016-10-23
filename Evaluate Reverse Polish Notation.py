__author__ = 'Jia'
'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
import sets
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        set = sets.Set(['+', '-', '*', '/'])
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in set:
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                result = self.calculate(num1, num2, tokens[i])
                stack.append(result)
        return stack[-1]

    def calculate(self, num1, num2, operation):
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        else:
            possitive = 1
            if num1 * num2 < 0:
                possitive = -1
            return abs(num1) / abs(num2) * possitive

s = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print s.evalRPN(tokens)
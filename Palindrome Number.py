__author__ = 'Jia'
'''
Determine whether an integer is a palindrome. Do this without extra space.

#########################

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

'''
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        digit = 0
        tmp = x
        while tmp != 0:
            tmp /= 10
            digit += 1
        while digit > 1:
            if x % 10  != x / (10 ** (digit - 1)) % 10:
                return False
            x /= 10
            digit -= 2
        return True

s = Solution()
print s.isPalindrome(10)

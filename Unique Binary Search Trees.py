__author__ = 'Jia'
'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

class Solution:
    # @return an integer
    def numTrees(self, n):
        list = [1 for i in range(n + 1)]
        if n <= 1:
            return 1
        index = 2
        while index <= n:
            result = 0
            for i in range(index):
                result += list[index - 1 - i] * list[i]
            list[index] = result
            index += 1
        return list[-1]
s = Solution()
print s.numTrees(4)
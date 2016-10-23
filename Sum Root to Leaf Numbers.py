__author__ = 'Jia'
'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):

        def sumNumbersRec(root, preValue):
            preValue = preValue * 10 + root.val
            if root.left is None and root.right is None:
                return preValue
            result = 0
            if root.right is not None:
                result += sumNumbersRec(root.right, preValue)
            if root.left is not None:
                result += sumNumbersRec(root.left, preValue)
            return result
        if root is None:
            return 0
        return sumNumbersRec(root, 0)
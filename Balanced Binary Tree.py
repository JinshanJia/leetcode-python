__author__ = 'Jia'
'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.isBalancedRec(root) != -1

    def isBalancedRec(self, root):
        if root is None:
            return 0
        left = self.isBalancedRec(root.left)
        right = self.isBalancedRec(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1



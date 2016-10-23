__author__ = 'Jia'
'''
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3

Return 6.
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
    def maxPathSum(self, root):
        return self.maxPathSumRec(root)[2]

    # @return [left, right, currentMax] results
    def maxPathSumRec(self, root):
        if root is None:
            return [0, 0, -2147483648]
        leftList = self.maxPathSumRec(root.left)
        rightList = self.maxPathSumRec(root.right)
        left = max(0, leftList[0], leftList[1])
        right = max(0, rightList[0], rightList[1])
        result = max(left + right + root.val, leftList[2], rightList[2])
        return [left + root.val, right + root.val, result]

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(-3)

s = Solution()
print s.maxPathSum(tree)
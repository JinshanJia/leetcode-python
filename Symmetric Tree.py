__author__ = 'Jia'
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
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
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetricRec(root.left, root.right)

    def isSymmetricRec(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        return self.isSymmetricRec(left.left, right.right) and self.isSymmetricRec(left.right, right.left)

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)

tree.right = TreeNode(2)
tree.right.right = TreeNode(3)
# tree.right.left = TreeNode(4)

s = Solution()
print s.isSymmetric(TreeNode(1))
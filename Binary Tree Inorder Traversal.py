__author__ = 'Jia'
'''
Given a binary tree, return the inorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
  1
    \
     2
    /
   3

return [1,3,2].
Note: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result = []
        l = []
        self.add(root, l)
        while len(l) != 0:
            node = l.pop()
            result.append(node.val)
            self.add(node.right, l)
        return result

    def add(self, root, l):
        while root is not None:
            l.append(root)
            root = root.left

tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
s = Solution()
print s.inorderTraversal(tree)
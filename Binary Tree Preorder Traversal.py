__author__ = 'Jia'
'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
 1
    \
     2
    /
   3

return [1,2,3].

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
    def preorderTraversal(self, root):
        if root is None:
            return []
        result = []
        toTraversal = [root]
        while len(toTraversal) > 0:
            node = toTraversal.pop()
            result.append(node.val)
            if node.right is not None:
                toTraversal.append(node.right)
            if node.left is not None:
                toTraversal.append(node.left)
        return result

tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
s = Solution()
print s.preorderTraversal(tree)
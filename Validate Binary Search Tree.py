__author__ = 'Jia'
'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
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
    def isValidBST(self, root):
        return self.inorder(root)

    def inorder(self, root):
        l = []
        pre = -2147483648
        self.add(root, l)
        while len(l) != 0:
            node = l.pop()
            if node.val <= pre:
                return False
            if node.right is not None:
                self.add(node.right, l)
            pre = node.val
        return True

    def add(self, root, l):
        while root is not None:
            l.append(root)
            root = root.left


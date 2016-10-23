__author__ = 'Jia'
'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return self.buildTreeRec(preorder, 0, inorder, 0, len(preorder))

    def buildTreeRec(self, preorder, preIndex, inorder, inIndex, length):
        if length <= 0:
            return
        root = TreeNode(preorder[preIndex])
        index = inIndex
        while index < inIndex + length and inorder[index] != root.val:
            index += 1
        leftLength = index - inIndex
        rightLength = length - leftLength - 1
        root.left = self.buildTreeRec(preorder, preIndex + 1, inorder, inIndex, leftLength)
        root.right = self.buildTreeRec(preorder, preIndex + 1 + leftLength, inorder, index + 1, rightLength)
        return root

s = Solution()
inorder = [1, 3, 2]
preorder = [1, 2, 3]
postorder = [3, 2, 1]
tree = s.buildTree(preorder, inorder)

def inorder(tree, l):
    if tree is None:
        return
    inorder(tree.left, l)
    l.append(tree.val)
    inorder(tree.right, l)

print "in order"
l = []
inorder(tree, l)
print l


def preorder(tree, l):
    if tree is None:
        return
    l.append(tree.val)
    preorder(tree.left, l)
    preorder(tree.right, l)

print "preorder"
l = []
preorder(tree, l)
print l


def postorder(tree, l):
    if tree is None:
        return
    postorder(tree.left, l)
    postorder(tree.right, l)
    l.append(tree.val)

print "postorder"
l = []
postorder(tree, l)
print l
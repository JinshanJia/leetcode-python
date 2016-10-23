__author__ = 'Jia'
'''
Given inorder and postorder traversal of a tree, construct the binary tree.

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
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        return self.buildTreeRec(inorder, 0, postorder, 0, len(inorder))

    def buildTreeRec(self, inorder, inStartIndex, postorder, postStartIndex, length):
        if length == 0:
            return
        root = TreeNode(postorder[postStartIndex + length - 1])
        index = inStartIndex
        while index < inStartIndex + length and inorder[index] != root.val:
            index += 1
        leftLength = index - inStartIndex
        rightLength = length - leftLength - 1
        root.left = self.buildTreeRec(inorder, inStartIndex, postorder, postStartIndex, leftLength)
        root.right = self.buildTreeRec(inorder, index + 1, postorder, postStartIndex + leftLength, rightLength)
        return root

s = Solution()
inorder = [1, 3, 2]
preorder = [1, 2, 3]
postorder = [3, 2, 1]
tree = s.buildTree(inorder, postorder)

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
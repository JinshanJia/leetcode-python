__author__ = 'Jia'
'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.generateTreesRec(1, n)

    def generateTreesRec(self, start, end):
        if start > end:
            return [None]
        if start == end:
            tree = TreeNode(start)
            return [tree]
        result = []
        for i in range(start, end + 1):
            leftList = self.generateTreesRec(start, i - 1)
            rightList = self.generateTreesRec(i + 1, end)
            for leftTree in leftList:
                for rightTree in rightList:
                    tree = TreeNode(i)
                    tree.right = rightTree
                    tree.left = leftTree
                    result.append(tree)
        return result

s = Solution()

def inorder(tree, l):
    if tree is None:
        return
    inorder(tree.left, l)
    l.append(tree.val)
    inorder(tree.right, l)

trees = s.generateTrees(3)
print "in order"
for tree in trees:
    l = []
    inorder(tree, l)
    print l

def preorder(tree, l):
    if tree is None:
        return
    l.append(tree.val)
    preorder(tree.left, l)
    preorder(tree.right, l)
print "preorder order"
for tree in trees:
    l = []
    preorder(tree, l)
    print l

def postorder(tree, l):
    if tree is None:
        return
    postorder(tree.left, l)
    postorder(tree.right, l)
    l.append(tree.val)

print "post order"
for tree in trees:
    l = []
    postorder(tree, l)
    print l
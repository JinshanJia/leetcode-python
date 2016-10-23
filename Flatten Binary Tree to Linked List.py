__author__ = 'Jia'
'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.flattenRec(root)

    def flattenRec(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return root
        tmpRight = root.right
        rightEnd = self.flattenRec(tmpRight)
        if root.left is not None:
            leftEnd = self.flattenRec(root.left)
            root.right = root.left
            root.left = None
            leftEnd.right = tmpRight
        return leftEnd if rightEnd is None else rightEnd

s = Solution()
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(5)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.right = TreeNode(6)
s.flatten(tree)

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
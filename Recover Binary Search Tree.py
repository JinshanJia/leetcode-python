__author__ = 'Jia'
'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.inorder(root)
        return root

    def inorder(self, root):
        firstSwapNode = None
        secondSwapNode = None
        l = []
        preNode = None
        self.add(root, l)
        while len(l) != 0:
            node = l.pop()
            if preNode is not None and preNode.val > node.val:
                if firstSwapNode is None:
                    firstSwapNode = preNode
                secondSwapNode = node
            self.add(node.right, l)
            preNode = node

        tmp = firstSwapNode.val
        firstSwapNode.val = secondSwapNode.val
        secondSwapNode.val = tmp


    def add(self, root, l):
        while root is not None:
            l.append(root)
            root = root.left



def inorder(tree, l):
    if tree is None:
        return
    inorder(tree.left, l)
    l.append(tree.val)
    inorder(tree.right, l)

s = Solution()
tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
l = []
inorder(tree, l)
print l
tree = s.recoverTree(tree)

l = []
inorder(tree, l)
print l
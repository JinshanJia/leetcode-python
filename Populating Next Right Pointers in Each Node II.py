__author__ = 'Jia'
'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is not None:
            self.connectRec(root)

    def connectRec(self, root):
        next = None
        current = None
        while root is not None:
            if root.left is not None:
                if next is None:
                    next = root.left
                if current is not None:
                    current.next = root.left
                current = root.left
            if root.right is not None:
                if next is None:
                    next = root.right
                if current is not None:
                    current.next = root.right
                current = root.right
            root = root.next
        if next is not None:
            self.connectRec(next)


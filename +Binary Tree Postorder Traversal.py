__author__ = 'Jia'
'''
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

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
    def postorderTraversal(self, root):
        result = []
        l = []
        lastNode = None
        while root is not None or len(l) != 0:
            self.add(root, l)
            root = None
            currentNode = l[-1]
            if currentNode.right is None or currentNode.right == lastNode:
                result.append(l.pop().val)
                lastNode = currentNode
            else:
                self.add(currentNode.right, l)
        return result

    def add(self, root, l):
        while root is not None:
            l.append(root)
            root = root.left

tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
s = Solution()
print s.postorderTraversal(tree)
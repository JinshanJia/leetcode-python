__author__ = 'Jia'
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

import collections
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        if root is None:
            return result
        queue = collections.deque([root])
        currentLevel = 1
        nextLevel = 0
        currentList = []
        while len(queue) != 0:
            currentNode = queue.popleft()
            currentList.append(currentNode.val)
            currentLevel -= 1
            if currentNode.left is not None:
                queue.append(currentNode.left)
                nextLevel += 1
            if currentNode.right is not None:
                queue.append(currentNode.right)
                nextLevel += 1

            if currentLevel == 0:
                currentLevel = nextLevel
                nextLevel = 0
                result.append(currentList)
                currentList = []
        return result
# Given binary tree {3,9,20,#,#,15,7},
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

s = Solution()
print s.levelOrder(tree)
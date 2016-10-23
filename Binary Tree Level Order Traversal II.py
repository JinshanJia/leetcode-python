__author__ = 'Jia'
'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by
level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7]
  [9,20],
  [3],
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
    def levelOrderBottom(self, root):
        if root is None:
            return []
        resultQueue = collections.deque()
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
                resultQueue.appendleft(currentList)
                currentLevel = nextLevel
                nextLevel = 0
                currentList = []
        return list(resultQueue)

# Given binary tree {3,9,20,#,#,15,7},
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

s = Solution()
print s.levelOrderBottom(tree)
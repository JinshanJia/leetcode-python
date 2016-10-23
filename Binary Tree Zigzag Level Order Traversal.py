__author__ = 'Jia'
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        fromLeft = True
        result = []
        if root is None:
            return result
        queue = collections.deque([root])
        currentLevel = 1
        nextLevel = 0
        currentList = []
        while len(queue) != 0:
            if fromLeft:
                while currentLevel != 0:
                    currentNode = queue.popleft()
                    currentLevel -= 1
                    currentList.append(currentNode.val)
                    if currentNode.left is not None:
                        queue.append(currentNode.left)
                        nextLevel += 1
                    if currentNode.right is not None:
                        queue.append(currentNode.right)
                        nextLevel += 1

            else:
                while currentLevel != 0:
                    currentNode = queue.pop()
                    currentLevel -= 1
                    currentList.append(currentNode.val)
                    if currentNode.right is not None:
                        queue.appendleft(currentNode.right)
                        nextLevel += 1
                    if currentNode.left is not None:
                        queue.appendleft(currentNode.left)
                        nextLevel += 1


            currentLevel = nextLevel
            nextLevel = 0
            result.append(currentList)
            currentList = []
            fromLeft = not fromLeft

        return result

# Given binary tree {3,9,20,#,#,15,7},
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.left.left = TreeNode(8)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

s = Solution()
print s.zigzagLevelOrder(tree)
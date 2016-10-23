__author__ = 'Jia'
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):

        def pathSumRec(root, sum):
            if root is None:
                return []
            if root.left is None and root.right is None:
                if root.val == sum:
                    return [[root.val]]
                else:
                    return []
            result = []
            left = pathSumRec(root.left, sum - root.val)
            right = pathSumRec(root.right, sum - root.val)
            for l in left:
                tmp = [root.val]
                tmp.extend(l)
                result.append(tmp)
            for l in right:
                tmp = [root.val]
                tmp.extend(l)
                result.append(tmp)
            return result
        return pathSumRec(root, sum)



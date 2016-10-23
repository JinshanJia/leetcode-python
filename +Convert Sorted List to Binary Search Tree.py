__author__ = 'Jia'
'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        currentNode = head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return self.sortedListToBSTRec(head, length)[1]

    # return [nextNode, currentRoot]
    def sortedListToBSTRec(self, head, length):
        if length <= 0:
            return [head, None]
        mid = length / 2
        head, left = self.sortedListToBSTRec(head, mid)
        root = TreeNode(head.val)
        root.left = left
        head, right = self.sortedListToBSTRec(head.next, length - 1 - mid)
        root.right = right
        return [head, root]

s = Solution()
head = None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
tree = s.sortedListToBST(head)


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
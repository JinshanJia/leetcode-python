__author__ = 'Jia'
'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be
changed.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None:
            return head
        return self.swapTwoNodes(None, head)

    def swapTwoNodes(self, pre, current):
        if current is None or current.next is None:
            if pre is None:
                return current
            pre.next = current
            return
        node1 = current
        node2 = current.next
        next = node2.next
        node2.next = node1
        self.swapTwoNodes(node1, next)
        if pre is not None:
            pre.next = node2
        else:
            return node2

def buildNode(l):
    head = ListNode(l[0])
    crr = head
    for i in l[1:]:
        crr.next = ListNode(i)
        crr = crr.next
    return head
def getList(node):
    l = []
    while node is not None:
        l.append(node.val)
        node = node.next
    return l

s = Solution()
l = [1]
head = buildNode(l)
head = s.swapPairs(head)
print getList(head)

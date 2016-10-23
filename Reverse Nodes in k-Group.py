__author__ = 'Jia'
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k <= 1:
            return head
        return self.reverseKNodes(head, k)

    def reverseKNodes(self, head, k):
        if head is None:
            return head
        count = 0
        pre = None
        current = head
        while current is not None and count < k:
            next = current.next
            current.next = pre
            pre = current
            current = next
            count += 1
        if count < k:
            current = pre
            pre = None
            while current is not None and count >= 0:
                next = current.next
                current.next = pre
                pre = current
                current = next
                count += 1
            return head
        head.next = self.reverseKNodes(current, k)
        return pre

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
l = [1, 2, 3, 4, 5, 6]
head = buildNode(l)
head = s.reverseKGroup(head, 6)
print getList(head)
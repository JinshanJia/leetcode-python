__author__ = 'Jia'
'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummyNode = ListNode(-1)
        dummyNode.next = head
        parrent = dummyNode
        count = 1
        while count < m:
            count += 1
            parrent = parrent.next
        self.reverseNode(parrent, n - m + 1)
        return dummyNode.next

    def reverseNode(self, parrent, n):
        curr = parrent.next
        count = 0
        pre = None
        while count < n:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
            count += 1
        parrent.next.next = curr
        parrent.next = pre

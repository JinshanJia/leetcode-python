__author__ = 'Jia'
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal
to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        dummyBeforeHead = ListNode(-1)
        dummyAfterHead = ListNode(-1)
        curr = head
        currBefore = dummyBeforeHead
        currAfter = dummyAfterHead
        while curr is not None:
            if curr.val < x:
                currBefore.next = curr
                currBefore = currBefore.next
            else:
                currAfter.next = curr
                currAfter = currAfter.next
            curr = curr.next
        currBefore.next = dummyAfterHead.next
        currAfter.next = None
        return dummyBeforeHead.next

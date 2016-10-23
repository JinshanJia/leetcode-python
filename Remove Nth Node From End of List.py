__author__ = 'Jia'
'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        count = 1
        faster = head
        while count <= n and faster is not None:
            count += 1
            faster = faster.next
        if faster is None:
            return head.next

        slower = head
        while faster.next is not None:
            faster = faster.next
            slower = slower.next
        slower.next = slower.next.next
        return head


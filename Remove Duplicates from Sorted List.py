__author__ = 'Jia'
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return head
        pre = head
        curr = head.next
        while curr is not None:
            if pre.val != curr.val:
                pre.next = curr
                pre = curr
            curr = curr.next
        pre.next = None
        return head
__author__ = 'Jia'
'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
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
    def rotateRight(self, head, k):
        if head is None or k == 0:
            return head
        count = 1
        front = head
        while count < k:
            count += 1
            front = front.next
            if front is None:
                front = head
        back = head
        preBack = None
        while front.next is not None:
            front = front.next
            preBack = back
            back = back.next
        if preBack is None:
            return head
        front.next = head
        preBack.next = None
        head = back
        return head

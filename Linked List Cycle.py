__author__ = 'Jia'
'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        faster = head
        slower = head
        while faster is not None and faster.next is not None:
            faster = faster.next.next
            slower = slower.next
            if faster == slower:
                return True
        return False
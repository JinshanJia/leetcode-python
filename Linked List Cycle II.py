__author__ = 'Jia'
'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        faster = head
        slower = head
        while faster is not None and faster.next is not None:
            faster = faster.next.next
            slower = slower.next
            if faster == slower:
                break
        if faster is None or faster.next is None:
            return None
        faster = head
        while faster != slower:
            faster = faster.next
            slower = slower.next
        return slower

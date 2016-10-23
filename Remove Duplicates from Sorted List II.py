__author__ = 'Jia'
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the
original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
        dummyNode = ListNode(-1)
        dummyNode.next = head
        pre = dummyNode
        curr = head
        while True:
            oneNode = True
            while curr is not None:
                if curr.next is None or curr.val != curr.next.val:
                    if oneNode:
                        break
                    else:
                        curr = curr.next
                        oneNode = True
                else:
                    curr = curr.next
                    oneNode = False
            pre.next = curr
            pre = curr
            if curr is None:
                break
            curr = curr.next
        return dummyNode.next
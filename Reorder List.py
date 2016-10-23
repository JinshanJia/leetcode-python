__author__ = 'Jia'
'''
Given a singly linked list L: L0->L1->...->Ln-1->Ln,
reorder it to: L0->Ln->L1->Ln->1->L2->Ln-2->...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def reorderList(self, head):
        if head is None:
            return None
        listStack = []
        curr = head
        while curr is not None:
            listStack.append(curr)
            curr = curr.next
        curr = head
        stackCurr = listStack.pop()
        while curr != stackCurr:
            tmp = curr.next
            curr.next = stackCurr
            curr = tmp
            if curr == stackCurr:
                break
            stackCurr.next = curr
            stackCurr = listStack.pop()
        curr.next = None
        return head
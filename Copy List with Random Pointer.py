__author__ = 'Jia'
'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the
list or null.

Return a deep copy of the list.
'''
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        result = RandomListNode(head.label)
        created = {head: result}
        created[None] = None
        curr = head
        while curr is not None:
            newNode = created[curr]
            if curr.next not in created:
                created[curr.next] = RandomListNode(curr.next.label)
            newNode.next = created[curr.next]
            if curr.random not in created:
                created[curr.random] = RandomListNode(curr.random.label)
            newNode.random = created[curr.random]
            curr = curr.next
        return result

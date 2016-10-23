__author__ = 'Jia'
'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes
of the first two lists.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummyNode = ListNode(-1)
        crr1 = l1
        crr2 = l2
        crr = dummyNode
        while crr1 is not None and crr2 is not None:
            if crr1.val < crr2.val:
                crr.next = crr1
                crr1 = crr1.next
            else:
                crr.next = crr2
                crr2 = crr2.next
            crr = crr.next
        if crr1 is not None:
            crr.next = crr1
        if crr2 is not None:
            crr.next = crr2
        return dummyNode.next



l1 = [1,3,5,7]
l2 = [2,4,6,8]
head1 = ListNode(l1[0])
head2 = ListNode(l2[0])
crr1 = head1
crr2 = head2
for i in range(1, len(l1)):
    crr1.next = ListNode(l1[i])
    crr1 = crr1.next
for i in range(1, len(l2)):
    crr2.next = ListNode(l2[i])
    crr2 = crr2.next

s = Solution()
head = s.mergeTwoLists(head1, head2)
l = []
crr = head
while crr is not None:
    l.append(crr.val)
    crr = crr.next
print l
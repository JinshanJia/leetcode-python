__author__ = 'Jia'

# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each
# of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        c1 = l1
        c2 = l2
        result = ListNode(c1.val + c2.val)
        current = result
        c1 = c1.next
        c2 = c2.next
        while c1 is not None and c2 is not None:
            temp = ListNode(c1.val + c2.val)
            current.next = temp
            current = temp
            c1 = c1.next
            c2 = c2.next

        if c1 is None:
            while c2 is not None:
                temp = ListNode(c2.val)
                current.next = temp
                current = temp
                c2 = c2.next
        else:
            while c1 is not None:
                temp = ListNode(c1.val)
                current.next = temp
                current = temp
                c1 = c1.next

        current = result
        while current.next is not None:
            if current.val >= 10:
                current.val -= 10
                current.next.val += 1
            current = current.next
        if current.val >= 10:
            current.val -= 10
            current.next = ListNode(1)
        return result

s = Solution()
head1 = None

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)

head = s.addTwoNumbers(head1, head2)

l = []
while head is not None:
    l.append(head.val)
    head = head.next

print(l)
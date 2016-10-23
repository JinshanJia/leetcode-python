__author__ = 'Jia'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None:
            return None

        def mergeSort(head, length):
            if length == 1:
                next = head.next
                head.next = None
                return [head, next]
            leftResult = mergeSort(head, length / 2)
            rightResult = mergeSort(leftResult[1], length - length / 2)
            return merge(leftResult, rightResult)

        def merge(leftResult, rightResult):
            dummy = ListNode(-1)
            curr = dummy
            currLeft = leftResult[0]
            currRight = rightResult[0]
            while currLeft is not None and currRight is not None:
                if currLeft.val < currRight.val:
                    curr.next = currLeft
                    currLeft = currLeft.next
                else:
                    curr.next = currRight
                    currRight = currRight.next
                curr = curr.next
                curr.next = None
            while currLeft is not None:
                curr.next = currLeft
                currLeft = currLeft.next
                curr = curr.next
                curr.next = None
            while currRight is not None:
                curr.next = currRight
                currRight = currRight.next
                curr = curr.next
                curr.next = None
            return [dummy.next, rightResult[1]]

        count = 0
        curr = head
        while curr is not None:
            count += 1
            curr = curr.next
        return mergeSort(head, count)[0]

s = Solution()

head = ListNode(1)
a = [2, 3, 4]
curr = head
for n in a:
    curr.next = ListNode(n)
    curr = curr.next
head = s.sortList(head)
curr = head
l = []
while curr is not None:
    l.append(curr.val)
    curr = curr.next
print l

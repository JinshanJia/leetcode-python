__author__ = 'Jia'
'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if lists is None or len(lists) == 0:
            return None
        size = len(lists)
        while size > 1:
            for i in range(size / 2):
                list1 = lists[i]
                list2 = lists[size - i - 1]
                lists[i] = self.mergeTwoLists(list1, list2)
            size -= size / 2
        return lists[0]


    def mergeTwoLists(self, list1, list2):
        if list1 is None or list2 is None:
            return list1 if list2 is None else list2
        if list1.val < list2.val:
            result = list1
            list1 = list1.next
        else:
            result = list2
            list2 = list2.next
        current = result
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        while list1 is not None:
            current.next = list1
            list1 = list1.next
            current = current.next
        while list2 is not None:
            current.next = list2
            list2 = list2.next
            current = current.next
        return result

lists = []
list1 = ListNode(1)
list2 = ListNode(0)
list3 = ListNode(3)
list3.next = ListNode(4)
list4 = None
lists = [list1]
s = Solution()
l = s.mergeKLists(lists)
r = []
while l is not None:
    r.append(l.val)
    l = l.next
print r
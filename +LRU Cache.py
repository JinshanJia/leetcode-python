__author__ = 'Jia'
'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it
should invalidate the least recently used item before inserting a new item.
'''
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = max(capacity, 1)
        self.length = 0
        self.innerDict = {}
        self.doublelist = DoublyLinkedList()

    # @return an integer
    def get(self, key):
        if key not in self.innerDict:
            return -1
        node = self.innerDict[key]
        self.doublelist.remove(node)
        self.doublelist.addFirst(node)
        return node.val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.innerDict:
            self.innerDict[key].val = value
            node = self.innerDict[key]
            self.doublelist.remove(node)
            self.doublelist.addFirst(node)
            return
        if self.length == self.capacity:
            toRemove = self.doublelist.tail.pre
            del self.innerDict[toRemove.key]
            self.doublelist.remove(toRemove)
            self.length -= 1
        node = DoubleLinkedNode(value, key)
        self.innerDict[key] = node
        self.doublelist.addFirst(node)
        self.length += 1

class DoublyLinkedList:
    def __init__(self):
        self.head = DoubleLinkedNode(-1, -1)
        self.tail = DoubleLinkedNode(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def addFirst(self, node):
        node.next = self.head.next
        node.next.pre = node
        self.head.next = node
        node.pre = self.head

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

class DoubleLinkedNode:
    def __init__(self, val, key):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None

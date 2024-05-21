---
title:  "LRU Cache"
created: 2022-12-16
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# LRU Cache
Least recently used (LRU) cache. Discard the least recently used items first from the cache to make room for new elements when cache is full.

Retrieving data from a computer's memory is an expensive task. 
High-speed memory known as cache memory is used to avoid accessing data from memory repeatedly.

## Operations
- LRUCache(int Capacity): Initialize LRU Cache with positive size capacity
- get(key): Return value of key if it exists
- put(key, val): Update value of key if exists, otherwise add key-value pair to cache. If number of keys exceeds the capacity of LRU cache, evict the least recently used key.

Access times are O(1).
Time required to get least recently used element is O(1).
Space required is O(n).

# Brute force: Using a simple array or linked list
Initialize an array of size equal to that of our cache. Each data element stores extra information (timestamp). Use timestamp to find the least recently used element in the LRU cache. Set the time-stamp of the most recently used element to 0. If we insert an item, increment the timestamp of all existing data by 1. Insert the new element with timestamp 0.

```python
from datetime import datetime
class DataElement:
	def __init__(self):
		self.key = key
		self.val = val
		self.time_stamp = datetime.now
	
```
 Time Complexity O(n)

# Implementation Using Hash map and Doubly Linked List

```python
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
```

## Optimizations

## Optimized Complexity

>[!Time Complexity]+
>Lookup: O(1)

>[!Space Complexity]+
>O(n)



# Related
[[LFU Cache]]
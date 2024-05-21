---
title:  "D-ary Heap"

created: 2022-12-10
---




# D-ary Heap
Each node can have up to D children.

 >[!danger]+ Intuition
> More children means a flatter tree with smaller depth.
> This means it requires less work to swim but more work to sink since you have to check the parent node against D children.

[Dijkstra's Shortest Path Algorith](</docs/Algos/Dijkstra's Shortest Path Algorithm.md>)
D-ary heaps also have better locality of reference for larger D in the dequeue operation. (https://stackoverflow.com/questions/29126428/binary-heaps-vs-d-ary-heaps)
# Implementation (0-indexed)

```python
class D_aryHeap:
	def __init__(self, d):
		self.heap = []
		self.size = 0
		self.d = d

	def size(self):
		return self.size

	def parent(self, i):
		return (i-1)//self.d

	def child(self, index, pos):
		return index*self.d + (pos+1)

	def get(self, i):
		return self.heap[i]

	def poll(self):
		min_key = self.heap[0]
		self.heap[0] = self.heap[self.size]
		self.size -= 1
		self.sink(0)
		return min_key

	def sink(self, i):
		min_i = i
		for j in range(self.d):
			c = self.child(i, j)
			if c < self.size and self.heap[c] < self.heap[i]:
				min_i = c
		if min_i != i:
			self.swap(min_i, i)
			self.sink(min_i)

	def swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def insert(self, key):
		i = self.size
		self.heap.append(key)
		self.size += 1
		self.swim(self.size)

	def swim(self, i):
		p = self.parent(i)
		while i > 0 and self.heap[i] < self.heap[p]:
			self.swap(i, p)
			i = p
			p = self.parent(i)
```

## Optimizations

## Optimized Complexity

>[!Time Complexity]+
>Notice that the maximum height for n nodes is $log_kn$
>Building the heap is still O(n) 
>Swim: $O(log_kn)$
>Sink: $O(klog_kn)$
>Swim < Sink


>[!Space Complexity]+
>O(n) to store all the 


# Related
[Heaps](</docs/DS/Heaps.md>)[Indexed D-ary Heap](</docs/DS/Indexed D-ary Heap.md>)[Indexed Priority Queue (IPQ)](</docs/DS/Indexed Priority Queue (IPQ).md>)
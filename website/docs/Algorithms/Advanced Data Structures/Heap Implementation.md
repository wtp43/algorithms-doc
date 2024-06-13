---
---

:::note[note] 

O(n) to build using sift_down starting from the last parent

:::

# Implementation

- This implementation of a min_heap is one-indexed for simplicity.
- In the case of zero-indexing, the parent of a child `i` is located at `p = (i-1)//2`

```python
class min_heap:

	def __init__(self):
		self.heap = [0]
		self.size = 0
		
	def insert(self, x):
		self.heap.append(x)
		self.size += 1
		self.sift_up(self.size)
		
	def sift_up(self, i):
		while i > 1:
			p = i//2
			if self.heap[i] < self.heap[p]:
				self.swap(i, p)
			i = p
			
	def sift_down(self, i):
		while i*2 < self.size:
			mc = self.get_minchild():
			if self.heap[i] > self.heap[mc]:
				self.swap(i, mc)
			i = mc
			
	def min_child(self, i):
		if i*2+1 > self.size or self.heap[i*2] < self.heap[i*2+1]:
			return i*2
		return i*2+1
		
	def poll(self):
		min_val = self.heap[1]
		self.heap[1] = self.heap[-1]
		self.heap.pop()
		self.size -= 1
		self.sift_down(1)
		return min_val
			
	def swap(self, x, y):
		self.heap[x], self.heap[y] = self.heap[y], self.heap[x]
		
	def make_heap(self, arr):
		self.size = len(arr)
		i = self.size//2
		self.heap = [0] + arr
		while i > 0:
			self.sift_down(i)
			i -= 1


h = min_heap()
h.insert(1)
h.insert(2)
min_val = h.poll()

```

# Heapq in Python

```python
import heapq

pq = []
heapq.heapify(pq)
heapq.heappush(pq, 1)
heapq.heappop(pq)
```

:::Applications[Applications] 

Build priority queue with get_min and insert in O(logn)

:::


# Related
[D-ary Heap](</docs/Algorithms/Advanced Data Structures/D-ary Heap.md>)[Indexed Priority Queue (IPQ)](</docs/Algorithms/Advanced Data Structures/Indexed Priority Queue (IPQ).md>)[Indexed D-ary Heap](</docs/Algorithms/Advanced Data Structures/Indexed D-ary Heap.md>)
---
title:  "Indexed Priority Queue"
created: 2022-12-12
---

# Indexed Priority Queue (Binary)
1. Assign index values to all the keys forming a bidirectional mapping using a bidirectional hashtable (maintain two dictionaries)

## Swap(i, j)
- i, j are the key indexes

Key | Key Index
---- | ---- 
'A' | 1
'B' | 2
'C' | 3
'D' | 4
'E' | 5
'F' | 6
'G' | 7

|      | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| vals |  0   |  6   | 10    |  4   |  7   |   15  |   1  |   12  |
| pm   |  0   |  3   |  5   |   2  |  4   |   7  |   1  |   6  |
| im   |  0   |  6   |  3   |  1   |  4   |  2   |  7   |  5   |

Swap(6, 5) results in

|      | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| vals |  0   |  6   | 10    |  4   |  7   |   15  |   1  |   12  |
| pm   |  0   |  3   |  5   |   2  |  4   |   '1'  |   '7'  |   6  |
| im   |  0   |  5   |  3   |  1   |  4   |  2   |  7   |  6   |

vals: ki -> value
pm: ki -> node index
im: node index (heap) -> ki

# Implementation

- We are only swapping the positions of the values
- The values array stays constant


```python
class IPQ:
	def __init__(self, n):
		#position map (key index -> node index)
		self.pm = [None] * (n+1)
		#inverse map (node index -> key index)
		self.im = [None] * (n+1)
		self.val = [None] * (n+1)
		self.size = n

	def size():
		return self.size

	def contains(self, ki):
		return self.val[ki] != None

	def insert(self, ki, value):
		values[ki] = value
		pm[ki] = self.size
		im[self.size] = ki
		swim(self.size)
		self.size += 1

	# Swims up node i (one based) until heap 
	# invariant is satisfied
	def swim(self, i):
		while i > 1 and less(i, i//2):
			self.swap(i, i//2)	
			i = i//2

	# i, j are heap positions aka node i and j in the heap
	# swap only moves around indexes.  
	def swap(self, i, j):
		# j is a number representing a position in the heap
		# im[j] = the node at position j in the heap
		# pm[im[j]] = the position of node j in the heap
		self.pm[self.im[j]] = i
		self.pm[self.im[i]] = j
		# the node at position i in the heap 
		# is now swapped the node at position j
		self.im[i], self.im[j] = self.im[j], self.im[i]

	def less(self, i, j):
		return values[im[i]] < values[im[j]]

	def remove(self, ki):
		# find node index (i) using key index (ki) and 
		# the position map
		i = self.pm[ki]
		swap(i, self.size)
		self.size -= 1
		# since we don't know whether to move it up or down
		# we sink and swim i
		self.sink(i)
		self.swim(i)
		self.values[ki] = null

	def sink(self, i):
		while true:
			left = 2*i + 1
			right = 2*i + 2
			smallest = left
			if right <= size and self.less(right, left):
				smallest = right
			if left > size or self.less(i, smallest)
				break
			self.swap(smallest, i)
			i = smallest


	def update(self, ki, value):
		i = self.pm[ki]
		self.values[ki] = value
		self.sink(i)
		self.swim(i)

	def peek(self, i):
		ki = im[i]
		return ki, self.val[ki]

	def poll(self):
		ki = im[1]
		min_val = val[ki]
		self.remove(ki)
		return ki, min_val

	# The functions below assumes ki and value are valid 
	# inputs and we are dealing with a min indexed binary heap
	
	def decrease_key(self, ki, v):
		if less(value, self.values[ki]):
			self.values[ki] = value
			self.swim(pm[ki])

	def increase_key(self, ki, value):
		if less(self.values[ki], value):
			self.values[ki] = value
			self.sink(pm[ki])

	def make_heap(self, arr):
		self.size = len(arr)
		p = self.size//2
		self.values = arr
		self.pm = [i for i in range(self.size + 1)]
		self.im = [i for i in range(self.size + 1)]
		while p > 0:
			self.sink(p)
			p -= 1
	
```

## Optimizations

## Optimized Complexity

:::Time-Complexity[Time Complexity] 

Sink/Swim: O(logn)
Update/decrease_key/increase_key: O(logn)
Build heap: O(n)

:::




:::Space-Complexity[Space Complexity] 


:::

# Related


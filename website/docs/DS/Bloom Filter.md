---
title:  "Bloom Filter"
created: 2022-12-15
---




# Bloom Filter
Space-efficient O(1) hashmap. Tradeoff for the space efficiency is that it's probabilistic.

When you look up an item in a bloom filter, the possible answers are:
- It's definitely not in the set (true negative)
- It might be in the set (either false positive or true positive)

Only supports insert and lookup operations. Can't iterate or delete.


:::danger[danger] 

Useful for when knowing something is definitely not present or possibly present would be helpful. 

:::
> 
> For instance, say we wanted to query a large database stored on a rotating hard drive (slow to read from). Before querying the disk, we could check for the record in a bloom filter and see if it's definitely not in there.

## Bitmap Size
The larger the bitmap, the less likely false positives are.

## Multiple Hash Functions
Another way to avoid a high false positive rate is to use multiple hash functions.
When using multiple hash functions:
- To add a new item: generate a bitmap index with _each_ hash function, and set _all_ of those bits to 1.
- To check if an item is present: just check if _any_ of the bits checked are still 0. If so, the item is definitely not present. (For a different item, it may only flipped one of the bits)

## False Positive Rate
- n = # of elements
- m = length of bloom filter
- k = number of hash functions
Assume that the hash function selects each index with equal probability. 
The probability that a particular bit is not set to 1 by a specific hash function during the insertion of an element is $1-\frac{1}{m}$.
If we pass this element through k hash functions, the probability that the bit is not set to 1 by any of the hash function is $(1-\frac{1}{m})^k$.
After inserting n elements, the probability that a particular bit is still 0 is $(1-\frac{1}{m})^{kn}$.
The probability that it is one is $1 - (1-\frac{1}{m})^{kn}$.
Here we want to test the membership of an element in the set. The probability of all k array positions computed by the hash functions being 1 is $(1 - (1-\frac{1}{m})^{kn})^k$, which is known as the **error rate**.
As 

# Implementation
- Simply a bitmap. Initially all bits are set to 0. 
- Fixed size is crucial here (remember, bloom filters require O(1) space)


```python
import mmh3 # murmurhash: is faster for blooms
import math

class Bloom_filter(object):
	def __init__(self, m , k):
		self.m = m # size of bloomfilter
		self.k = k # number of hash functions
		self.n = 0
		self.bloom_filter = [0] * self.m

	def clear_bits(self):
		self.n = 0
		self.bloom_filter = [0] * self.m

	def get_bit_array_indices(self, item):
		"""
		hashes the key for k defined, 
		returns a list of indices to be set 
		"""

		index_list = []
		for i in range(1, self.k + 1):
			index_list.append((hash(item) + i * mmh3.hash(item)) % self.m)
		return index_list

	def add(self, item):
		for i in self.get_bit_array_indices(item):
			self.bloom_filter[i] = 1
		self.n += 1

	def contains(self, key):
		for i in self.get_bit_array_indices(key):
			if self.bloom_filter[i] == 0:
				return False
		return True

	def length(self):
		return self.n

	def generate_stats(self):
		n = float(self.n)
		m = float(self.m)
		k = float(self.k)
	
		probability_fp = math.pow((1.0 - math.exp(-(k*n)/m)), k)
		print(probability_fp)

	def reset(self):
		self.clear_bits()
			
```

## Optimizations

## Optimized Complexity

:::Time-Complexity[Time Complexity] 


:::
>Look up and insert are O(1)

:::Space-Complexity[Space Complexity] 


:::
>O(1)

# Applications
[LRU Cache](</docs/DS/LRU Cache.md>)# Related

Reference: https://www.enjoyalgorithms.com/blog/bloom-filter
---
title:  "Kth Largest"
created: 2023-01-13
---
# Top K Numbers
Use a min heap to keep track of the k largest numbers. Fill the heap up with k numbers. If the current number is smaller than the heap minimum, continue. If it is bigger, pop the top of the heap and push this number onto the heap.

## Applications
Find the _top_ / _smallest_ / _frequent_ **K** elements
# Implementation

```python
def findKthLargest(self, nums: List[int], k: int) -> int:
	min_heap = []
	
	for i in range(k):
		heappush(min_heap, nums[i])
	
	for i in range(k, len(nums)):
		if nums[i] > min_heap[0]:
			heappop(min_heap)
			heappush(min_heap, nums[i])
		
	return min_heap[0]
```

## Optimizations

## Optimized Complexity

:::Time-Complexity[Time Complexity] 


:::
>O(NlogK) 
>Logk is the complexity to extract/insert into the heap. Then we need to do it for N numbers

:::Space-Complexity[Space Complexity] 


:::



# Related

---
title:  "Bucket Sort"
created: 2022-12-13
---




# Bucket Sort (Scatter Gather Approach)
Divides unsorted array elements into buckets. Each bucket is then sorted using a sorting algorithm or recursively applying the same bucket algorithm. Bucket sort does not involve direct comparison between numbers.

Useful for when the input is uniformly distributed over a range or there are floating point values.

Stable if the underlying sort is stable

:::danger[danger] 

Bucket sort/count sort is extremely useful (sorting in O(n) time) when you know the maximum number in the array. Then you can insert all items into a list of buckets then pop the items from the bucket sequentially.

:::



# Implementation for floats ranging between 0 and 1
Make 10 buckets
Nums are decimals between 0 and 1 hence the * 10
```python
def bucket_sort(nums):
	b = [[] for i in range(len(nums))]
	output = [None] * len(nums)
	# insert elements into repective buckets
	for num in nums:
		i = int(num * 10)
		bucket[i].append(num)

	# sort the elements of each bucket
	for i in range(len(bucket)):
		bucket[i].sort()

	# get the sorted elements
	k = 0
	for i in range(len(array)):
		for j in range(len(bucket[i])):
			output[k] = bucket[i][j]
			k += 1
	return output
```

# Implementation for integers

```python
def bucket_sort(nums, n_buckets):
	max_val = max(nums)
	min_val = min(nums)
	r = math.ceil(max_val - min_val)
```

## Optimizations

A degenerate case of bucket sort ([[Counting Sort#Unstable version (without cumulative sum), works only for integers|unstable count sort]]) runs in o(n) time.


## Optimized Complexity

:::Time-Complexity[Time Complexity] 

O($nlogn$), occurs if elements are all placed into the same buckets.

:::
[Insertion Sort](</docs/Algos/Insertion Sort.md>)
:::Space-Complexity[Space Complexity] 

O(n+k) where n is the number of elements and k is the number of buckets formed.

:::


# Related

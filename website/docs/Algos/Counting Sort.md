---
title:  "Count Sort"
created: 2022-12-15
---




# Counting Sort
Stable sort. Count occurrences of each unique element in array and stores it in an auxiliary array. Then calculate the cumulative sum of the elements of the count array. Use the cumulative sum to place the numbers in the correct position.

![Pasted-image-20221215155937.png](</Pasted-image-20221215155937.png>)

:::danger[danger] 

Useful for keys are integers. I.e. [('msft', 1), ('aapl', 2)] or [-3,-2, 1, -20]. Linear in the range of the elements.

:::


# Implementation

## Unstable version (without cumulative sum), works only for integers
```python
# Saves space but doing lots of addition/subtraction
def counting_sort(nums):
	min_val = math.inf
	max_val = -math.inf
	for val in nums:
		if val < min_val:
			min_val = val
		if val > max_val:
			max_val = val

	sz = max_val - min_val + 1
	b = [0] * sz
	for i in range(len(nums)):
		b[nums[i] - min_val] += 1
	k = 0
	for i in range(sz):
		while b[i] > 0:
			b[i] -= 1
			nums[k] = i + min_val
			k += 1
			
# if min_val is low
def count_sort(nums):
	n = len(nums)
	k = max(n)
	b = [0] * k

	# store count
	for i in range(n):
		b[nums[i]] += 1
	
	k = 0
	for i in range(n):
		while b[i] > 0:
			b[i] -= 1
			nums[k] = i
			k += 1
		

```

## Stable version (uses cumulative sum, useful when items sorted are not just integers)
- This version is stable because we iterate the unsorted array backwards, check its position in the sorted array according to the counts array, and copy it to the sorted array
- The counts array is not used to tell how many times an integer appears in the unsorted array, instead, it is used to tell which position the element should be in the final sorted array. And since we decrease the count every time we output an element, we are essentially making the elements with same key's next appearance final position smaller. That's why we need to iterate the unsorted array from backwards to ensure its stableness. (https://stackoverflow.com/questions/2572195/how-is-counting-sort-a-stable-sort)


```python
def counting_sort(nums):
	n = len(nums)
	k = max(nums) + 1
	count = [0] * k
	output = [0] * n
	
	# store count
	for i in range(n):
		count[nums[i]] += 1

	# store cumulative count
	for i in range(1,k):
		count[i] += count[i-1]

	# place nums backwards to ensure stableness
	for num in reversed(nums):
		# count[num] -=1 because this stores the count but the index of the output is 0-based
		count[num] -= 1
		output[count[num]] = num
	return output
```

## Accounting for negative numbers
``count = [0] * max_val - min_val + 1``
``count[nums[i] - min_val] += 1``

```python
def counting_sort(nums):
    n = len(nums)
    min_val = min(nums)
    k = max(nums) - min_val + 1
    count = [0] * k
    output = [0]* n
    
    # store count
    for num in enumerate(nums):
        count[num - min_val] += 1

    # store cumulative count
    for i in range(1,k):
        count[i] += count[i-1]

    # place nums backwards
    for num in reversed(nums):
        count[num-min_val] -= 1
        output[count[num-min_val]] = num
    return output
```

# Complexity

:::Time-Complexity[Time Complexity] 

The algorithm is only in linear time if k = max(n) is in O(n)

:::

:::Space-Complexity[Space Complexity] 

O(n + max_val - min_val)

:::

# Related
[Radix Sort](</docs/Algos/Radix Sort.md>)
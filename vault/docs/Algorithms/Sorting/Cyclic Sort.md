---
title:  "Cyclic Sort"
created: 2023-01-06
---
# Cyclic Sort
Swap numbers of array until they are in the correct place.
Iterate until you find missing/duplicate number.

<mark style="background: #cc085d;">Identification:</mark> given array of 0 to N, do some missing, repeated kind of operation  
**PigeonHole principle:** If you have N boxes and > N items, at least one box has more than 1 item.

## Applications:
Dealing with numbers in a given range and asking to find the duplicates/missing ones etc.

When the problem involving arrays containing numbers in a given range, you should think about cyclic sort pattern.

# Missing Number 
$i$ is the current index. We take fact of our knowledge that there is N boxes and a list of numbers from 0 to N+1.
- Thus, we know what the correct index should be. 
- Put the current item in it's correct spot
- Repeatedly do this
- In the end, we will have N+1 at the location of the missing number
- O(n) time complexity because each number gets swapped into its correct position at most once
```python
def missingNumber(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            correct_idx = nums[i]
            if correct_idx < len(nums) and correct_idx != i:
                nums[i], nums[correct_idx] = \
	                nums[correct_idx], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)
```


# Find all Duplicates in an Array
observation 1: ``[1,n] integers and some appear twice, we can't put two elements in same box.
observation 2: `for every element, correctIdx = nums[i] - 1 because instead of [0,n] we have [1,n] numbers

Similar to missing number. Each number can appear either once or twice.
The difference is that we don't need to swap if this is a duplicate.
Ex:
4 1 3 1 2 -> 1 1 3 4 2 
At this stage, we don't need to swap the 1's because a 1 is already in it's correct spot.
All the duplicated numbers will be at spots they shouldn't be. 
Pigeonhole principle again since we have filled all the correct numbers at their spots and each spot can only hold 1 number.

```python
def findDuplicates(self, nums: List[int]) -> List[int]:
	n = len(nums)
	i = 0
	res = []
	while i < n:
		correct_idx = nums[i]-1
		if nums[i] != nums[correct_idx]:
			nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
		else:
			i += 1

	for i in range(n):
		if nums[i]!= i+1:
			res.append(nums[i])
	return res
```
# Related

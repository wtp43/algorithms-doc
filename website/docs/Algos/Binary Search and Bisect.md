---
title:  "Binary Search and Bisect"
created: 2023-01-06
---




# Binary Search and Bisects

:::Note[Note] 

Binary Search should be equal to Bisect_left in the case of no duplicates

:::

## Bisect Left
- Returns the index of the first num $\leq$ x
- Repeatedly move right border towards the left if there are duplicates
- ``if target == arr[mid]: j = mid-1
- `if target > arr[-1]: i = len(arr)
- `if target < arr[0]: i = 0

```python
def bisect_left(arr, x):
	i = 0
	j = len(arr)-1
	while i <= j:
		mid = i + (j - i)//2
		if arr[mid] >= x:
			j = mid - 1
		else:
			i = mid + 1
	return i
```

## Bisect Right
- Returns the index of the first num > x
- ``if target == arr[mid]: i = mid+1
- `if target > arr[-1]: i = len(arr)
- `if target < arr[0]: i = 0`

```python
def bisect_right(arr, x):
	i = 0
	j = len(arr)-1
	while i <= j:
		mid = i + (j - i)//2
		if arr[mid] <= x:
			i = mid + 1
		else:
			j = mid - 1
	return i
```

```python
# leftBias=[True/False], if false, res is rightBiased
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i
```

# Related

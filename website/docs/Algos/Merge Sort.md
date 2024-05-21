---
title:  "Merge Sort"
created: 2022-12-15
---




# Merge Sort
Stable sort.
# Implementation

```python
def merge_sort(nums):
    if not nums:
        return

    mid = len(nums)//2
    L = nums[:mid]
    R = nums[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0
    len_L = len(L)
    len_R = len(R)
    while i < len_L and j < len_R:
        if L[i] < R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1

    while i < len_L:
        nums[k] = L[i]
        i += 1
        k += 1

    while j < len_R:
        nums[k] = R[j]
        j += 1
		k += 1
	
```

## Optimizations

## Optimized Complexity

>[!Time Complexity]+
>O(nlogn)

>[!Space Complexity]+
>O(n)



# Related

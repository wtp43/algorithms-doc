---
title:  "Insertion Sort"
created: 2022-12-15
---




# Insertion Sort
Places an unsorted element at its suitable place in each iteration.
**Insertion sort is a stable sort**. During the selection sort process, we will only swap the ordering of any two items if the item on the right is less than the item to its left. Therefore, the ordering of two equivalent items will always be preserved in insertion sort.

:::danger[danger] 

The insertion sort is useful when:
- the array is has a small number of elements
- there are only a few elements left to be sorted
- the array is almost sorted

:::

# Implementation

```python
# Insertion sort in Python

def insertionSort(nums):

    for i in range(1, len(nums)):
	    key = nums[i]
        j = i - 1
        # Compare key with each element on the left of it until an element smaller than it is found
      
        while j >= 0 and key < nums[j]:
            array[j + 1] = array[j]
            j -= 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
```

## Optimizations

## Optimized Complexity

:::Time-Complexity[Time Complexity] 


:::
>O($n^2$)

:::Space-Complexity[Space Complexity] 


:::
>O(1) for storing the key



# Related

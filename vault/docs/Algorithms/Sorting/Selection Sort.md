---
title:  "Selection Sort"
created: 2022-12-15
---




# Selection Sort
Not stable. The swap that occurs at the end of each iteration can change the relative order of items having the same value./


> [!example]+ Example
> Suppose you sorted 4a 2 3 4b 1 with selection sort.
> 
> The first "round" will go through each element looking for the minimum element. it will find that 1 is the minimum element. then it will swap the 1 into the first spot. this will cause the 4 in the first spot to go into the last spot: 1 2 3 4b 4a

# Implementation

```python
def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
```

To make this stable, insert of swapping values, insert the 'least value' at the beginning of the array pushing all elements back one index. (which is similar to insertion sort, but you are always picking the least value)
## Optimizations

## Optimized Complexity

>[!Time Complexity]+

>[!Space Complexity]+



# Related

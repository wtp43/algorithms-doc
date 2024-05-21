---
title:  "Radix Sort"
created: 2022-12-15
---




# Radix Sort
A non-comparative algorithm just like counting sort.
Sorts by first grouping the individual digits of the same **place value**. 

# Most Significant Digit (MSD) vs Least Significant Digitt (LSD) Radix Sort
If we start with the most significant digits, a first pass would go a long way toward sorting the entire range. The idea of a MSD radix sort is to divide all the digits with an equal value into their own bucket and repeat. Naturally, this suggests a recursive algorithm, but this also means that we can now sort variable length items and we don't have to touch all of the digits to get a sorted array. However, a recursive implementation of MSD uses more space than LSD. LSD is faster than MSD when there is a fixed length. (https://stackoverflow.com/questions/11939656/radix-sort-lsd-versus-msd-versions)
# LSD Radix Implementation

Counting sort is used as an intermediate sort in radix sort. Counting sort is slightly modified to divide 

```python
def counting_sort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


def LSD_radix_sort(nums):
	max_val = max(nums)

	# apply counting sort to sort elements based on place value
	place = 1
	while max_val // place > 0:
		counting_sort(nums, place)
		place *= 10
		
```

# MSD Radix Implementation

```python
def radix_sort_MSD_for_strings (array, i):

    # base case (list must already be sorted)
    if len(array) <= 1:
        return array

    # divide (first by length, then by order of the first character)
    done_bucket = []
    buckets = [ [] for x in range(64,100) ] # ASCII TABLE A-Z is from 64 to 90

    for s in array:
        if i >= len(s):
            done_bucket.append(s)
        else:
            buckets[ ord(s[i]) - ord('a') ].append(s)

    # ***********conquer (recursively sort buckets)***********
    buckets = [ radix_sort_MSD_for_strings (b, i + 1) for b in buckets ]
    return done_bucket + [ b for blist in buckets for b in blist ]
```

## Optimized Complexity

>[!Time Complexity]+
>O(n+k)

>[!Space Complexity]+
>O(max).
>If we take very large digit numbers or the number of other bases like 32-bit and 64-bit numbers then it can perform in linear time however the intermediate sort takes large space.
This makes radix sort space inefficient. This is the reason why this sort is not used in software libraries.



# Related

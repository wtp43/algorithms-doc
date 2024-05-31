---
---
# Prefix Sums
- Can be used if dealing with Subarrays
- Store some 'useful value' for all prefixes in an array
- Don't forget the base cases for the prefix sums
- Not applicable for subsequences

> [!tip] Intuition 
> Can be used to find max/min of some f(subarray) for all subarrays in O(n) 
## Example
Useful for sum of ranges.
sum i to j = `prefix[j] - prefix[i-1]

Subarray sum = k? 
- prefix sum
- we are essentially looking to see if the prefix sum: `prefix_sum[i]-k` exists.
## Prefix Sum + Hash Map
These questions are an extension of twosum.
We use a Hash Map to find if a previous prefix sum exists.

[[LC-560. Subarray Sum Equals K]]
- We have to store a counter for the number of prefix sums because you can add a 0 to the same subarray and get a new subarray with the same sum.
	- Take this example:  5,  2,  2,  0,  3
	- For k = 3, we can take the subarray (0,3) or (3)
- We want to see if we can jump from index 0 to index `prefix_sum[i]-k` for every i
- Initialize `prefix_sum[0]=1` for the case that we use the entire prefix_sum

[[LC-523. Continuous Subarray Sum]]
- Reduces to subarray sum equals k. 
- Initialize `prefix_sums[0] = 1` for the case that we use the entire prefix_sum

## Range Based Problems

### Difference Array + Binary Search

## Applications

### Sum of Ranges
https://leetcode.com/problems/subarray-sum-equals-k/description/



### Tracking Valid Subarrays

### Max/Min 'f(x)' of Subarray

### Sum of Distances

https://leetcode.com/problems/sum-of-distances/description/

- Store occurrences/indices in dictionary
- Iterate all indices of each key in the dictionary
- Build prefix and suffix sum for each key
- Complexity: O(n) for each number + O(n) to sum

```python
def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)

        arr = [0]*len(nums)
        for x in d:
            prefix = 0
            suffix = sum(d[x])
            n = len(d[x])
            p = 0
            for i in d[x]:
                arr[i] = i*p-prefix + suffix-i*(n-p)
                p += 1
                prefix += i
                suffix -= i
        return arr
```

### Max Partitions Allowed to Make Sorted Array

- Split arr into maxiumum number of individually sorted partitions such that concatenated array is also sorted
- A partition is only possible if the maximum prefix is less than the minimum suffix

```python
def maxChunksToSorted(self, arr: List[int]) -> int:
        # a partition can be made if
        # max[:i+1] < min[i+1:]

        n = len(arr)
        minSuffix = [math.inf]*(n+1)
        for i in range(n-1, 0, -1):
            minSuffix[i] = min(arr[i], minSuffix[i+1])

        maxPrefix = 0
        partition = 0
        for i in range(n):
            maxPrefix = max(maxPrefix, arr[i])
            if maxPrefix <= minSuffix[i+1]:
                partition += 1
        return partition
```


## Tracking Multiple Prefixes
### Count Triplets
https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

- Use one map to store number of occurrences
- Use another map to store the 'total contributions' of the previous occurrences
	- Here, we want the lengths of all previous subarrays that have the same prefix
	- We can do so by storing the cumulative distance of all x's to 0

```python
def countTriplets(self, arr: List[int]) -> int:
        res = 0
        prefix = 0
        # Store occurences
        count = defaultdict(int)
        # Base case: The current array[:i] satisfies the requirement
        count[0] = 1
        # Store cumulative distance from 0 to ith element where key = prefix[i]
        indices_sum = defaultdict(int)

        # Iterating through the array
        for i in range(len(arr)):
            prefix ^= arr[i]
            res += count[prefix] * i - indices_sum[prefix]

            # ---x----x----x
            # ---i----j-----k:
            # to get m's contribution :
            # k-i-1 + j-j-1
            # -1 because i < j <=k, so we can't pick i to be j 

            # Updating total count of current XOR value
            indices_sum[prefix] += i+1
            count[prefix] += 1
        return res
```

### Sweep Line
https://leetcode.com/problems/corporate-flight-bookings/description/
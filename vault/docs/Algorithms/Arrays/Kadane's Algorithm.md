---
---
# Kadane's Algorithm
- Solve maximum/minimum subarray in O(n) 

## Maximum Subarray
- Ask interviewer "Are subarrays with length 0 valid?"
```python
def maximum_array(arr):
	maxsuffix = 0
	maxsofar = 0 
	for a in arr:
		maxsuffix = max(0, maxsuffix + a)
		maxsofar = max(maxsofar, maxsuffix)
	return res

#if subarrays with length 0 are not valid
maxsofar = arr[0]
maxsuffix = 0
for a in arr:
    maxsuffix = max(a, maxsuffix + a)
    maxsofar = max(maxsofar, maxsuffix)
return maxsofar

```

## Subarray/Substring

### [2272. Substring With Largest Variance](https://leetcode.com/problems/substring-with-largest-variance/)
> Variance: largest difference in frequency between any two characters in a string

- Try combinations of all pairs of characters: $O(26^2)$
```python
def largestVariance(self, s: str) -> int:
        letters = set(s)
        max_var = 0
        for a in letters:
            for b in letters:
                if a == b:
                    continue
                var = 0
                has_b = False
                first_b = False

                for c in s:
                    if c == a:
                        var += 1
                    elif c == b:
                        has_b = True

                        if first_b and var >= 0: # the first letter is a b and the b count is greater than 1. Shift right (remove the first b and count the current b)
                            first_b = False
                        elif var < 1: # restart subarray from this b, used to skip double bb's
                            first_b = True
                            var = -1
                        else:
                            var -= 1
                    if has_b:
                        max_var = max(max_var, var)
        return max_var

```

### [Maximum Array after swapping equal length subarray](https://leetcode.com/problems/maximum-score-of-spliced-array/)
- Kadane's can be used to find the maximum subarray.
- INTUITION: We are trying to maximum the sum of the subarray after the swap. This is the same as precomputing a cost array for swapping the ith element.

```python
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        cost = [0]*n
        # compute cost (of swapping ith element) array
        for i in range(n):
            cost[i] = nums2[i] - nums1[i]
        # Run Kadane's twice
        cur = max_s = 0
        for i in range(n):
            cur = max(cur+cost[i], 0)
            max_s = max(max_s,cur)
        cur = max_t = 0
        for i in range(n):
            cur = max(cur-cost[i], 0)
            max_t = max(max_t, cur)
        return max(max_s+sum(nums1), max_t+sum(nums2))

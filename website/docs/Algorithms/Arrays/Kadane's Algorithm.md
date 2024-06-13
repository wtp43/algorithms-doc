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
	for a in range(arr):
		maxsuffix = max(0, maxsuffix + a)
		maxsofar = max(maxsofar, maxsuffix)
	return res

#if subarrays with length 0 are not valid
maxsofar = nums[0]
maxsuffix = 0
for a in nums:
    maxsuffix = max(a, maxsuffix + a)
    maxsofar = max(maxsofar, maxsuffix)
return maxsofar

```


## Substring with Largest Variance
https://leetcode.com/problems/substring-with-largest-variance/solutions/2579146/weird-kadane-intuition-solution-explained/

### Maximum Array after swapping equal length subarray

- Kadane's can be used to find the maximum subarray.
- INTUITION: We are trying to maximum the sum of the subarray after the swap. This is the same as precomputing a cost array for swapping the ith element.

```python
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        arr = [0]*n
        # compute cost (of swapping ith element) array
        for i in range(n):
            arr[i] = nums2[i] - nums1[i]
        # Run Kadane's twice
        cur = max_s = 0
        for i in range(n):
            cur = max(cur+arr[i], 0)
            max_s = max(max_s,cur)
        cur = max_t = 0
        for i in range(n):
            cur = max(cur-arr[i], 0)
            max_t = max(max_t, cur)
        return max(max_s+sum(nums1), max_t+sum(nums2))

---
---
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
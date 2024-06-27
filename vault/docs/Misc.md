# Misc
Random things to be organized



#### [Minimum Penalty for a Shop](https://leetcode.com/problems/minimum-penalty-for-a-shop/)
- We want to find the minimum penalty index, we don't need to know the exact penalty
- We can keep just the relative difference
- Assume index 0 has difference 0

```python
def bestClosingTime(self, customers: str) -> int:
	curpenalty = 0
	ind = 0
	minpenalty = 0
	for i,x in enumerate(customers):
		if x == 'Y':
			curpenalty -= 1
		else:
			curpenalty += 1
		
		if curpenalty < minpenalty:
			ind = i+1
			minpenalty = curpenalty
	return ind
```



## Python

prefix sum
- `[0] + list(accumulate(nums))`
```python
def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
    nums.sort()
    prefix = [0] + list(accumulate(nums))
    for x in queries:
        i = bisect_left(nums, x)
        yield x * (2 * i - len(nums)) + prefix[-1] - 2 * prefix[i]
```
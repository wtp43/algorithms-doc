---
---
# Two pointers

## Subsequences
- Useful for subsequences since order is important unlike subsets
### Largest Subsequence Prefix 
https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/?envType=daily-question&envId=2024-06-03

- [ ] TwoSum: 
Find two elements in an array that sum to the target
- Sort then two pointers
- Or, store the complement in hashset and iterate
- O(n)
- [ ] ThreeSum (Reduces to TwoSum): 
Find three elements in an array that sum to the target
- Sort then run TwoSum starting at i+1 for i in range(n)
- Again, hashset the complement
- O(n)

- [ ] [[LC-189. Rotate Array]]
- k = k mod n
- reverse the entire array
- reverse the first k (0->k-1)
- reverse the last k

- [x] Valid Palindrome 
- Works for both even and odd length palindromes: while i < j
- Check the first and last character, if they don't match it's not a palindrome

- [ ] [[LC-977. Squares of a Sorted Array]] 
- We have a list` [-10,-5,0,1,2,20]` and require a list of squares in sorted order
- Two pointers is very useful here because the list is sorted, and either we take from the front or the back of the list

- [ ] [[LC-1268. Search Suggestions System]]
- Keep a left and right pointer that have the prefix 

## Increasing/Decreasing Sequences
### 2972. Count the Number of Incremovable Subarrays II
- A subarray is incremovable if nums becomes strictly increasing on removing only that subarray
- Find longest increasing seq from the left
- Iterate from the right and find the longest decreasing seq from the right

```python
def incremovableSubarrayCount(self, nums: List[int]) -> int:
	n = len(nums)
	i = res = 0
	# find the longest increasing seq from the start of the arr
	while i+1< n and nums[i] < nums[i+1]:
		i += 1
	# we can delete [i:] from 0 to i+1 inclusive, which equals i+2 possible arrays 
	if i == n-1:
		return n*(n+1)//2
	res = i + 2
	for j in range(n-1, -1,-1):
		#
		while i >= 0 and nums[i] >= nums[j]:
			i -= 1
		if j < n-1 and nums[j] >= nums[j+1]:
			# we have met the longest increasing seq from the right
			break
		res += i+2
	return res
```
---
title:  "Quick Select"
created: 2022-12-10
---

```toc 
style: number 
min_depth: 1 
max_depth: 6
```
# Quick Select

- Time complexity: O(n) on average, O(n2) in the worst case
# Implementation

```python
#k is 0 indexed here
def findKthLargest(self, nums: List[int], k: int) -> int:
    def qselect(nums: List[int], l: int, r: int, k: int) -> None:
        p = partition(nums, l, r)
        
        if p < k: 
            return qselect(nums, p + 1, r, k)
        if p > k: 
            return qselect(nums, l, p - 1, k)
        
        return nums[p]

    def partition(nums: List[int], l: int, r: int) -> int:
        pivot, p = nums[r], r

        i = l
        # find the correct position of nums[p] in the arr[l:r]
        while i < p:
			# if nums[i] is greather than pivot, swap with nums[p-1],
			# then swap nums[p-1] with nums[p]
			# decrement i and p by one since we have reduced the arr size by swapping
            if nums[i] > pivot: 
                nums[i], nums[p - 1] = nums[p - 1], nums[i]
                nums[p], nums[p - 1] = nums[p - 1], nums[p]
                i -= 1
                p -= 1
                
            i += 1

        return p
	#kth largest
    return qselect(nums, 0, len(nums) - 1, len(nums) - k)
    #kth smallest
    return qselect(nums, 0, len(nums) - 1, k)
```

## Optimizations

## Optimized Complexity

>[!Time Complexity]

>[!Space Complexity]



# Related
https://leetcode.com/problems/k-closest-points-to-origin/solutions/1590679/k-closest-points-to-origin/?orderBy=most_votes


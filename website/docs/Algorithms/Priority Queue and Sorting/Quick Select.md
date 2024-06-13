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

# Implementation

```python
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
        while i < p:
            if nums[i] > pivot: 
                nums[i], nums[p - 1] = nums[p - 1], nums[i]
                nums[p], nums[p - 1] = nums[p - 1], nums[p]
                i -= 1
                p -= 1
                
            i += 1

        return p

    return qselect(nums, 0, len(nums) - 1, len(nums) - k)
```

## Optimizations

## Optimized Complexity

:::Time-Complexity[Time Complexity] 


:::

:::Space-Complexity[Space Complexity] 


:::



# Related
https://leetcode.com/problems/k-closest-points-to-origin/solutions/1590679/k-closest-points-to-origin/?orderBy=most_votes


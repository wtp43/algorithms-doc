---
title:  "Interpolation Search"
created: 2022-12-13
---




# Interpolation Search
A fast alternative to a binary search when the elements are uniformly distributed. This algorithm runs in a time complexity of ~O(log(log(n))).  

Binary search always goes to the middle. If the target is closer to the first element, interpolation search will start search toward the beginning


:::important[important] 



:::

# Implementation

```python
class InterpolationSearch():

  def __init__(self):
    pass

  def interpolationSearch(self, nums, val):
    lo = 0
    mid = 0
    hi = len(nums) - 1
    
    while nums[lo] <= val and nums[hi] >= val:
      mid = lo + ((val - nums[lo]) * (hi - lo)) // (nums[hi] - nums[lo])
      if nums[mid] < val:
        lo = mid + 1
      elif nums[mid] > val:
        hi = mid - 1
      else:
        return mid

    if nums[lo] == val:
      return lo
    return -1


if __name__ == '__main__':
  s = InterpolationSearch()
    
  values = [10, 20, 25, 35, 50, 70, 85, 100, 110, 120, 125]

  # Since 25 exists in the values array the interpolation search
  # returns that it has found 25 at the index 2
  print(s.interpolationSearch(values, 25))
  mid = 0 + ((25 - 10) * (10-0)) // (125-10) = 1
  

  # 111 does not exist so we get -1 as an index value
  print(s.interpolationSearch(values, 111))
```

## Optimizations

## Optimized Complexity

:::Time-Complexity[Time Complexity] 

O(log(log(n))) if array is uniformly distributed

:::

:::Space-Complexity[Space Complexity] 


:::

# Related

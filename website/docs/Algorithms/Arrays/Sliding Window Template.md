# LC Templates

## Dp

Dp is about managing states. 
- Use dictionary, arrays


### Bottom up DP 
1. Find recursive relation
	1. Recurse on target (target must thus be outer loop since we are building up answers using target-1)
2. Find base case 
	1. May need to construct extra row for ease of calculation
3. Find edge case
	1. ie: handle impossible cases, input not big enough for target
### Top down


## Sliding Window

### Template 1
Keep L(left side of window) tracker 

1. Remove left element if window already size k
	1. L-R > k
	2. Increment L
2. Add current element
3. Check if conditions are met

Alternative way to store window
- dictionary of {e: ind}

```python
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, n in enumerate(nums):
            if n in d and i - d[n] <= k:
                return True
            d[n] = i
        return False
```
### Template 2
Keep L tracker

1. Update relevant counters
2. Update window (while loop)
	1. Remove left side until constraints are satisfied again
3. Update result if needed







## Graphs

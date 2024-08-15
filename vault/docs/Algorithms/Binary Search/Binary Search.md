---
---
# Binary Search

> [!tip] Intuition
> Can be used when `f(x)` is monotonically increasing/decreasing and the range for which `x` exists on is very large

- Binary Search should be equal to Bisect Left in the case of no duplicates

## Bisect Left
- lo will be the first num $\leq$ x
- Repeatedly move right border towards the left if there are duplicates
- ``if target == arr[mid]: hi = mid-1

```python
def bisect_left(arr, x):
	lo = 0
	hi = len(arr)-1
	while i <= j:
		mid = lo + (hi - lo)//2
		if arr[mid] >= x:
			hi = mid - 1
		else:
			lo = mid + 1
	return lo
```

## Bisect Right
- lo will be the first num > x
- hi will be the greatest num <= x
- ``if target == arr[mid]: lo = mid+1

## Implementation

- Implementation differs only at the equality comparison
- Bisect left:
	- If condition is met:
		- always decrease right
-  Bisect right
	- If condition is met:
		- always increase left

```python
def bisect_left(arr, x):
	lo = 0
	hi = len(arr)-1
	while lo <= hi:
		mid = lo + (hi - lo)//2
    # in bisect left, to return lo, the condition must be strictly > or strictly <
		if arr[mid] < x:
			lo = mid + 1
		else:
			hi = mid - 1
	return lo

lo = first position where arr[lo] > x
hi = position before lo
	lo = 0
	hi = len(arr)-1
	while lo <= hi:
		mid = lo + (hi - lo)//2
		if arr[mid] <= x:
			lo = mid + 1
		else:
			hi = mid - 1
	return lo
```
# Related
## Structure

- The only difference in the following 3 types of binary search is what happens when f(x) is equal to the target
EXCALIDRAW DIAGRAM HERE
### Discrete Binary Search
- Return  
```python


```

### Bisect Left 
- lo will be the first index for which f(lo) <= target 

### Bisect Right
- lo will be the first index for which f(lo) > target 
- hi will be the greatest index for which f(lo) <= target

## Applications

### Replacing DP

#### Minimize Maximum Difference of Pairs

- we don't need DP here because the minimum difference between two pairs occur next to each in a sorted array
- DP solution:
- Binary search
  - Sort (differences will be minimized)
  - Binary search the maximum difference on range (0, max difference of all pairs)

```python
def minimizeMax(self, nums: List[int], p: int) -> int:
	nums.sort()
	lo = 0
	hi = nums[-1]-nums[0]
	n = len(nums)
	while lo <= hi:
		mid = lo + (hi-lo)//2
		cnt = i = 0
		while i < n-1:
			if nums[i+1] - nums[i] <= mid:
				cnt += 1
				## skip the 2nd num used in the pair
				i += 1
			i += 1
		if cnt < p:
			lo = mid+1
		else:
			hi = mid-1
	return lo
	# nLogV + nlogn, V = maximum difference in array,
	# in each step of the binary search (total logV steps)
	# we have to determine how many pairs are valid (n steps)
```
#### [719. Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) 
-  Key: sliding window to calculate distances <= dist
	- O(n) since 
```python
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        lo = 0
        hi = max(nums)
        n = len(nums)
        # sort to calc min distances iteratively
        nums.sort()
        # how many pairs have less distance than cur
        def count(nums, dist):
            ans = i = j = 0
			for j in range(n):
				while nums[j] - nums[i] > dist:
					i += 1
				ans += j-i
            return ans

        while lo <= hi:
            mid = lo + (hi-lo)//2
            if count(nums,mid) < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo 
```

#### Largest Subarray Sum After K Splits
https://leetcode.com/problems/split-array-largest-sum/description/
- Subarray sum is monotonic
- Binary search on minimum sum possible
- Count number of partitions required for current sum limit 

```python
def splitArray(self, nums: List[int], k: int) -> int:
        def count(nums, limit):
            ans = 1
            cur = 0
            for x in nums:
                if cur + x > limit:
                    ans += 1
                    cur = 0
                cur += x
            return ans

        start, end = max(nums), sum(nums)
        while start <= end:
            mid = start + (end-start)//2
            if count(nums, mid) <=  k:
                end = mid-1
            else:
                start = mid+1
        return start
```

#### Kth Smallest Number in Multiplication Table

https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/

```python
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(x):
            ans = 0
            for i in range(1, m+1):
                ans += min(x//i, n)
            return ans
        lo, hi = 1, m*n
        while lo <= hi:
            mid = (lo + hi)//2
            if count(mid) < k:
                lo = mid+1
            else:
                hi = mid-1
        return lo
```


## Binary Search + Greedy
>[!intuition] Tip
>Greedy: Greedily find the first strongest worker that can complete task[j]. If it isn't possible check if it is possible with pills.
>The best worker[i] to increase is not the weakest one or the strongest one but the one with smallest difference = task[j]-worker, for a worker that has not yet been assigned. Use bisect_left and SortedList with O(logn) removal from a list). 
https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/
```python
# sorted list has removal in logn
from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(workers)
        tasks.sort()
        workers.sort()
        def valid(k):
            # take k strongest workers
            W = SortedList(workers[n-k:])
            p = pills
            # we cannot greedily assign the pills
            # have to search for the smallest (strength + workers[i] that is greater than the current task)
            for t in tasks[:k][::-1]:
                #limit search to workers[x:n-x]
                ind = W.bisect_left(t)
                if ind < len(W):
                    W.pop(ind)
                elif p > 0:
                    ind = W.bisect_left(t - strength)

                    if ind < len(W):
                        W.pop(ind)
                        p -= 1
                else:
                    return False
            return len(W) == 0

        lo,hi = 0, min(len(workers), len(tasks))
        while lo <= hi:
            mid = (lo+hi)//2
            if valid(mid):
                lo = mid+1
            else:
                hi = mid-1
        return hi
```


### Median of Two Sorted Arrays

https://leetcode.com/problems/median-of-two-sorted-arrays/description/

- O(m+n): Merge both arrays and then binary search
- O(log(m + n)): smart binary search
  https://leetcode.com/problems/median-of-two-sorted-arrays/editorial/


### Practice Problems

#### Kth Smallest Amount With Single Denomination Combination

https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

```python
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        d = defaultdict(list)
        # lcm of all combinations: O(2**n)
        for i in range(1, n+1):
            for comb in itertools.combinations(coins, i):
                d[len(comb)].append(math.lcm(*comb))

        def count(d, target):
            ans = 0
            for i in range(1, n+1):
                for lcm in d[i]:
                    ans += target // lcm * pow(-1, i+1)
            return ans
        start, end = min(coins), min(coins) * k
        while start<= end:
            mid = (start + end) // 2
            c = count(d, mid)
            if c >= k:
                # continue iterating until we find a valid number
                end = mid -1
            else:
                start = mid+ 1
        if count(d, start) >= k:
            return start
        else:
            return end
```






- [ ] [[LC-1752. Check if Array Is Sorted and Rotated]] (Find the pivot if sorted array is rotated)
- Important to note that the first and last num are connected
- Check if the next number is bigger: This can only happen once if sorted and rotated
	- nums[i] > nums[(1+i)%n]


- [ ] [[LC-153. Find Minimum in Rotated Sorted Array]]
- Update the min every loop. The min will not always land on j or always on i
- `If nums[j] > nums[mid]: the min has to be on the left


- [ ] [[LC-33. Search in Rotated Sorted Array]]

>[!danger]+ Intuition
>   enumerate possibilities
> 
1. `we are in the left portion ([6789] 123)
	    - `target > nums[mid]: i=mid+1
	    - ``nums[i] <= target < nums[mid] j=mid-1
	    - `target < nums[i]: i=mid+1
2. `we are in right portion (78 [123])
		- `target < num[mid]: j=mid-1
		- `nums[mid] < target <= nums[j]: i=mid+1
		- `target > nums[j]: j=mid-1

- [ ] [[LC-74. Search a 2D Matrix]]

- [ ] [[LC-981. Time Based Key-Value Store]]
- We want to store multiple values with different timestamps for the same key
- We notice that since time is strictly increasing, our list of values will in sorted order
- Create a dictionary of lists and binary search on the list

- [ ] [[LC-34. Find First and Last Position of Element in Sorted Array]]
- Left and right bisect essentially move the same way when target != `nums[mid]
- The only difference is when the target == `nums[mid]
- Left bisect will set j = mid-1 and move left 
- Right bisect will set i = mid+1 and move right

- [ ] [[LC-1268. Search Suggestions System]]
- Suggest at most 3 words based on the prefix
- Sort strings then bisect left on the prefix 

- [ ] [[LC-2563. Count the Number of Fair Pairs]]
	- Find pairs (i,j) where lower <= nums[i] + nums[j] <= upper
	- Bisect_left and bisect_right on index i+1 with upper-nums[i] and lower-nums[i]
	- res += r-l. There isn't a +1 here because r is the first index where i is > upper-nums[i]

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/solutions/2934252/capacity-to-ship-packages-within-d-days/

[Koko eating bananas](https://leetcode.com/problems/koko-eating-bananas/)  
[Minimum number of days to make m bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)  
[Magnetic force between two balls](https://leetcode.com/problems/magnetic-force-between-two-balls/)  
[Split array largest sum](https://leetcode.com/problems/split-array-largest-sum/)  
[Divide chocolate (for premium users only)](https://leetcode.com/problems/divide-chocolate/)  
[Cutting ribbons (for premium users only)](https://leetcode.com/problems/cutting-ribbons/)
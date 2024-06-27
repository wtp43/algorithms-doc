---
---
# Prefix Sums/ Frequency Map

- Store some 'useful value' for all prefixes in an array
- Don't forget the base cases for the prefix sums
- Not applicable for subsequences
- Useful for subarray problems

> [!tip] Intuition 
> Can be used to find max/min of some f(subarray) for all subarrays in O(n) 

## Prefix Sum + Hash Map
> Check if a prefix exists in the hash map
> Storing indices or counters may be helpful
### [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
```python
def subarraySum(self, nums: List[int], k: int) -> int:
	prefix_sums = Counter()
	prefix_sums[0] = 1
	cur = 0
	count = 0
	for i in range(len(nums)):
		cur += nums[i]
		count += prefix_sums[cur-k]
		prefix_sums[cur] += 1
	return count

```

- Reduces to subarray sum equals k. 
- Initialize `prefix_sums[0] = 1` for the case that we use the entire prefix_sum

### [Longest Subarray with Sum k = 1](https://leetcode.com/problems/longest-well-performing-interval/)
- Categorize elements as either 1 or -1 
- key = prefix sum
- val = earliest index
```python
# We want the longest subarray where the elements > 8 are strictly more than the elements that are <= 8
def longestWPI(self, hours: List[int]) -> int:]
        prefix = defaultdict(int)
        cur = res = 0
        for i,h in enumerate(hours):
            cur += 1 if h > 8 else -1
            if cur > 0:
                res = max(i+1, res)
            if not prefix[cur]:
                prefix[cur] = i+1
            if cur-1 in prefix:
                res = max(res, i-prefix[cur-1]+1)
        return res
```

### [Find Subarray with Sum Divisible by K with at Least 2 Elements](https://leetcode.com/problems/continuous-subarray-sum/)
- Check if there is a previous subarray with remainder equal to the current remainder
- Check if this subarray is at least length 2
- Why does this work? we can omit the prefix subarray to get a subarray with remainder 0
```python
def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = defaultdict(lambda: math.inf)
        prefix[0] = -1
        cur = 0
        for i in range(len(nums)):
            cur = (cur + nums[i])%k
            if cur in prefix:
                if prefix[cur]+1 < i:
                    return True
            else:
                # we only want the earliest occurrence of the subarray
                prefix[cur] = i
        return False
```


### [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)
- key = prefix sum
- val = index
```python
def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        cur = 0
        maxlen = 0
        prefix_sum[0] = -1
        for i in range(len(nums)):
            cur += nums[i]
            if cur-k in prefix_sum:
                maxlen = max(maxlen, i-prefix_sum[cur-k])
            if cur not in prefix_sum:
                prefix_sum[cur] = i
        return maxlen
```

### [Minimum Operations to Make All Array Elements Equal](https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/)
![[Pasted image 20240604181855.png]]
Source: https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/solutions/3341928/c-java-python3-prefix-sums-binary-search/

- Store prefix sum
- Since q can be greater than n, it would be useful to 1 index the prefix sums

```python
def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefix = [0]*(n+1)
        prefix[1] = nums[0]
        for i in range(1,len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        res = []
        for q in queries:
            i = bisect_left(nums, q)
            res.append((q*i - prefix[i]) + (prefix[n]-prefix[i] - q*(n-i)))
        return res
```

### Find Subarray with Bitwise & Closest to K
https://leetcode.com/problems/find-subarray-with-bitwise-and-closest-to-k/description/
- & property: monotonically decreasing
- Sliding window + frequency map to store all ith bits
- Decrease window if mask < k, frequency map helps restore the ith bit to 1 if the freq[i] == j-i, where j-i is the length of the decreased window length



## Difference Array + Binary Search
- Prefix sum for differences

```python
def minimumDifference(self, nums: List[int], k: int) -> int:
        res = abs(nums[0]-k)
        mask = nums[0]
        freq = [0]*32
        i = 0
        # freq map is helpful to restore bitmask
        for j in range(len(nums)):
            for ind in range(32):
                if nums[j] & 1<<ind:
                    freq[ind] += 1
            mask &= nums[j]
            res =min(res, abs(mask-k))
            while mask < k and i < j:
                for ind in range(32):
                    if nums[i] & 1<<ind:
                        freq[ind] -= 1
                    if freq[ind] == j-i:
                        mask |= 1<<ind
                res =min(res, abs(mask-k))
                i += 1
        return res
```

### Tracking Valid Subarrays

### Max/Min 'f(x)' of Subarray

### Sum of Distances

https://leetcode.com/problems/sum-of-distances/description/

- Store occurrences/indices in dictionary
- Iterate all indices of each key in the dictionary
- Build prefix and suffix sum for each key
- Complexity: O(n) for each number + O(n) to sum

```python
def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)

        arr = [0]*len(nums)
        for x in d:
            prefix = 0
            suffix = sum(d[x])
            n = len(d[x])
            p = 0
            for i in d[x]:
                arr[i] = i*p-prefix + suffix-i*(n-p)
                p += 1
                prefix += i
                suffix -= i
        return arr
```

### [Max Partitions Allowed to Make Sorted Array](https://leetcode.com/problems/max-chunks-to-make-sorted-ii/)
> Split arr into maxiumum number of individually sorted partitions such that concatenated array is also sorted
- Notice that a partition is only possible if the maximum in the prefix subarray is less than the minimum in the suffix subarray

```python
def maxChunksToSorted(self, arr: List[int]) -> int:
        # a partition can be made if
        # max[:i+1] < min[i+1:]
        
        n = len(arr)
        minSuffix = [math.inf]*(n)
        minSuffix[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            minSuffix[i] = min(arr[i], minSuffix[i+1])
        
        maxPrefix = 0
        partition = 1
        for i in range(n-1):
            maxPrefix = max(maxPrefix, arr[i])
            if maxPrefix <= minSuffix[i+1]:
                partition += 1
        return partition

```

## Tracking Multiple Prefixes
### Count Triplets
https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

- Use one map to store number of occurrences
- Use another map to store the 'total contributions' of the previous occurrences
	- Here, we want the lengths of all previous subarrays that have the same prefix
	- We can do so by storing the cumulative distance of all x's to 0

```python
def countTriplets(self, arr: List[int]) -> int:
        res = 0
        prefix = 0
        # Store occurences
        count = defaultdict(int)
        # Base case: The current array[:i] satisfies the requirement
        count[0] = 1
        # Store cumulative distance from 0 to ith element where key = prefix[i]
        indices_sum = defaultdict(int)

        # Iterating through the array
        for i in range(len(arr)):
            prefix ^= arr[i]
            res += count[prefix] * i - indices_sum[prefix]

            # ---x----x----x
            # ---i----j-----k:
            # to get m's contribution :
            # k-i-1 + j-j-1
            # -1 because i < j <=k, so we can't pick i to be j 

            # Updating total count of current XOR value
            indices_sum[prefix] += i+1
            count[prefix] += 1
        return res
```

## Sweep Line
> O($n$) 
- Initiate delta array
- Store all delta changes at the boundary of ranges
- Increment x at start of range
- Decrement x at end of range
- Sweep deltas and keep the running sum
### [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/)

```python
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Total seats:         10  55  45  25  25
Hence, answer = [10,55,45,25,25]

def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
	res = [0]*(n+2) # since bookings is 1 indexed and j+1 can happen for index n-1

	for i,j,x in bookings:
		res[i] += x
		res[j+1] -= x

	cur = 0
	for i in range(1, n+1):
		cur += res[i] 
		res[i] = cur

	return res[1:n+1]
```

## Storing Prefix States

### [Minimum Number of K Consecutive Bit Flips](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/)

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.
- Continuously flip the leftmost bit
- It is not possible if there are still 0s in the last k window after flipping all bits to the left.

```python
def minKBitFlips(self, nums: List[int], k: int) -> int:
        cur = res = 0
        state = [0]*len(nums) 
        for i,x in enumerate(nums):
            if i >= k:
	            # clear the action by the element last previously inside the window
	            # for a window of size k, it's elements are [1..k] inclusive
	            # So we XOR the state of the element at 0
                cur ^= state[i-k]
            if cur == nums[i]:
                if (i+k>len(nums)):
                    return -1
                state[i] = 1
                cur ^= 1
                res += 1
        return res
```
---
---
# Monotonic Queue
MQ is mostly used as a dynamic programming optimization technique and for some problems where it is applicable we can reduce the reasoning to finding the nearest (biggest, smallest) element.
Before stepping into more interesting problems let’s glance at a different approach to search for nearest values. We will be using an array to keep indexes of nearest biggest values. This algorithm was invented not too long ago by Jérémy Barbay and Johannes Fischer, you can find a paper describing it in full [here](https://arxiv.org/abs/1009.5863).

The idea is to store the index j of the preceding smaller value of the ith value A[i] in P[i], where P is an array of preceding smaller value indexes:

for i from 1 to n:  
    j = i-1  
    while A[j] >= A[i]:  
        j = P[j]  
    P[i] = j

Before actually adding an element to the queue, we remove values which are smaller than the current value, this way we can keep a non-increasing sequence.

- [ ] [[LC-739. Daily Temperatures]]

- [ ] [[LC-862. Shortest Subarray with Sum at Least K]] (MONOQUEUE + PREFIX SUM)
- subarray is contiguous
- contains negative numbers
- maintain the (index, prefixsum from 0 to index) in a monoqueue
- when the prefix sum is smaller than the last prefix sum in the monoqueue, pop the last element
- what we are checking every time is the current prefix sum - prefix sum ending at i
- so in the second while loop, the subarray with the smaller prefix sum is preferred because it has a larger index (resulting in a smaller window in the future) and a smaller prefix sum (resulting in a larger sum in the future)
- we need to keep a monotonically increasing sequence of prefix sums 
- we cannot keep individual elems in the queue because there exists negative numbers
- (2,-1,3) will not work if we just extend the start after finding a sum that's at least k
- we have to keep prefix sums instead to get pass negative numbers
**Why do we have a prefix array and not just the initial array like in sliding window :**  
Because in the sliding window when we move `start` (typically when we increment it) we can just substract `nums[start-1]` from the current sum and we get the sum of the new subarray. Here the value of the `start` is `jumping` and one way to compute the sum of the current subarray in a `constant` time is to have the prefix array.
```python
 def shortestSubarray(self, A, K):
        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        for i, a in enumerate(A):
		    # prefix sum
            cur += a
            # d[0][1] is the prefix sum that ends at 
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            # we must have encountered a negative number
            # we are considering the start 
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return res if res < float('inf') else -1
```


- [ ] [[LC-1425. Constrained Subsequence Sum]]
	- Find the maximum sum of a non-empty subsequence such that every two consecutive integers in the subsequence nums(i) and nums(j) for i < j satisfies j-i <= k
	- This reduces to a DP problem. Include or not include the current num. Try to find a recurrence relation
	- The recurrence relation is ``dp[i+K] = nums[i+K] + max(0, dp[i], dp[i+1], ..., dp[i+K-1])``
	- It will be useful for us to find the maximum sums for the last k-1 subsequences that end on i for i in range(i,k)
	- Monoqueue is able to optimize the DP solution because we are limited to finding the nearest value(maximum or minimum) in building 
	- Longest Palindromic Substring must expand around the center for n centers


https://medium.com/algorithms-and-leetcode/monotonic-queue-explained-with-leetcode-problems-7db7c530c1d6
https://iq.opengenus.org/monotonic-queue/
https://labuladong.gitbook.io/algo-en/ii.-data-structure/monotonic_queue
https://algo.monster/problems/mono_stack_intro
https://1e9.medium.com/monotonic-queue-notes-980a019d5793
https://leetcode.com/problems/constrained-subsequence-sum/solutions/597751/java-c-python-o-n-decreasing-deque/
- [ ] https://leetcode.com/problems/constrained-subsequence-sum/description/
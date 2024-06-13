---
dg-publish: true
title:  "Advanced Questions"
created: 2023-01-29
---

# Todo
https://leetcode.com/problems/maximum-average-pass-ratio/description/
https://leetcode.com/problems/minimum-operations-to-halve-array-sum/description/
https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
# Binary Search
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
https://leetcode.com/problems/split-array-largest-sum/description/


# Dynamic Programming

https://leetcode.com/problems/concatenated-words/description/
https://leetcode.com/problems/distinct-subsequences/
- [ ] https://leetcode.com/problems/4sum/submissions/
- [ ] https://leetcode.com/problems/word-ladder/description/

# Graphs

[LC-305. Number of Islands II](</docs/Some Leetcode Questions/LC-305. Number of Islands II.md>)- grid of 0's initially, Perform land operations which turns water to land, Return number of islands
- Instead of storing parents as a 2d grid, we can store their land position as $i*n + m$
- Components: either dfs or union find (faster than dfs)
- Initializing the parent and rank arrays is O(mn)
- Store the number of connected components and decrement it every time a valid union-set is completed.

# Heap
[LC-23. Merge k Sorted Lists](</docs/Some Leetcode Questions/LC-23. Merge k Sorted Lists.md>)- Put the head of each linked list on a heap
- Extend the resulting linked list
- If the extended tail has a next node, put it back on the heap

[LC-1851. Minimum Interval to Include Each Query](</docs/Some Leetcode Questions/LC-1851. Minimum Interval to Include Each Query.md>)- Find the smallest interval that can include each query (array of nums)
- Sort queries and intervals
- Put all intervals ``[l,r]`` that include q onto the heap with key ``[l-r+1, r]``
- Pop all intervals where `r` < q
- Store results in dictionary because we sorted our input 

https://leetcode.com/problems/the-skyline-problem/description/


# Sliding Window
- Sum of window and prefix sums are useful
- <mark style="background: #FFB86CA6;">What is the state of the window we need to keep track of?</mark>

Check validity of window

## Template 1: Sliding Window (Shrinkable)
- The window is kept valid at the end of each outer for loop
```cpp
int i = 0, j = 0, ans = 0;
for (; j < N; ++j) {
    // CODE: use A[j] to update state which might make the window invalid
    for (; invalid(); ++i) { // when invalid, keep shrinking the left edge until it's valid again
        // CODE: update state using A[i]
    }
    ans = max(ans, j - i + 1); // the window [i, j] is the maximum window we've found thus far
}
return ans;
```



https://leetcode.com/problems/frequency-of-the-most-frequent-element/
[LC-1838. Frequency of the Most Frequent Element](</docs/Some Leetcode Questions/LC-1838. Frequency of the Most Frequent Element.md>)- Return the maximum possible frequency of an element after performing at most k operations (increment the element at index i by 1)
- Sliding window problem,  
- the key is to find out the valid condition: 
- `k + sum >= size * max`  
	- if this is true, we can extend the window further
- which is  
- `k + sum >= (j - i + 1) * A[j]`
- window is not valid if (we do not have enough operations to change all numbers into `A[j])
	- sum + k < (j - i + 1) * `A[j]`
- Sort so we can deal with adjacent numbers easily

```cpp
// OJ: https://leetcode.com/problems/frequency-of-the-most-frequent-element/
// Author: github.com/lzl124631x
// Time: O(NlogN)
// Space: O(1)
class Solution {
public:
    int maxFrequency(vector<int>& A, int k) {
        sort(begin(A), end(A));
        long i = 0, N = A.size(), ans = 1, sum = 0;
        for (int j = 0; j < N; ++j) {
            sum += A[j];
            while ((j - i + 1) * A[j] - sum > k) {
	            sum -= A[i++];
            }
            ans = max(ans, j - i + 1);
        }
        return ans;
    }
};
```

## Template 2: Sliding Window (Non-shrinkable) - faster than shrinkable
- Grow the window when it's valid, shift the window when it's invalid (1 for loop)
- The first valid window is kept constant and moved ahead. If we get any new valid window greater than the existing window then we increment the window length which was kept in the existing loop.
```cpp
// OJ: https://leetcode.com/problems/frequency-of-the-most-frequent-element/
// Author: github.com/lzl124631x
// Time: O(NlogN)
// Space: O(1)
class Solution {
public:
    int maxFrequency(vector<int>& A, int k) {
        sort(begin(A), end(A));
        long i = 0, j = 0, N = A.size(), sum = 0;
        for (; j < N; ++j) {
            sum += A[j];
            if ((j - i + 1) * A[j] - sum > k) sum -= A[i++];
        }
        return j - i;
    }
};
```


[[LC-2302. Count Subarrays With Score Less Than K]]

-   1425.  [Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/discuss/597751/JavaC++Python-O(N)-Decreasing-Deque)
-   1358.  [Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/516977/JavaC++Python-Easy-and-Concise)
-   1248.  [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC%2B%2BPython-Sliding-Window-atMost(K)-atMost(K-1))
-   1234.  [Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/discuss/408978/javacpython-sliding-window/367697)
-   1004.  [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC%2B%2BPython-Sliding-Window)
-   930.  [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/discuss/186683/)
-   992.  [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window)


# Stacks

## Monotonic Stacks

[LC-862. Shortest Subarray with Sum at Least K](</docs/Some Leetcode Questions/LC-862. Shortest Subarray with Sum at Least K.md>)- subarray is contiguous
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



## Monotonic Queue
https://leetcode.com/problems/4sum/submissions/
https://leetcode.com/problems/minimum-interval-to-include-each-query/
https://leetcode.com/problems/word-ladder/description/




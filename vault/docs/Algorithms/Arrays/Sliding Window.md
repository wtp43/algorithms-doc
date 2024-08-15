---
---
# Sliding Window
- Sum of window and prefix sums are useful
- What is the state of the window we need to keep track of?


> [!note] Sliding Window Restriction
> Sliding window only works for positive numbers as it assumes increasing the window size will also increase the current counter.

Check validity of window.
The number of starting positions for the window is the number of elements in the array = j-i+1

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
[[LC-1838. Frequency of the Most Frequent Element]] (Shrinkable Window)
- Return the maximum possible frequency of an element after performing at most k operations (increment the element at index i by 1)
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

### [2799. Count Complete Subarrays in an Array](https://leetcode.com/problems/count-complete-subarrays-in-an-array/)
- Count the number of subarrays that has all the distinct elements in the entire array
- The key to prevent double counting is to add all the valid subarrays ending at the current position
- 
```python
def countCompleteSubarrays(self, A: List[int]) -> int:
	n, k = len(A), len(set(A))
	res = i = 0
	count = Counter()
	for j in range(n):
		count[A[j]] += 1
		# Find the smallest valid subarray that ends at j
		# Then the start indices of all the valid subarrays is [0...i] 
		while len(count) == k:
			count[A[i]] -= 1
			if count[A[i]] == 0:
				del count[A[i]]
			i += 1
		res += i
	return res
```
- [ ] https://leetcode.com/problems/substring-with-concatenation-of-all-words/
- [ ] [[LC-2302. Count Subarrays With Score Less Than K]]

- [ ]   1425.  [Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/discuss/597751/JavaC++Python-O(N)-Decreasing-Deque)
- [ ]   1358.  [Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/516977/JavaC++Python-Easy-and-Concise)
- [ ]   1248.  [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC%2B%2BPython-Sliding-Window-atMost(K)-atMost(K-1))
- [ ]   1234.  [Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/discuss/408978/javacpython-sliding-window/367697)
- [ ]   1004.  [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC%2B%2BPython-Sliding-Window)
- [ ]   930.  [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/discuss/186683/)
- [ ]   992.  [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window)

##  Advanced: Sliding Window + DP
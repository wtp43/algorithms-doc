---
---
---
 Jan 2024
# Misc Math
- Minimum sum path
	- Watch out for input constraints (especially if negative numbers exist)
	- Watch out for cycles
## Recursion 
Tail end recursion:pass computations as function argument
## Arrays 

- hashmaps are generally useful for storing some kind of ordering

- longest consecutive subsequence in unsorted array
	- ie: 3, 100, 200, 2, 1, 4
	- o(n): store all numbers into a set
	- build subsequence by checking if the number to the left exists
	- optimization: only start building at numbers that could be a starting point
		- ie: no numbers to the left of it
	- start building sequence if the number to the left doesn't exist
		- search for next number (n+length) in set 
	- update max length

- longest common prefix

## Sliding Window
[1838. Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)

- sort so that the next element is guaranteed to be bigger
	- we know that we are always operating on the next biggest num
- update current sum
- update window if 
```python
def maxFrequency(self, nums: List[int], k: int) -> int:
		# we always have to check every element
		# sum is helpful here
		# increase window if operations are in excess (sum + k < window size * current element to be checked)
		# window only works here since we sorted
        nums.sort()
        max_freq = 0
        L = 0
        cur_sum = 0
        for R in range(len(nums)):
            cur_sum += nums[R]

            # update window
            while cur_sum + k < nums[R] * (R-L+1):
                cur_sum -= nums[L]
                L +=1
            max_freq = max(max_freq, R-L+1)
        
        return max_freq

```


## Union- find
- Path compression find: O(log(logn))
- Merge parents


## Dynamic Programming

Iterative DP
- Construct array such that first row/base case aids in computation
- Constructing recursive relation will help in loop ordering
### LC-1230. Toss Strange Coins
- Return the probability that the number of coins facing heads equals `target` if you toss every coin exactly once.
- The `i`-th coin has a probability `prob[i]` of facing heads when tossed.

- outer loop: prob length
- inner loop: target

- Recursive relation:
	- let i = current coin
	- let j = current target
	- roll heads 
		- p(i) x p(j-1 heads in the first i-1 coins)
	- don't roll heads
		- 1-(p(i)) x p(j heads in first i-1 coins )
**Notice that the recursive relation relies on coin array size**
- this is a hint that you need the answers for i-1 coins must be computed first

The optimal substructure here is that once you have solution for first `i` coins, you can extend it for `i+1` coins.
But when you flip the order of execution of loops, this substructure property does not hold. In this case, you are first calculating the number of ways to form amount `i` using all the coins and extending it to find the number of ways to form amount `i+1`, for which the optimal substructure property does not hold true.


### Path Traversal 
https://leetcode.com/problems/minimum-path-sum/
- 1D DP is possible, store row values

### Interleaving String
String traversal empty cases
 - empty string should be true

### Buying and selling stock 2
**Finite State Machine**
- with 1 day cooldown after selling

#### Maximal Square
https://leetcode.com/problems/maximal-square/description/?envType=study-plan-v2&envId=top-interview-150
- Square area: min(diag, left, up) of ones
- 1d array possible: diag needs to be stored in a temp variable
- up_j is just the current dp(j) before it is updated
- update prev_row_j = temp at the end
- make sure to reset/update dp(j) to 0 since we only have a 1d arrayL

# TODO

- 1d DP for path traversal + interleaving string 

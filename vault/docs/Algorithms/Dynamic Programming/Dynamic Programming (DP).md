---
---

# Dynamic Programming
- [ ] 01 Knapsack
	- [ ] [[LC-2008. Maximum Earnings From Taxi]]



- [ ] https://leetcode.com/problems/minimum-cost-to-split-an-array/description/
https://leetcode.com/problems/minimum-cost-to-split-an-array/solutions/3083850/python3-dp/

- [ ] [[LC-472. Concatenated Words]]
- https://leetcode.com/problems/concatenated-words/solutions/2822170/concatenated-words/?orderBy=most_votes
Why sliding window wouldn't work here:
- There is no window of k for our solution
	- The size of k will not encompass all the substrings that a word may contain
	- we need to do more comparisons
- Sorting does not allow us to find the answer in O(1)
	- we realize that we have to check more than just the word at the start of the window

- [ ] [[LC-115. Distinct Subsequences]]

- [ ] https://leetcode.com/problems/longest-increasing-subsequence/
- [ ] [[LC-2218. Maximum Value of K Coins From Piles]]

- [ ] [[LC-139. Word Break]]
	- Can the string be built using words that exist in the dictionary
	- We want dp to store the states from 0 to n+1 because a 
	- Iterate for each start index of the string
		- Iterate for all words in the dictionary
	- State[i] = whether the string up to index i can be constructed using words form the dictionary
	- State[i] = s[i-len(w):i] == w and dp[i-len(w)]
- [ ] [[LC-5. Longest Palindromic Substring]]
	- State`[i][j]` = 1 if the str from i to j is a palindrome
	- State`[i][j]` = s`[i] == s[j] and state[i+1][j-1]
	- Using a bottom up approach, we have to have already calculated state`[i+1][j-1]
	- So the loop structure should be 
```python
for i in reversed(range(n)):
	for j in (i+1, n):
```

- [x] [[LC-322. Coin Change]]


- [ ] [[LC-152. Maximum Product Subarray]]
- Can contain negative numbers
- Maintain the cur_max and cur_min
- When there is a negative number, they will swap
- If the number is 0, we restart our product
- Update the max_so_far after each iteration

- [ ] [[LC-300. Longest Increasing Subsequence]]
	- Recurrent relation: `dp[i] = max(dp[i], dp[j] + 1)` for j = 0..i-1

[[LC-416. Partition Equal Subset Sum]]
- Subset sum (01 knapsack)
[[LC-474. Ones and Zeroes]]
- Iterating each word will allow us to save space so we don't have to recount the number of 0's and 1's in each word
- Consider only the possible indices we have to check
- In this case # of 0s...m, # of 1s...n
- We also want to iterate backwards, range(n,`A[0]`-1,-1), because we do not want to rewrite previous calculations by including the previous string. Doing this bottom up may result in duplicated count of the current word

[[LC-120. Triangle]]
- <mark style="background: #cc085d;">Prove validity of assumptions!! </mark>
- This immediately suggests that we should be working from top to bottom. But is this actually necessary? Could we go from bottom to top instead? Going top to bottom results in paths where some cells can take two paths while others only one. Going bottom up, every cell will have two paths they can take. 

[[LC-740. Delete and Earn]]
- Reduces to [[LC-198. House Robber]]
- If we take `nums[i]`, we delete all `nums[i-1], nums[i+1]`
- Key takeaway: We never have to worry about `nums[i+1]`
	- Always only use the past. Never worry about the future results.
	- If we take `nums[i+1]`  in the future, that step wouldn't let us take `nums[i-1]` which is our current num
- Think about which nums would be optimal?
	- Suppose we take `nums[i]`, which number should we take next?
		- It would make sense to take all numbers=`nums[i]` since we paid the cost of deleting it's adjacent numbers.
- How do we access the previous key of a dictionary since we can't index it?
	- Store all the keys in an array

[[LC-256. Paint House]]
- First determine the recurrence relation:
	- `dp[i][j] = min(dp[i], costs[i][j] + min(dp[i])`

- [ ] [[LC-1143. Longest Common Subsequence]]
	- It's important to recognize that the rows and cols are interchangeable here.
	- To optimize space, we only need to store 2 rows with min(len(s1), len(s2)) cols.
	- If s1(i) == s2(i): we can increment `dp[i-1][j-1]`
	- else: `max(dp[i%2][j-1], dp[(i-1)%2][j])`
	- `return dp[n%2][m]` : Make sure to check whether to return (n%2) or (n-1)%2. Do an example (len(s1) == 1 vs len(s1) == 0)
- [ ] [[LC-518. Coin Change II]]
	- to optimize space, we realize that we only need a 1D array with length amount+1
	- we cannot loop the amount by all coins (coins in the inner loop) because we would get permutations
		- consider amount = 7 with coins `[2,5]`: using all coins, `dp[7] = dp[7-5] + dp[7-2]`
		- by looping on coins first, we preserve the above DP definition as `dp[j]="number of ways to get sum 'j' using 'previous /first i coins'
		- by looping coins first, we are fixing the order of the coins in the combination
		- Note: the loop order doesn't matter if we use a 2D array. 
- [[LC-377. Combination Sum IV]]
	- Get permutation of coins that make the sum
	- We can optimize this by sorting the coins in ascending order and breaking out of the inner loop if the amount is smaller than the current coin

# Advanced DP

- [ ] [[LC-2218. Maximum Value of K Coins From Piles]]
- https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/solutions/1889647/python-bottom-up-dp-solution/
- https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/solutions/1887010/java-c-python-top-down-dp-solution/?orderBy=most_votes
- https://leetcode.com/problems/split-array-largest-sum/description/


# Pattern Recognition
Generally we want to find some kind of pattern that holds true in every subset.
Then prove it (by induction).
- ie: We notice that all the elements used to build our window are the maximum in the last k elements
# Memoization
[[0-1 Knapsack#Memoization]] 
- Bottom up dynamic programming that only uses O(n) space

Always consider the state of each `dp[i][j]`
- Like in [[LC-474. Ones and Zeroes]]
- `dp[i][j]` is a different state for every new word
- To avoid duplicates, we have to iterate backwards when updating max subsets
- Otherwise, if we do it bottom up, we may end up using the same word twice

Usually, if we want the reuse the input array, we have to traverse backwards.


**Interview Tip: In-place Algorithms**

In-place algorithms overwrite the input to save space, but sometimes this can cause problems. Here are a couple of situations where an in-place algorithm might not be suitable.

1. The algorithm needs to run in a _multi-threaded_ environment, without exclusive access to the array. Other threads might need to read the array too, and might not expect it to be modified.
2. Even if there is only a single thread, or the algorithm has exclusive access to the array while running, the array might need to be reused later or by another thread once the lock has been released.

In an interview, you should always check whether or not the interviewer minds you overwriting the input. Be ready to explain the pros and cons of doing so if asked!



# DP + Sliding Window

https://leetcode.com/problems/maximize-win-from-two-segments/solutions/3141449/java-c-python-dp-sliding-segment-o-n/?orderBy=most_votes
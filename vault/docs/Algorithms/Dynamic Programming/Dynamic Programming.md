---
title:  "Dynamic Programming"
created: 2023-01-31
---
## Dynamic Programming
>Dynamic Programming is an algorithmic paradigm that solves a given complex problem by breaking it into subproblems using recursion and storing the results of subproblems to avoid computing the same results again. For DP to work, the following properties must be true for the problem.
-   **Overlapping Subproblems** 
	- A problem is said to have overlapping subproblems if the problem can be broken down into subproblems which are reused several times or a recursive algorithm for the problem solves the same subproblem over and over rather than always generating new subproblems.
-   **Optimal Substructure**
	- A problem is said to have optimal substructure **if an optimal solution can be constructed from optimal solutions of its subproblems**.
	- The decisions we make depends on previously made decisions, which is very typical of a problem involving subsequences.

>[!note] Intuition
>Useful for subsequences or when there is no greedy solution. DP problems are essentially graph problems where the edges are not given to you.


## List of Common Problems
> Problems for which Greedy don't work for. Build intuition by using good test cases.
- 0-1 Knapsack
- Subset Sum
- Longest Increasing Subsequence
- Minimum Set/Vertex Cover
	- Test case `[0-3, 1-6, 4-7]`
	- Greedy would take `1-6` first resulting in a suboptimal covering
- Counting all possible paths from top left to bottom right corner of a matrix
- Longest Common Subsequence
- Longest Path in a Directed Acyclic Graph (DAG)
- Coin Change
- Longest Palindromic Subsequence
- Rod Cutting
- Edit Distance
- Bitmask Dynamic Programming
- Digit Dynamic Programming
- Dynamic Programming on Trees


## Subsequences
#### Longest Increasing Subsequence (LIS)

- DP: 0(n^2)
- Approach 1: Build LIS
- Approach 2: Binary search for first position cur num is smaller than `sequence[i]`

```python
def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)

def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for i in range(len(nums)):
            if not seq or nums[i] > seq[-1]:
                seq.append(nums[i])
            else:
                ind = bisect_left(seq, nums[i])
                seq[ind] = nums[i]
        return len(seq)
```

```python
def longestPalindromeSubseq(self, s: str) -> int:
	# current letter + longest palindrome subsequence of array of size 1 smaller
	# how to make a palindrome with the current letter:
	# find letter equal to current letter in a[0:i]
	# dp will be 2 + a[start+1:end-1] or max of subproblems(prefix and suffix with length of 1 smaller)

	n = len(s)

	dp = [[0]*n for _ in range(n)]

	for end in range(n):
		dp[end][end] = 1
		for start in range(end-1, -1, -1):
			if s[start] == s[end]:
				dp[start][end] =  2 + dp[start+1][end-1]
			else:
				dp[start][end] =max(dp[start][end-1], dp[start+1][end])

	return dp[0][-1]
```

#### Length of Longest Subsequence that Sums to Target

https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

- Similar to coin change problem
- Base case: sum 0 has subsequence length 0
- Iterate over nums, update dp for num to target

```python
def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        res = 0
        n = len(nums)
        dp = [-math.inf]*(target+1)
        dp[0] = 0
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = max(dp[i], dp[i-num]+1)
        return dp[target] if dp[target] != -math.inf else -

# Coin Change
def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if c > i:
                    continue
                dp[i] =  min(dp[i], dp[i-c] + 1)
        return dp[-1] if dp[-1] != math.inf else -

```

## Largest Subset
### Largest Divisible Subset
https://leetcode.com/problems/largest-divisible-subset/

```python
def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        def EDS(i):
            """ recursion with memoization """
            if i in memo:
                return memo[i]
            
            tail = nums[i]
            maxSubset = []
            # Check which previous subset can be extended with nums[i]
            for p in range(0, i):
                if tail % nums[p] == 0:
                    subset = EDS(p)
                    if len(maxSubset) < len(subset):
                        maxSubset = subset
            
            # extend the found max subset with the current tail.
            maxSubset = maxSubset.copy()
            maxSubset.append(tail)
            
            memo[i] = maxSubset
            return maxSubset
        
        # test case with empty set
        if len(nums) == 0: 
            return []
        
        # sort is important because of transitivity of division
        # if a | b and b | c then a | c
        nums.sort()

        # memoize largest subset that ends on nums[i]
        memo = {}
    
        # Find the largest divisible subset
        return max([EDS(i) for i in range(len(nums))], key=len)
```

## Bitmask DP 
- Space optimization for subset
### Minimum Vertex Cover
https://leetcode.com/problems/smallest-sufficient-team/description
- Optimization: Remove all inputs that are subsets of another
# Related
## [[LC-174. Dungeon Game]]

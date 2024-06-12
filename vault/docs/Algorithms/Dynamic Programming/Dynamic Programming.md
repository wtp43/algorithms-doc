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


## 0/1 Knapsack

### Maximum Number of Achievable Transfer Requests
https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/description/
- Note: Tuples are hashable in python, lists are not
```python
def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i, a):
            if i == len(requests):
                return 0 if not any(a) else -math.inf
            arr = list(a)
            arr[requests[i][0]] -= 1
            arr[requests[i][1]] += 1
            x = dfs(i+1, tuple(arr))
            y = dfs(i+1, a)
            return max(1+x,y)
        return dfs(0, tuple([0]*n))
```

### Number of Ways to Achieve At Least K
https://leetcode.com/problems/profitable-schemes/
 - Optimization (reduce states): use `min(minProfit, p + profit[i])` instead of `p + profit[i]` to reduce states
	 - suppose the current profit is greater than minProfit
	 - then the number of ways is the same for `dfs(i, mem, p)` and `dfs(i, mem, p+1)`
	 - By reducing the states, we can use more memoized results

```python
def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, mem, p):
            if i >= len(group):
                return 1 if p >= minProfit else 0
            tot = dfs(i+1, mem, p)%(10**9+7)
            if group[i] <= mem:
                tot += dfs(i+1, mem-group[i], min(minProfit, p+profit[i]))
            return  tot %(10**9+7)
        
        return dfs(0,n, 0)
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

### Maximum Total Reward 
> Take any untaken reward as long as it is less than your current reward. You start with reward = 0
https://leetcode.com/problems/maximum-total-reward-using-operations-ii/
- Use bit mask to indicate which number is taken
- binary 1001 means 3 and 1 are taken

```python
def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(set(rewardValues))
        # at the beginning, the x is 0, we set the first bit of binary to indicate x is 0.
        x = 1
        for num in rewardValues:
            # for each reward, only the x < reward can be used
            # so we only keep the x < reward as validX
            validX = x & ((1 << num) - 1)

            # for each value in validX, we add num to it
            # for example, if we have x = 5 (binary 100000) and num = 6
            # then we will have new x = 11, whose binary = 10000000000
            # == (100000) << 6
            x |= validX << num 
        
        # return the largest x as the result
        return rewardValues[-1] + x.bit_length() - 1

```

### Distinct Subsequences
- Store number of words that end with the current letter
-  recurrence relation: `f(s) = f(s[:n-1])*2+1 - freq[s[n-1]]`
```python
def distinctSubseqII(self, s: str) -> int:
        # recurrence relation: f(s) = f(s[:n-1])-freq[s[n-1]] * 2+ 1
        # store number of words that end with current letter
        res = 0
        freq = defaultdict(int)
        for c in s:
            # we can make res amount of sequences by appending c to all of them
            # then account for the subsequence 'c'
            tmp = freq[c]
            freq[c] = res+1
            # minus all previous subsequences ending with c to prevent double counting
            res = (res*2+1 - tmp)% (10**9+7)
        return res 
```



## General DP

### Largest Sum of Averages for at Most K Partitions
https://leetcode.com/problems/largest-sum-of-averages/description/
- Mediant property of fractions means we want to partition as much as possible since average <= sum 
- Try every index except 0 as a partition
```python
def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        dp = {}

        def dfs(n, k):
            if (n, k) in dp:
                return dp[n, k]
            if n < k:
                return 0
            if k == 1:
                dp[n, k] = sum(nums[:n])/n
                return dp[n,k]

            cur = dp[n, k] = 0
            # try partitioning at at all indices except for 0
            for i in range(n - 1, 0, -1):
                cur += nums[i]
                dp[n, k] = max(dp[n, k], dfs(i, k - 1) + cur /(n - i))
            return dp[n, k]
        return dfs(len(nums), k)

```
### Restore The Array
https://leetcode.com/problems/restore-the-array/description/?envType=study-plan-v2&envId=dynamic-programming-grandmaster
- Return the number of possible partitions of s such that each partition of s is less than k
```python
def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        m = len(str(k))
        for i in range(n):
            j = i
            x = j-10
            for j in range(max(0, i-m+1), i+1):
                if s[j] != '0' and int(s[j:i+1])<=k:
                    dp[i+1] = (dp[i+1] + dp[j]) % (10**9+7)
        return dp[n]
```

### Handshakes That Don't Cross
https://leetcode.com/problems/handshakes-that-dont-cross/
- 2n people stand in a circle
- How many ways can n handshakes occur such that none cross
	- The current person can only shake hands with someone if there is an even amount of people between them
- Choose two people to be the split between the left and right side
```python
def numberOfWays(self, numPeople: int) -> int:
        n = numPeople//2
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            for j in range(i):
                # choose 2 people to be pivot 
                # there are 2i-2 people to choose for the left
                # there are then 2i-2j-2 to choose for the right 
                dp[i] += dp[j] * dp[i-j-1]
                dp[i] %= 10**9+7
        return dp[n]

```
## [[LC-174. Dungeon Game]]

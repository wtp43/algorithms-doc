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

## Efficient Iteration (Reducing Search Space and States)
> Choosing the right input to iterate over can significantly reduce the search space.
### [Number of Ways to Wear Different Hats to Each Other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/)
>Given a list of preferred hats per person, count the number of ways each person is wearing a different preferred hat. 
- There are 40 types of hats and at most 10 people.
- Iterate over all 40 hats instead of `10*40` hats for every person
	- O($k \cdot n \cdot 2 ^n$) vs O($k \cdot n\cdot 2^{k}$)
```python
def numberWays(self, hats: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(hat, mask):
            if mask == complete:
                return 1
            if hat > 40:
                return 0
            ans = dp(hat+1, mask)
            for person in hats_to_people[hat]:
                if mask & (1<<person) == 0:
                    ans = (ans + dp(hat+1, mask|(1<<person)))%mod
            return ans%mod

        n = len(hats)
        mod = 10**9+7
        complete = 2**n-1

        hats_to_people = defaultdict(list)
        for i in range(len(hats)):
            for hat in hats[i]:
                hats_to_people[hat].append(i)
        return dp(0, 0)
```
- Time complexity O($k \cdot n \cdot 2 ^n$): There are $k$ states for hat and $2^n$ states for mask. At each state, you have to iterate over all possible people for that hat for a max cost of 0($n$)
- Space Complexity  O($k \cdot 2 ^n$): The total number of states

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

## Optimization (State Reduction)
- Notice when it's not needed to generate all combinations
	- Generation of all combinations is generally needed if it is required to count all the possible partitions
### Examples
#### Omit all combinations when unneeded
- Finding the max of all combinations (generation of all combinations is thus not needed)
	- We want to find the largest x such that `x = sum(set1) + sum(set2)` Instead of storing all combinations `(sum1, sum2)`, we can instead store the `diff = sum1 - sum2`
	- States are reduced from Exponential -> Polynomial
#### Traversing duplicate states
- For DP, not backtracking, we generally only need to traverse on the suffix/prefix 
## Subsequences
#### Longest Increasing Subsequence (LIS)

- DP: 0($n^2$)
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

#### [Length of the Longest Subsequence That Sums to Target](https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/)
- Similar to coin change problem
- Base case: sum 0 has subsequence length 0
- Iterate over nums, update dp for num to target
- **We iterate in reverse while updating the longest subsequence to avoid using the same num twice. This works because the recurrence relation: smaller sequences do not depend on larger sequences**
	- This is important because we are using 1-D dp, we don't need to iterate in reverse if we store the results in `dp[i][j] = max(dp[i][j], dp[i-1][j-num]+1)` where $i$ represents the results using only the first $i$ nums 
	- Example of when iterating in ascending order would fail for 1-D dp
		- nums = `[4, 2]`, target = 4
		- first loop, dp = `[0,0,0,0,1]`
		- second loop, dp = `[0,0,1,0,2]`,  `dp[2]` is updated first to be 1, then `dp[4]` is updated using `dp[2]`
		- Iterating in reverse would prevent overwriting the results of the previous loop

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
# The difference with coin change is that coins are not unique and order does not matter
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

###  Number of Beautiful Partitions
https://leetcode.com/problems/number-of-beautiful-partitions/description/
- Count the number of valid (k partition combinations) of s
```python
def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
	m = 10**9+7
	primes = '2357'
	if k > len(s):
		return 0
	if s[-1] in primes or s[0] not in primes:
		return 0
	@lru_cache(None)
	def dfs(i,k):
		if k == 0 and i <= len(s):
			return 1
		if i >= len(s):
			return 0
		
		cnt = dfs(i+1, k)
		if s[i] in primes and s[i-1] not in primes:
			cnt = (cnt + dfs(i+minLength, k-1))%m
		return cnt%m
		
	return dfs(minLength, k-1)
```
- Time complexity: O($n\cdot k$)
	- For every index i of s, we check with partitions made, 0..k
- Notice that it isn't needed to traverse an extra (n steps) for the current state
```python
for j in range(i+minLength-1, len(s)):
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

## Meet in the Middle 
- Divide search space into two halves (not recursive)
- Use hash maps to store differences of all combinations
### Maximum Sum of 2 Equal Sum Subsets
https://leetcode.com/problems/tallest-billboard/description
- Brute force: Keep the states -> i = current element to consider, x = sum of set 1, y = sum of set 2
	- where initially, x = 0 and y = sum(nums) 
	- transitions: don't take (remove from y), add to x, keep it in y
	- Time complexity O($3^n$)
- Brute force optimization (reducing states to utilize memoization): Instead of keeping state of set1 and set2, use the diff instead
```python
def tallestBillboard(self, rods: List[int]) -> int:
	@lru_cache(None)
	def dfs(i, diff):
		if i >= len(rods):
			return 0 if diff == 0 else -math.inf
		return max(dfs(i+1, diff), rods[i] + dfs(i+1, diff + rods[i]), rods[i]+ dfs(i+1, diff-rods[i]))
	return dfs(0, 0)//2
```
#### Reduction to O($3^n$) to  2$\cdot$O($3^\frac{n}{2}$) with Divide and Conquer$^*$
- Split array into 2 halves 
- Generate all combinations of the two sets for each half separately (non recursive)
- Transitions: don't take, take for x, take for y
- State: Use `diff = left - right` as keys to store the sum of either the left or right subset (used to rebuild the max sum)
- Merge step: Find `max(left_half[diff] + right_half[-diff])` for all diff

```python
def tallestBillboard(self, rods: List[int]) -> int:
	def combinations(nums):
		states = set([(0,0)])
		for x in nums:
			new_states = set()
			for l,r in states:
				new_states.add((l+x, r))
				new_states.add((l, r+x))
			states |= new_states

		dp = defaultdict(int)
		for l,r in states:
			dp[l-r] = max(dp[l-r], l)
		return dp
	res = 0
	n = len(rods)
	a = combinations(rods[:n//2])
	b = combinations(rods[n//2:])
	for diff in a:  
		if -diff in b:
			res = max(res, a[diff] + b[-diff])
	return res
```

#### Reduce to 0($n^2$), Combinations to DP
>[!tip] State Reduction
> Notice that since we are looking for the max sum and not the count of all partitions, we don't need to generate/keep track of all combinations

- Save the higher sum the two subsets in a dictionary with `diff` as the keys
- If we were to skip (not use for either support) the new rod, then `dp` would not change. That's why we are initializing `new_dp` by copying `dp`. It implicitly considers this option.

```python
def tallestBillboard(self, rods: List[int]) -> int:
	dp = defaultdict(int)
	dp[0] = 0

	for x in rods:
		# need a copy so we don't overwrite what
		# we are iterating
		new_dp = dp.copy()
		for diff, taller in dp.items():
			shorter = taller-diff
			
			# add x to taller
			new_dp[diff+x]= max(new_dp[diff+x], taller+x)   

			# add x to shorter
			new_diff = abs(shorter+x-taller)
			new_taller = max(shorter+x, taller)
			new_dp[new_diff] = max(new_dp[new_diff], new_taller)
		dp = new_dp
	return dp[0]
```
## Time Complexity
### Memoization
https://stackoverflow.com/questions/21273505/memoization-algorithm-time-complexity
- Can reduce complexity to polynomial time
- Ex: Word Break Problem 
	- Use of **memoization** reduces worst case time complexity to O($n^2$) since `SegmentString` is only called on suffixes of the original input string, and that there are only O(n) suffixes

## [[LC-174. Dungeon Game]]

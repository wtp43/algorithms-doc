---
title:  "Backtracking"
created: 2023-01-05
---




# Backtracking

# Implementation

```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
```

## Optimizations
- Suppose we want to check the validity of an array
	- Sort 


>[!Time Complexity]+

>[!Space Complexity]+

## Applications

### Item Matching/Distribution
https://leetcode.com/problems/distribute-repeating-integers/
```python
def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
    # why does greedy not work here
    count = Counter(nums)
    n = len(quantity)
    # we only need the len(quantity) greatest numbers
    available= sorted(count.values())[-n:]
        
    # Optimization: Start with largest quantity
    quantity.sort(reverse=True)
    # This cannot be cached since answers at i are not unique
    def dfs(i):
        if i == n:
            return True
        for j in range(len(available)):
            if available[j] >= quantity[i]:
                available[j] -= quantity[i]
                if dfs(i+1):
                    return True
                available[j] += quantity[i]
        return False
    return dfs(0)
```

### Testing All Pairs
https://leetcode.com/problems/maximize-score-after-n-operations/description/
#### Optimizations
- Keep map for costly computations:
	- GCD map. 
	- To build a map with tuples as the key, access them as (mn, mx) where mn = min(x,y) and mx = max(x,y)
- Memoize/cache completed calculations:
	- Either keep a memo map or append lru_cache decorator to function
	- Make sure to not include unique counters (such as score) into the function parameters

```python
def maxScore(self, nums: List[int]) -> int:
        n = len(nums)//2
        nums.sort()
        gcd_map = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                gcd_map[(nums[i], nums[j])] = gcd(nums[i], nums[j])
        @lru_cache(None)
        def dfs(k, mask):
            if k == n+1:
                return 0
            maxScore = 0
            for i in range(len(nums)):
                if mask & 1<<i:
                    continue
                for j in range(i+1, len(nums)):
                    if mask & 1<<j:
                        continue
                    cur_score = k*gcd_map[(nums[i], nums[j])]
                    new_mask = mask | 1 << i | 1 << j
                    remaining_score = dfs(k+1, new_mask)
                    maxScore = max(maxScore, cur_score + remaining_score)
    
            return maxScore
        return dfs(1,0)
```

**Time Complexity:** O($2^{2n}*(2n)^2+2n*log(A)$) since we cache the result of dfs(k,mask), we are only processing each unique mask once.
There are $2^{2n}$ masks, at most $(2n)^2$ pairs for each mask, $log(A)$ to calculate the GCD of the maximum two numbers.


### Including or not including

- No for loop needed in each backtrack because there is only two options
  - Take i or don't take i compared to take or don't take for each of remaining numbers

#### Power Set

```python
def subsets(self, nums: List[int]) -> List[List[int]]:
	res = []
	n = len(nums)
	subset = []
	def backtrack(i):
		if i == n:
			res.append(subset.copy())
			return
		subset.append(nums[i])
		backtrack(i+1)
		subset.pop()
		backtrack(i+1)
	backtrack(0)
	return res
```

### Picking the element for the current position

#### Permutations

- Swap first num with all nums after it and backtrack (equivalent to choosing a num for every single position)

```python
def permute(self, nums: List[int]) -> List[List[int]]:ķ        res = []
	n = len(nums)
	def backtrack(i):
		if i == n-1:
			res.append(nums.copy())
			return
		for j in range(i, n):
			nums[i], nums[j] = nums[j], nums[i]
			backtrack(i+1)
			nums[i], nums[j] = nums[j], nums[i]
	backtrack(0)
	return res
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
	res = []
	n = len(nums)
	def backtrack(i):
		if i == n-1:
			res.append(nums.copy())
			return
		starting_num = set()
		for j in range(i, n):
			if nums[j] in starting_num:
				continue
			nums[i], nums[j] = nums[j], nums[i]
			backtrack(i+1)
			nums[i], nums[j] = nums[j], nums[i]
			starting_num.add(nums[j])

	backtrack(0)
	return res
```

**Time Complexity:** O($2^n * n)$ since there are $2^n$ orderings and it takes O(n) to make a copy of that order.
#### Combinations

- build combination by picking a number from (i,n)
- keep track of how many numbers are needed (only backtrack if available numbers is enough for remaining numbers needed)

```python
# Get all combinations of size k for elements in 1..n
def combine(self, n: int, k: int) -> List[List[int]]:
	combination, res = [], []

	def backtrack(i, need):
		if need==0:
			res.append(combination.copy())
			return

		remain = n - i + 1
		available = remain-need

		for j in range(i, i + available + 1):
			combination.append(j)
			backtrack(i, combination)
			combination.pop()
	return res
```

#### n-queens

- Sets: col, row, neg diag, pos diag

```python
 def solveNQueens(self, n: int) -> List[List[str]]:
	res = []
	col = set()
	posDiag = set()  # (r + c)
	negDiag = set()  # (r - c)
	board = [['.']*n for i in range(n)]

	def backtrack(r):
		if r == n:
			copy = ["".join(row) for row in board]
			res.append(copy)
			return
		for c in range(n):
			if c in col or (r + c) in posDiag or (r - c) in negDiag:
					continue
			col.add(c)
			posDiag.add(r + c)
			negDiag.add(r - c)
			board[r][c] = "Q"

			backtrack(r + 1)

			col.remove(c)
			posDiag.remove(r + c)
			negDiag.remove(r - c)
			board[r][c] = "."


	backtrack(0)
	return res
```

### Paths

- Manhattan Distance: abs distance between start and destination

```python
def uniquePathsIII(self, grid: List[List[int]]) -> int:
	m,n = len(grid), len(grid[0])
	squares = 0
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				start = (i,j)
			elif grid[i][j] == 2:
				end = (i,j)
			if grid[i][j] != -1:
				squares += 1
	visited = set([start])
	squares-= 2
	paths = 0
	def backtrack(pos, squares):
		nonlocal paths
		i,j = pos
		if pos == end:
			paths += 1
			return
		for x,y in [[0,1], [0,-1], [1,0], [-1,0]]:
			new_x = j+x
			new_y = i+y
			new_pos = (new_y, new_x)
			if new_pos in visited or new_x < 0 or new_x >= n or new_y < 0 or new_y >= m or grid[new_y][new_x] == -1:
				continue
			if new_pos == end and squares > 0:
				continue
			manhattan_distance = abs(end[0] - new_pos[0]) + abs(end[1] - new_pos[1])
			if squares < manhattan_distance - 1:
				continue
			visited.add(new_pos)
			backtrack(new_pos, squares-1)
			visited.remove(new_pos)
	backtrack(start, squares)
	return paths
```


# Spiral Backtracking



# Related

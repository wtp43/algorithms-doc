---
---
# Depth First Search
- 

## Time Complexity
- O(E + V)

## Space Complexity
- Space complexity O(depth) nodes compared to O(|V|) = O(n) for BFS

```python
seen = set()

def dfs(graph: Dict[int, List[int]], cur: int):
    if cur in seen: return
    seen.add(cur)
    for next in graph[cur]:
        dfs(graph, next)
```
- Alternatively, graph and seen can be set as global variables. 
- 'seen' does not need to be marked as `global` inside `dfs` to modify it because we are not reassigning its value using 
# Brute Force
We can traverse in a DFS fashion by linearly searching for the child nodes.
This will take O(n) to search for each child and in the worst case, the depth is n, time complexity will be O($n^n$).

# Use Cases

[Strongly Connected Components](</docs/Algorithms/Graphs/Strongly Connected Components.md>)- Start DFS at every node (except if it's already been visited) and mark all reachable nodes as being part of the same component
[LC-200. Number of Islands](</docs/Some Leetcode Questions/LC-200. Number of Islands.md>)
## DFS Traversals

### Pre-order Traversal

### In-order Traversal

### Post-order Traversal





## Backtracking
- Extension of DFS
- General process: at the current node, update some state, continue DFS, once returned, revert state, continue DFS 
###  0-1 Knapsack (Include or Exclude)
- No for loop needed in each backtrack because there is only two options
- Take `a[i]` or don't take `a[i]` and DFS for all i
- Time Complexity: O$(n2^n)$
	- There are two choices to take at each step
	- It takes n steps to visit each node i



### Permutations

:::note[note] 

Recursively fix the $i^{th}$ element. Available choices are `a[i...n]`. Swap the chosen element with the $i^{th}$ element and continue until the last position.


:::

- Slight modification needed if there are duplicate elements, we do not pick the current element if it has been picked already

```python
def permute(self, nums: List[int]) -> List[List[int]]:        
	res = []
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

### Combinations

- build combination by picking a number from `a[i...n]`
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

### N-Queens

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

### Matrix Traversal
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
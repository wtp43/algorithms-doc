---
---
# Hashing
- [ ] https://leetcode.com/problems/strings-differ-by-one-character/solutions/801825/python-clean-set-string-hashing-solution-from-o-nm-2-to-o-nm/?orderBy=most_votes
- [ ] Distinct islands
- [ ]  https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1126/



## [694. Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/)
- Hash islands by DFS path
- Append a ('0') at the end of each recursion to distinguish between ![3 islands that hash to the same path, using the scheme described above.](https://leetcode.com/problems/number-of-distinct-islands/Figures/694/image_6.png)

```python
def numDistinctIslands(self, grid: List[List[int]]) -> int:
	def dfs(row, col, direction):
		if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
			return
		if (row, col) in seen or not grid[row][col]:
			return
		seen.add((row, col))
		path_signature.append(direction)
		dfs(row + 1, col, "D")
		dfs(row - 1, col, "U")
		dfs(row, col + 1, "R")
		dfs(row, col - 1, "L")
		path_signature.append("0")
	
	seen = set()
	unique_islands = set()
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			path_signature = []
			dfs(row, col, "0")
			if path_signature:
				unique_islands.add(tuple(path_signature))
	
	return len(unique_islands)
```
---
---

## Direction Vectors
- Makes accessing neighbouring cells very easy

```python
dr = [-1, +1,  0,  0]
dc = [ 0,  0, +1, -1]

for i in range(len(dr)):
	rr = r + dr[i]
	cc = c + dc[i]

	#skip invalid cells
	if rr < 0 or cc < 0: continue
	if rr >= R or cc >= C: continue

```


[BFS](</docs/Algorithms/Graphs/BFS.md>)
```python

dirs = [[0,1], [0,-1], [1,0], [-1,0]]

def bfs(grid: List[List[int]], x: int, y: int):
	q = deque((x, y))
	seen = set([(x, y)])
	n_dir = len(dr)
	r = len(grid)
	c = len(grid[0])
	while q:
		cur = q.popleft()
		if cur in seen:
			continue
		for x, y in dirs:
			i = cur[0] + x
			j = cur[1] + y
			if (i,j) in seen or i < 0 or j < 0 or i >= r or j >= c:
				continue
		 	seen.add((i,j))
		 	q.append((i,j))
	

```


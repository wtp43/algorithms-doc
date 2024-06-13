---
---
# BFS

## BFS
> BFS can guarantee shortest path while DFS does not
```python
def bfs(graph: Dict[int, List[int]], start: int):
	
    q = deque([start])
    seen = [0]*n
    seen[start] = 1
	prev = [-1]*n
	
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if next in seen: 
                continue
            q.append(next)
            seen[next] = 1
            prev[next] = cur
    return prev

def reconstruct_path(start, end, prev):
	path = []
	while end != -1:
		path.append(end)
		end = prev[end]
		if end == start:
			break
	path.reverse()

	# if traversing backwards starting from end gives 
	# us the starting node, there exists a path
	if path[0] == s:
		return path
	return []
```
- the prev array allows us to reconstruct the shortest path
### Time/Space Complexity
- O($b^d$) where $b$ is the branching factor, $d$ is the depth of the tree which is equivalent to O(E + V)
- Space Complexity of DFS is only O(depth) while BFS is O(n) = O(|v|)

## Multisource BFS
Append all sources to a q and iterate the q in chunks/layers.

[LC-286. Walls and Gates](</docs/Some Leetcode Questions/LC-286. Walls and Gates.md>)[LC-994. Rotting Oranges](</docs/Some Leetcode Questions/LC-994. Rotting Oranges.md>)


## Shortest Path Problems

### Minimum Operations to Convert Number
https://leetcode.com/problems/minimum-operations-to-convert-number/description/
- Put possible subsequent states into a queue

```python
def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
	q = deque([start])
    seen = set()
    res = 0
    while q:
        for _ in range(len(q)):
            x = q.popleft()
            if x == goal:
                return res
            if x < 0 or x > 1000 or x in seen:
                continue
            seen.add(x)
            for y in nums:
                q.append(x+y)
                q.append(x-y)
                q.append(x^y)
        res += 1
    return -1
```

# Related Problems

## [[Matrix Traversals|Using BFS to find the shortest path on a grid]]



## BFS Traversals

### Level-order Traversal


---
---
# BFS

## BFS
- Space Complexity of DFS is only O(depth) while BFS is O(n) = O(|v|)
- BFS can guarantee shortest path while DFS does not

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
## Time Complexity
O($b^d$) where $b$ is the branching factor, $d$ is the depth of the tree which is equivalent to O(E + V)

## Space Complexity

# BFS Implementation

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

# Multisource BFS
Append all sources to a q and iterate the q in chunks/layers.

[[LC-286. Walls and Gates]]
[[LC-994. Rotting Oranges]]


# Related Problems

## [[Matrix Traversals|Using BFS to find the shortest path on a grid]]



## BFS Traversals

### Level-order Traversal


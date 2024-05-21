---
---

## A note on State Representation
- Instead of storing positions as (x,y) pairs which require an array/object wrapper to store the coordinate values, one can directly enqueue coordinates in one queue. This avoids the overhead of packing and unpacking the coordinates
- Keeping everything in one queue will preserve memory locality (sequential accesses in the same area of memory, likely in the same cache read), while having to access 3 different queues every iteration will likely be a performance hit as they cause cache misses (which, even if they're contiguous, would be inevitable above a certain number of vertices), and quite possibly be worse than packing/unpacking a structure depending on how the compiler optimizes that as an alternative, if you want your queues to just be primitives without any packing, just push x,y,z sequentially onto the same queue, and dequeue them 3 at a time as well. it's not any more complex than managing 3 queues at once, avoids packing, and most importantly doesn't require both allocating and accessing multiple data structures.
## Pros vs DFS
- Able to find shortest path in an undirected graph

## Time Complexity
O($b^d$) where $b$ is the branching factor, $d$ is the depth of the tree
equivalent to
O(E + V)

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


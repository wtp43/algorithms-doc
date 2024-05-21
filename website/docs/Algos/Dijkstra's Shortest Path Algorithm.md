---
---
- Looks only to the immediate neighbors of a vertex (while Bellman Ford goes through each edge in every iteration)
- Dijkstra's algorithm is a [[Shortest and Longest Path on DAG#Single Source Shortest Path (1 root)|SSSP]] algorithm for graphs with **non-negative edge weights**. However, in the real word, many applications can be modelled as graphs with non-negative weights
- This constraint is imposed to ensure that once a node has been visited, its optimal distance cannot be improved
[Topological Sort](</docs/Algos/Topological Sort.md>)
>[!Intuition]
>Greedy algorithms work because once the next 'node' has been visited, it's optimal distance cannot be improved

# Overview
1. Initialize `dist` array to `math.inf` with `dist[start]=0` 
2. Maintain priority queue (PQ) of key-value pairs `(node index, distance)`
3. Insert `(start,0)` into PQ and loop while PQ is not empty
4. Iterate over all edges outwards from current node and relax each edge appending the neighbouring node if it was relaxed,


# Implementation

**Complexity:** O(E log V)
- Iterate over all edges  = E
- Building a priority queue of all vertices = log V
# Lazy Dijkstra

- Contains duplicated key-value pairs in the PQ

```python
import heapq

def lazy_dijkstra(self, start):
	n = len(self.get_vertices())
	dist = [math.inf] * n
	prev = [None] * n
	dist[start] = 0
	seen = [0] * n
	pq = [(start, 0)]
	heapq.heapify(pq)
	while pq:
		min_value, index = heapq.heappop(pq)
		if dist[index] < min_value:
			continue
		seen.add(index)
		for u,v,w in self.get_edges(index):
			if seen[v]: 
				continue
			new_dist = dist[index] + w
			if new_dist < dist[v]:
				dist[v] = new_dist
				prev[v] = u
				heapq.heappush(pq, (new_dist, v))
	return dist, prev
```

- Optimization: `if dist[index] < min_value: continue`
	- We do not need to check all out-edges from this key-value pair because a previous edge took us to this node faster
- It is possible to have duplicate node indices in the PQ. This is not ideal but inserting a new key-value pair is O(logn) which is faster than searching for the key in the PQ which takes O(n)
	- Ex: (0, 0) ->  (2,5), (1,10) -> (1,1), (1,10)
		- Start at 0. Append neighbors 1 and 2 with their respective weights
		- Continue at node 2 which has the smallest weight 5.
		- Append 2's neighbors which is 1 with weight 1
		- Thus, the PQ contains node 1 twice

# Finding the Optimal Path 
- Keep finding the parent of end and reverse the list 
- If the last parent is equal to start, there exists a path
```python
def find_shortest_path(self, start, end):
	dist, prev = self.dijkstra(start, end)
	path = []
	while end:
		path.append(end)
		end = prev[end]
	if path[-1] != start:
		return None
	path.reverse()
	return path
```

# Stopping Early

> [!question]+ 
> **Suppose you know the destination node you're trying to reach is 'e' and you start at node 's', do you still have to visit every node in the graph?**
> 
> Yes, in the worst case. However, it is possible to stop early once you have finished visiting the destination node. The main idea for stopping early is that Dijkstra's algorithm processes each next most promising node in order. So if the destination node has been visited, its shortest distance will not change as more future nodes are visited.

```python
import heapq

def lazy_dijkstra(self, start, end):
	n = len(self.get_vertices())
	dist = [math.inf] * n
	prev = [None] * n
	dist[start] = 0
	seen = [0] * n
	pq = [(0, start)]
	heapq.heapify(pq)
	while pq:
		min_value, index = heapq.heappop(pq)
		if dist[index] < min_value:
			continue
		seen.add(index)
		for u,v,w in self.get_edges(index):
			if vis[v]: continue
			new_dist = dist[index] + w
			if new_dist < dist[v]:
				dist[v] = new_dist
				prev[v] = u
				heapq.heappush(pq, (new_dist, v))

	# stop early
	if index == end:
		return dist[end]
	return math.inf
```
# Eager Dijkstra's Algorithm using Indexed Priority Queue

[Indexed Priority Queue (IPQ)](</docs/DS/Indexed Priority Queue (IPQ).md>)	> Allows us to avoid duplicated duplicate key-value pairs. Supports efficient value updates in O(logn)

```python
def dijkstra(self, start):
	n = len(self.get_vertices())
	dist = [math.inf] * n
	prev = [None] * n
	vis = [0] * n
	dist[0] = 0
	ipq = IPQ()
	ipq.insert((s, 0))

	while ipq.size():
		index, min_val = ipq.poll()
		vis[index] = 1
		if dist[index] < min_val: continue
		for u,v,w in self.get_edges(index):
			if v[index]: 
				continue
			new_dist = dist[index] + min_val
			if ipq.contains(v):
				ipq.decrease_key(v, new_dist)
			else:
				ipq.insert(v, new_dist)
	return dist
	

```


[D-ary Heap](</docs/DS/D-ary Heap.md>)When executing Dijkstra's algorithm, especially on dense graphs, there are a lot more updates (decrease_key operations) to key-value pairs than there are dequeue (poll) operations.

A D-ary heap speeds up decrease key operations at the expense of more costly removals. 

> [!danger]+ Intuition
> More children means a flatter tree with smaller depth.
> This means it requires less work to swim but more work to sink since you have to check the parent node against D children.


## Optimal D-ary Heap degree


> [!question]+ Question
> **What is the optimal D-ary heap degree to maximize performance of Dijkstra's algorithm?**
> 
> A: In general $D = E/V$ is the best degree to use balance removals against decrease\_key operations improving Dijkstra's time complexity to $O(E \log_{E/V}(V))$ which is much better especially for dense graphs which have lots of decrease_key operations


[Fibonacci Heap](</docs/DS/Fibonacci Heap.md>)Fibonacci heap gives Dijkstra's algorithm a time complexity of $O(E + Vlog(V))$. However, in practice, Fibonacci heaps are very difficult to implement and have a large enough constant amortized overhead to make them impractical unless your graph is quite large.
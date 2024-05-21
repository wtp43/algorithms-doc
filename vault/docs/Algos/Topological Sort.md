---
title: Topological Sort
created: 2022-12-10
---

>[!summary]+ Contents
>```toc 
style: number 
min_depth: 1 
max_depth: 6


# Topological Sort Using DFS
Produces a list of all vertices in an order such that no vertex appears before another vertex that has an edge to it.

Topological sort simply involves **running DFS on an entire graph and adding each node to the global ordering of nodes, but only after all of a node's children are visited**. This ensures that parent nodes will be ordered before their child nodes, and honours the forward direction of edges in the ordering. The ordering is not unique.

- Orders the vertices on a line such that all directed edges go from left to right
- Such an ordering cannot exist if the graph contains a directed cycle
- Each [[Graph Theory#Directed Acyclic Graphs (DAG)|DAG]] has at least one topological sort, they are not unique

> [!example]+ 
> ![[Pasted image 20230106154005.png]]
> ![[Pasted image 20230106154013.png]]





>[!Purpose]
>Gives an ordering where each vertex can be processed before it's successors. This allows us to seek the shortest/longest path from x to y in a DAG

# DFS Implementation

```python
def topsort(self,graph):
	seen = set([])
	ordering = deque()
	for node in graph.get_vertices():
		self.dfs_topsort(node, seen, ordering)
	return ordering

def dfs_topsort(self, graph, node, seen, ordering):
	if node in seen:
		return 
	seen.add(node)
	for neighbor in graph.get_neighbors(node):
		self.dfs_topsort(neighbor, seen, ordering)
	ordering.appendleft(node)
```

## Modified to detect cycles

```python
def topsort(self,graph):
	vis = defaultdict(lambda: 0)
	ordering = deque()
	for node in graph.get_vertices():
		self.dfs_topsort(graph, node, vis, ordering)
	return ordering

def dfs_topsort(self, graph, node, vis, ordering):
	if vis[node] == 2:
		return 
	if vis[node] == 1:
		raise CycleError
	vis[node] = 1
	for nbor in graph.get_neighbors(node):
		self.dfs_topsort(graph, nbor, vis, ordering)
	ordering.appendleft(node)
	vis[node] = 2
```

## Optimized Complexity

>[!Time Complexity]
>O(V + E)

>[!Space Complexity]
>O(d)

# Kahn's Topological Sort Algorithm
Find vertices with no incoming edges and removing all outgoing edges from these vertices.

Maintain in-degree information of all graph vertices.
Removing an edge from u to v will decrement ``indegree[u]`` by 1.

If a cycle exists, then not all vertices will be able to achieve an indegree of 0. If the top_order does not have a length of n, then we must have encountered a cycle.

```python
def topsort(edges, n):
	top_order = deque()
	indegree = [0] * n
	adj_list = [[] for _ in range(n)]
	for u,v in edges:
		adj_list[u].append(v)
		indegree[v] += 1

	# Store all the nodes with no incoming edges
	q = deque([i for i in range(n) if indegree[i] == 0])
	while q:
		# extract front of queue
		u = q.popleft()
		# add the current vertex to the tail of the ordering
		top_order.append(u)
		for v in adj_list[u]:
			indegree[v] -= 1
			if indegree[v] == 0:
				q.append(v)
				
	if len(top_order) != n:
		print('Cycle Exists')
	return top_order

```
# Applications
## Scheduling Problems
[[LC-207. Course Schedule]]
[[LC-210. Course Schedule II]]



# Related
- [[Cycle Detection in Directed Graphs]]

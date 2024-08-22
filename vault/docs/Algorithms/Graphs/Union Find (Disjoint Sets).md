---
---
# Union Find
- Stores an array indicating which elements in the array are connected to each other
- Can be augmented to store additional information about each component (size, sum, etc.)

>[!note]
>Union Find stores the index of each element's parent in an array.
## Union Find Optimizations

### Weighted Union (by Size or Rank): 
- Keep track of size to keep balanced trees. Root of subtree with lesser number of nodes points towards the root of subtree with larger amount of nodes which leads to reduction of tree's height
	- These will not necessarily result in binary trees
	- This limits the total depth of the tree to O(logn) because the depth of nodes only in the smaller tree will now increase by one and the depth of the deepest node in the combined tree can only be at most one deeper than the deepest node before the trees were combined. The total number of nodes in the combined tree is therefore at least twice the number in the smaller subtree. Thus the depth of any node can be increased at most logn times where n equivalences are processed (since each addition to the depth must be accompanied by at least doubling the size of the tree).
	- https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/UnionFind.html
### Path Compression
- Shorten path to parent


## Python Implementation
- We can either union by rank/height or size

```python
class Union_find:
	def __init__(self,n):
		self.n = n
		self.parent = list(range(n))
		self.rank = [1]*n

	#Path compression used to shorten path to parent O(loglogn)
	def find(self,x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	# Union modifies the parent array
	def union(self, x, y):
		px = self.find(x)
		py = self.find(y)

		if px == py:
			return
		# bigger parent stays the parent
		if self.rank[px] == self.rank[py]:gg
			self.parent[px] = py
			self.rank[py] += 1
		elif self.rank[px] < self.rank[py]:
			self.parent[px] = py
		else:
			self.rank[py] = self.rank[px]
```

## Applications

### Connected Components
- Union all edges (u, v)
- Alternatively, Start DFS at the next unvisited node
  - Increment components by one, update visited nodes


### Find Longest Consecutive Sequence in a set
  - Keep track of seen numbers in hash map
  - Union current current component to existing components

```python
def longest_consecutive_sequence(nums):
	d = {}
	uf = union_find(len(nums))
	for i, num in enumerate(nums):
		if num in d:
			continue
		d[num] = i
		if num-1 in d:
			uf.union(i, d[num-1])
		if num+1 in d:
			uf.union(i, d[num+1])
	return max(uf.size) if nums else 0
```

### Cycle Detection for Undirected Graphs

- UF does not work for directed graphs
- Create UF for number of vertices
- Iterate through all edges and if two vertices have the same parent, there must be a cycle

```python
def isCyclic(edges,num_vertices):
    uf = union_find(num_vertices)
    for x,y in edges:
        if uf.find(x) == uf.find(y):
            return True
        uf.union(x,y)
	return False

```

We cannot use union-find to detect cycles in a directed graph. This is because a directed graph cannot be represented using the disjoint-set(the data structure on which union-find is performed).

When we say 'a union b' we cannot make out the direction of edge

1. is a going to b? (or)
2. is b going to a?

But, incase of undirected graphs, each connected component is equivalent to a set. So union-find can be used to detect a cycle. Whenever you try to perform union on two vertices belonging to the same connected component, we can say that cycle exists.

Source: https://stackoverflow.com/questions/61167751/can-we-detect-cycles-in-directed-graph-using-union-find-data-structure

### Examples
[[LC-684. Redundant Connection]]
- This is the case where the tree has no cycles and is an undirected graph. Then we just need to remove one of the two edges that make up the node with indegree 2.
- Use union find to detect if nodes u,v in the edge (u,v) have the same parent. If they do, this edge is redundant

 [[LC-685. Redundant Connection II]]
-  A valid graph in this context is a single rooted tree (directed graph) with no cycles. This graph is given a single extra edge.
- An edge that is redundant if it is one of two edges that enter the same node or an edge in a cycle. In the case that both scenario happens, we need to remove the edge inside the cycle otherwise it only solves one of the two problems.
- Since we are not sure which edge to remove to ensure that the node has indegree of 1, we have to keep track both edges. We want to remove the edge that is part of a cycle if there exists one. 
- It will help to store the previous node of each node in a dictionary.
- Union find will help us detect the cycle

[[LC-261. Graph Valid Tree]]
- A valid tree has 1 connected component with no cycles
- Reduces to redundant connection
- An extra check is required at the end to see if the edges have connected all the components

[[LC-323. Number of Connected Components in an Undirected Graph]] 
- Union find
- Reduce the number of connected components every time we take the union of nodes u and v
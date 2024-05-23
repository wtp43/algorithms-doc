---
---
:::note[note] 

Union Find stores the index of each element's parent 

:::

## Union Find Optimizations

- Weighted union: Keep track of size to keep balanced trees. Root of subtree with lesser number of nodes points towards the root of subtree with larger amount of nodes which leads to reduction of tree's height
	- These will not necessarily result in binary trees
	- This limits the total depth of the tree to O(logn) because the depth of nodes only in the smaller tree will now increase by one and the depth of the deepest node in the combined tree can only be at most one deeper than the deepest node before the trees were combined. The total number of nodes in the combined tree is therefore at least twice the number in the smaller subtree. Thus the depth of any node can be increased at most logn times where n equivalences are processed (since each addition to the depth must be accompanied by at least doubling the size of the tree).
	- https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/UnionFind.html
- Path compression when finding parents
- Weighted Union by Rank
	- Instead of saving the size, save the rank/height of the trees
```python
# x and y are not in same set, so we merge them
if xRoot.rank < yRoot.rank 
  xRoot.parent := yRoot 
else if xRoot.rank > yRoot.rank
  yRoot.parent := xRoot
else
 xRoot.parent := yRoot
 yRoot.rank   := yRoot.rank + 1
```

## Disjoint Sets to find longest consecutive sequence in a set


```python
class Union_find:
	def __init__(self,n):
		self.n = n
		self.parent = list(range(n))
		self.size = [1]*n

	#Path compression used to shorten path to parent O(loglogn)
	def find(self,x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	#Observe that it is the parents of i,j that are being merged
	def union(self, x, y):
		i = self.find(x)
		j = self.find(y)
		
		if i == j:
			return
		# bigger parent stays the parent
		if self.size[i] < self.size[j]:
			self.parent[i] = j
			self.size[j] += self.size[i]
		else:
			self.parent[j] = self.parent[i]
			self.size[i] += self.size[j]
			
	def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        return True
```

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

## Cycle Detection for Undirected Graphs

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
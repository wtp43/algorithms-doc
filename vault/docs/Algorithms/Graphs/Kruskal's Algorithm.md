---
---
- Greedy algorithm to finding minimum spanning trees that is more efficient on sparse graphs than Prim's algorithm
- Kruskal's algorithm repeatedly considers the lightest remaining edge and adds it if the two vertices lie within different components (to prevent cycles)
- Union-find can be used to store disjoint sets

```python
def kruskal(graph):
	mst = []
	uf = Union_find(graph.get_vertices())
	edges = graph.get_edges()
	# sort edges by cost
	edges.sort(key = lambda x: x[2])
	for u,v,cost in edges:
		if uf.find(u) != uf.find(v):
			mst.append([u,v,cost])
			uf.union(u,v)
	return mst

mst_weight = sum(t[2] for t in mst)
```

## Optimizations
- Suppose we know that the cost for every edge is bounded by U
- Using [[Count Sort| count sort]] allows us to upper bound the sort to O(E + U)
- Union find 
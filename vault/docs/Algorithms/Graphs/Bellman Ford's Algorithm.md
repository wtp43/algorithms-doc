---
---
>[!note]
Bellman Ford iteratively relaxes the distance from u to v 
**Complexity**: O(VE) Intuitively, |V-1| iterations are needed because that's the largest amount of stops the longest possible shortest path from source s to destination v can have. 

- Finds the shortest path from a starting vertex to all other vertices in a weighted graph
- Works for negative weights
- Good for detecting [[negative weight cycles]] as the algorithm converges to an optimal solution in O(V*E) steps
- If the resultant is not optimal, then the graph contains a negative weight cycle
- Dijkstra's algorithm can handle positive weighted cycles but not negative weighted cycles

```python
def bellman_ford(graph, start):
	num_vertices = len(graph.get_vertices())
	edges = graph.get_edges()

	dist = [math.inf for i in range(num_vertices)]
	prev = [None for i in range(num_vertices)]

	dist[start] = 0
	#relax edges |V| - 1 times
	for _ in range(num_vertices - 1):
		for u, v, w in edges:
			new_dist = dist[u] + w
			if new_dist < dist[v]:
				dist[v] = new_dist
				prev[v] = u

	#detect negative cycles
	for u,v,w in edges:
		if dist[u] + w < dist[v]:
			raise NegativeWeightCycleError()
	return dist, prev
```

### Backlinks
---

[[Graph Theory]]
[[Floyd-Warshall's Algorithm]]
---
---
## Adjacency Matrix
![[Pasted image 20221202190928.png]]
Pros
- Useful for dense graphs with many edges
- Allows for matrix operations
-  Edge weight lookup is O(1)
Cons
- O($V^2$) space requirement
- Iterating over all edges takes O($V^2$) time

## Adjacency List
![[Pasted image 20221202190703.png]]
Pros
- Space efficient for sparse graphs
- Iterating over all edges
Cons
- Edge weight lookup is O(E) although rare in practice
- Less space efficient for denser graphs (overhead in linked list structure)

## Edge List
- Unordered list of edges: `[(u1,v1,w1), (u2,v2,w2)]`
- Seldomly used because of its lack of structure

# Implementation

### Adjacency Matrix

```python
from collections import defaultdict
class Graph:
	def __init__(self, size, directed=True):
		self.matrix = [[0]*size for _ in range(size)]
		self.size = size
		self.directed = directed
	
	def add_edge(self, v1, v2, weight=1):
		self.matrix[v1][v2] = weight
		if not self.directed:
			self.matrix[v2][v1] = weight
		
	def remove_edge(self, v1, v2):
		self.matrix[v1][v2] = 0
		if not self.directed:
			self.matrix[v2][v1] = 0
			
	def get_weight(self, v1, v2):
		return self.matrix[u1][u2]

	def get_edges(self):
		edges = []
		for i in range(self.size):
			for j in range(self.size):
				if self.matrix[i][j]:
					edges.apend([(i,j), matrix[i][j]])
		return edges
		
	def print_matrix(self):
	    print(self.matrix)

graph = Graph(5)
graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)
graph.print_matrix()
```

![[Pasted image 20221205181815.png]]

## Adjacency list
- Use dictionary and store a set containing values as pairs of (node, weight)
```python
from collections import defaultdict
class Graph:
	def __init__(self, directed=True):
		self.d = defaultdict(dict)
		self.vertices = set()
		self.directed = directed

	def add_vertex(self, v):
		self.vertices.add(v)

	def remove_vertex(self, v):
		self.vertices.remove(v)

	def add_edge(self, v1, v2, weight=1):
		if v1 not in self.vertices:
			self.add_vertex(v1)
		if v2 not in self.vertices:
			self.add_vertex(v2)
		self.d[v1][v2] = weight
		if not self.directed:
			self.d[v2][v1] = weight
		
	def remove_edge(self, v1, v2):
		self.d[v1].pop(v2)
		if not self.d[v1]:
			self.remove_vertex(v1)
		if not self.directed:
			self.d[v2].pop(v1)
			if not self.d[v2]:
				self.remove_vertex(v2)

	def get_weight(self, v1, v2):
		return self.d[v1][v2]

	#returns out neighbors for a directed graph
	def get_neighbors(self, v):
		return self.d[v].keys()
		
	def get_edges(self, start=None):
		edges = []
		if start:
			for v in self.d[start]:
				edges.append([start, v, self.d[start][v]])
		else:
			for u in self.d:
			    for v in self.d[u]:
			        edges.append([u,v,self.d[u][v]])
		return edges
	
	def get_vertices(self):
	    return self.vertices
		
graph = Graph()
graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)
print(graph.get_edges())
print(graph.get_vertice())
```

# Related
[Graph Theory](</docs/DS/Graph Theory.md>)
---
---

:::Note[Note] 


:::
>Greedy Algorithm: Start from one vertex and keep adding edges with the lowest weight until we get a minimum spanning tree
>Complexity: O(E log V)
# Pseudocode
1. Initialize minimum spanning tree with a any vertex
2. Find all edges that connect the tree to new vertices. Add the minimum edge to the tree
3. Repeat step 2 by adding all new edges from the newly connected vertex until we get a minimum spanning tree

# Proof of Optimality (using contradiction)

Suppose there exists a graph G in which Prim's algorithm doesn't return a minimum spanning tree. Then there must have been some particular instant where we went wrong. Before we inserted edge $(x,y)$, $T_{prim}$ consisted of a set of edges that was a subtree of some minimum spanning tree $T_{min}$. Choosing $(x,y)$ took us away from any possible minimum spanning tree.

Then there must be a path $p$ from $x$ to $y$ in $T_{min}$ like in figure *b)*. $p$ must use an edge $(v_1,v_2)$ where $v_1$ is in $T_{prim}$ but $v_2$ is not. $(v_1,v_2)$ must have weight at least that of $(x,y)$ or else Prim's algorithm would have selected it before $(x,y)$. Inserting $(x,y)$ and deleting $(v_1, v_2)$ from $T_{min}$ leaves a spanning tree no larger than before, meaning that Prim's algorithm could not have made a fatal mistake in selecting edge $(x,y)$. Therefore, by contradiction, Prim's algorithm must construct a minimum spanning tree.

# Implementation

## Approach #1: Adjacency Matrix
Complexity O($V^2$) instead of O(VE) since we don't iterate all edges
- dist stores the cost of adding the vertex to the tree
- Keep track of cheapest edge linking very non-tree vertex in the tree
- The cheapest such edge over all remaining no-tree vertices gets added in the next iteration

```python
def prim(graph, start):
	n_vertices = len(graph.get_vertices())
	dist = [math.inf for _ in range(n_vertices)]
	seen = [0 for _ in range(n_vertices)]
	parent = [-1 for _ in range(n_vertices)]
	dist[start] = 0

	u = start
	while (not seen[u]):
		seen[u] = 1
		# update all weights from u to its neighbors (v)
		for v in graph.get_neighbors(u):
			weight = graph.get_weight(u,v)
			if not seen[v] and weight < dist[v]:
				dist[v] = weight
				parent[v] = u

		# find the unvisited vertex with the smallest weighted edge 
		# to iterate from 
		cur_dist = math.inf
		for i in range(n_vertices):
			if not seen[i] and dist[i] < cur_dist:
				cur_dist = dist[i]
				u = i
	
	return parent, dist
```


## Approach #2: Adjacency List + Priority Queue (Heap)
Complexity O(E log V)
-  Start from an arbitrary vertex
- Keep track of the minimum distance to every other node in a heap
- The log V comes from 
- Consider the vertex with the least cost that has not been visited yet
- Implementation in python requires a modification of heapq since it does not provide a decrease-key function
- Typically, no decrease-key function is used and instead just append and invalidate entries later on in which case, the complexity is same as Kruskal's


```
MST-PRIM(G, w, r)
1  for each u ∈ G.V
2       u.key ← ∞
3       u.π ← NIL
4   r.key ← 0
5   Q ← G.V
6   while Q ≠ Ø
7       u ← EXTRACT-MIN(Q)
8       for each v ∈ G.Adjacent[u]
9           if v ∈ Q and w(u, v) < v.key
10              v.π ← u
11              v.key ← w(u, v)
```

**Using a Binary Heap**

1. The time complexity required for one call to `EXTRACT-MIN(Q)` is `O(log V)` using a min priority queue. The while loop at line 6 is executing total V times.so `EXTRACT-MIN(Q)` is called `V` times. So the complexity of `EXTRACT-MIN(Q)` is `O(V logV)`.
    
2. The `for` loop at line 8 is executing total `2E` times as length of each adjacency lists is `2E` for an undirected graph. The time required to execute line 11 is `O(log v)` by using the `DECREASE_KEY` operation on the min heap. Line 11 also executes total `2E` times. So the total time required to execute line 11 is `O(2E logV) = O(E logV)`.
    
3. The `for` loop at line 1 will be executed `V` times. Using the procedure to perform lines 1 to 5 will require a complexity of `O(V)`.
    

Total time complexity of `MST-PRIM` is the sum of the time complexity required to execute steps 1 through 3 for a total of `O((VlogV) + (E logV) + (V)) = O(E logV)` since `|E| >= |V|`.

**Using a Fibonacci Heap**

1. Same as above.
2. Executing line 11 requires `O(1)` amortized time. Line 11 executes a total of `2E` times. So the total time complexity is `O(E)`.
3. Same as above

So the total time complexity of `MST-PRIM` is the sum of executing steps 1 through 3 for a total complexity of `O(V logV + E + V)=O(E + V logV)`.

## Source
- https://stackoverflow.com/questions/20430740/time-complexity-of-prims-algorithm

:::example[example] 


:::
>```python
>graph = Graph(directed=False)
>graph.add_edge('A', 'B', 2)
>graph.add_edge('A', 'C', 3)
>graph.add_edge('B', 'C', 1)
>graph.add_edge('B', 'D', 1)
>graph.add_edge('B', 'E', 4)
>graph.add_edge('C', 'F', 5)
>graph.add_edge('D', 'E', 1)
>graph.add_edge('E', 'F', 1)
>graph.add_edge('F', 'G', 1)
>mst, total_cost = prim(graph, 'A')
>
>assert(total_cost==29)
>assert(mst == {'A': set(['B']), 'B': set(['C', 'D']), 
> 				'D': set(['E']), 'E': set(['F']), 
> 				'F': set(['G'])})


![Pasted-image-20221208044247.png](</Pasted-image-20221208044247.png>)

## Optimizations
- Suppose we know that the cost for every edge is bounded by U
- Instead of using a priority queue (heap), a bucket sort can be implemented in 

# Prim vs Dikjstra
Prim's algorithm constructs a [minimum spanning tree](http://en.wikipedia.org/wiki/Minimum_spanning_tree) for the graph, which is a tree that connects all nodes in the graph and has the least total cost among all trees that connect all the nodes. However, the length of a path between any two nodes in the MST might not be the shortest path between those two nodes in the original graph. MSTs are useful, for example, if you wanted to physically wire up the nodes in the graph to provide electricity to them at the least total cost. It doesn't matter that the path length between two nodes might not be optimal, since all you care about is the fact that they're connected.

Dijkstra's algorithm constructs a [shortest path tree](http://en.wikipedia.org/wiki/Shortest_path_tree) starting from some source node. A shortest path tree is a tree that connects all nodes in the graph back to the source node and has the property that the length of any path from the source node to any other node in the graph is minimized. This is useful, for example, if you wanted to build a road network that made it as efficient as possible for everyone to get to some major important landmark. However, the shortest path tree is not guaranteed to be a minimum spanning tree, and the sum of the costs on the edges of a shortest-path tree can be much larger than the cost of an MST.

Another important difference concerns what types of graphs the algorithms work on. Prim's algorithm works on undirected graphs only, since the concept of an MST assumes that graphs are inherently undirected. (There is something called a "minimum spanning arborescence" for directed graphs, but algorithms to find them are much more complicated). Dijkstra's algorithm will work fine on directed graphs, since shortest path trees can indeed be directed. Additionally, Dijkstra's algorithm [does not necessarily yield the correct solution in graphs containing negative edge weights](https://stackoverflow.com/questions/6799172/negative-weights-using-dijkstra-algorithm/6799344#6799344), while Prim's algorithm can handle this. (https://stackoverflow.com/questions/14144279/difference-between-prims-and-dijkstras-algorithms)


The main difference is here: for Prim `graph[u][v] < key[v]`, and for Dijkstra `dist[u]+graph[u][v] < dist[v]`

Dijkstra's algorithm doesn't create a MST, it finds the shortest path.

Consider this graph

```
       5     5
  s *-----*d-----* t
     \         /
       -------
         9
```

The shortest path is 9, while the MST is a different 'path' at 10.

### References
https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/



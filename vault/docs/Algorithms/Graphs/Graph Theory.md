---
---
# Types of Graphs
## Undirected Graph 
- Edges are bidirectional

## Directed Graphs (digraph)
- Edges only point in 1 direction

## Directed Acyclic Graphs (DAG)
- Topological sorting is the most important operation on DAG's

## Weighted Graphs
- Edges contain a certain weight

## Tree
- Undirected graph with no cycles

## Rooted Tree
- Tree with a designated root node
- Arborescence (out-tree) has all edges pointing away from the root
- Anti-arborescence (in-tree) has all edges pointing towards the root
- All out-trees are DAGs but not all DAGs are out-trees

## Bipartite Graph
- All vertices can be split into two independent groups U, V such that every edge connects between U and V
- Two colourable or there is no odd length cycle

## Connected Graph
- Graph in which there is always a path from a vertex to any other vertex

## Complete Graph
- Graph in which there is a unique edge between every pair of nodes
- A complete graph with n vertices is denoted as $K_n$
- Good way to test worst case scenario in an algorithm because of how many edges there are
- ${n \choose 2}$ =  $n(n-1)/2$ edges

## Spanning Tree
 - Sub-graph of an undirected connected graph which includes all the vertices of a graph with a minimum possible number of edges. (Must include all vertices)
 - Edges may have weights
 - $n-1$ edges
 - Remove a maximum of e - n + 1 edges from a complete graph to construct a spanning tree
 
>[!Note]
>The total number of spanning trees with `n` vertices that can be created from a complete graph is equal to $n^{(n-2)}$

## Minimum Spanning Tree
- Spanning tree in which sum of weight of edges are minimized
- Has no cycles

# Graph Representations
1. [[Graph Structures#Adjacency Matrix| Adjacency Matrix]]
2. [[Graph Structures#Adjacency List| Adjacency List]]


# Problems in Graph Theory
## [[Graph Theory#Connected Graph|Connectivity]]
>[!question]
Does there exist a path between node A and node B?
- [[Union Find (Disjoint Sets)]]
- [[BFS]]
- [[DFS]] 
## [[Strongly Connected Components]]
1. [[Tarjan's Strongy Connected Component Algorithm]]
2. [[Kosaraju's Algorithm]]

## Negative Cycles
>[!question]
Does my weighted digraph have any negative cycles? If so, where?
- [[Bellman Ford's Algorithm]]
- [[Floyd-Warshall's Algorithm]]

## [[Graph Theory#Minimum Spanning Tree|Minimum Spanning Tree]] Algorithms
1. [[Prim's Algorithm]]
2. [[Kruskal's Algorithm]]

## Shortest Path Algorithms
1. [[BFS]]: used if weights are the same. [[DFS]] does not necessarily yield shortest paths in an undirected graph.
	- [[Iterative Deepening Search (IDS)]] combines both BFS and DFS
2. [[Bellman Ford's Algorithm]]
3. [[Floyd-Warshall's Algorithm]]: used to find the shortest paths from a source vertex to all other vertices in a weighted graph

## Traveling Salesman Problem
Algorithms used in the [[Traveling Salesman Problem]]
1. [[Held-karp]]

## [[Bridges Algorithm]]
- A bridge / cut edge is any edge in a graph whose removal increases the number of connected components
- Often important in graph theory because they hint at weak points, bottlenecks or vulnerabilities in a graph
## Articulation Point 
- An articulation point / cut vertex is a node in a graph whose removal increases the number of connected components

## Network flow: max flow Algorithms
>![question]
>With an infinite input source, how much "flow" can we push through the network?
1. [[Ford-Fulkerson Algorithm]]
2. [[Edmonds-Karp Algorithm]]
3. [[Dinic's Algorithm]]

## [[Matrix Traversals]]
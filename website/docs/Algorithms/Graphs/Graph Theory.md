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
 
:::Note[Note] 

The total number of spanning trees with `n` vertices that can be created from a complete graph is equal to $n^{(n-2)}$

:::

## Minimum Spanning Tree
- Spanning tree in which sum of weight of edges are minimized
- Has no cycles

# Graph Representations
1. [[Graph Structures#Adjacency Matrix| Adjacency Matrix]]
2. [[Graph Structures#Adjacency List| Adjacency List]]


# Problems in Graph Theory
## [[Graph Theory#Connected Graph|Connectivity]]
:::question[question] 


:::
Does there exist a path between node A and node B?
[Union Find (Disjoint Sets)](</docs/Algorithms/Graphs/Union Find (Disjoint Sets).md>)[BFS](</docs/Algorithms/Graphs/BFS.md>)[DFS](</docs/Algorithms/Graphs/DFS.md>)[Strongly Connected Components](</docs/Algorithms/Graphs/Strongly Connected Components.md>)1. [[Tarjan's Strongy Connected Component Algorithm]]
[Kosaraju's Algorith](</docs/Algorithms/Kosaraju's Algorithm.md>)
## Negative Cycles
:::question[question] 


:::
Does my weighted digraph have any negative cycles? If so, where?
[Bellman Ford's Algorith](</docs/Algorithms/Graphs/Bellman Ford's Algorithm.md>)[Floyd-Warshall's Algorith](</docs/Algorithms/Graphs/Floyd-Warshall's Algorithm.md>)
## [[Graph Theory#Minimum Spanning Tree|Minimum Spanning Tree]] Algorithms
[Prim's Algorith](</docs/Algorithms/Graphs/Prim's Algorithm.md>)[Kruskal's Algorith](</docs/Algorithms/Graphs/Kruskal's Algorithm.md>)
## Shortest Path Algorithms
[BFS](</docs/Algorithms/Graphs/BFS.md>)[Iterative Deepening Search (IDS)](</docs/Algorithms/Graphs/Iterative Deepening Search (IDS).md>)[Bellman Ford's Algorith](</docs/Algorithms/Graphs/Bellman Ford's Algorithm.md>)[Floyd-Warshall's Algorith](</docs/Algorithms/Graphs/Floyd-Warshall's Algorithm.md>)
## Traveling Salesman Problem
Algorithms used in the [[Traveling Salesman Problem]]
1. [[Held-karp]]

[Bridges Algorith](</docs/Algorithms/Graphs/Bridges Algorithm.md>)- A bridge / cut edge is any edge in a graph whose removal increases the number of connected components
- Often important in graph theory because they hint at weak points, bottlenecks or vulnerabilities in a graph
## Articulation Point 
- An articulation point / cut vertex is a node in a graph whose removal increases the number of connected components

## Network flow: max flow Algorithms
>![question]
>With an infinite input source, how much "flow" can we push through the network?
1. [[Ford-Fulkerson Algorithm]]
[Edmonds-Karp Algorith](</docs/Algorithms/Edmonds-Karp Algorithm.md>)3. [[Dinic's Algorithm]]

[Matrix Traversals](</docs/Algorithms/Arrays/Matrix Traversals.md>)
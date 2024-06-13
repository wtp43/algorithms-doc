---
title:  "Cycle Detection in Directed Graphs"
created: 2023-01-06
---
# Cycle Detection
## Directed Graphs
### Using Topological Search (3 Coloring)

Use the following approach: consider we have three colors, and each vertex should be painted with one of these colors. 0 means that the vertex hasn't been visited yet. 1 means that we've visited the vertex but haven't visited all vertices in its subtree. 2 means we've visited all vertices in subtree and left the vertex. So, initially all vertices are 0. When we visit the vertex, we should paint it 1. When we leave the vertex (that is we are at the end of the _dfs()_ function, after going through all edges from the vertex), we should paint it 2. If you use that approach, you just need to change _dfs()_ a little bit. Assume we are going to walk through the edge u->v. If v is 0, go there. If v is 2, don't do anything. If v is 1, you've found the cycle because you haven't left v yet (it's 1, not 2), but you come there one more time after walking through some path.
### Union Find
- If two vertices that you are merging have the same parent, a cycle exists
## Undirected Graphs


## Shortest Cycle in Undirected Graph
https://leetcode.com/problems/shortest-cycle-in-a-graph/
- Same idea applies for directed
- BFS on each vertex
- Optimization: 
	- Topological Sort
	- Discard all nodes with in_degree = 1
```python
def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
#We can do an optimization here: using topological sort to remove vertices that are not in cycles, and then perform a vertex with maximum degree to do BFS. After BFS, we remove this vertex from the graph. Repeat the procedure above until there is no vertex left.
#Such optimization can drastically improve the efficiency of algorithm.

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res = math.inf
        for i in range(n):
            q = [i]
            dist = [math.inf]*n
            dist[i] = 0
            while q:
                nextq = []
                for u in q:
                    for v in graph[u]:
                        if dist[v] == math.inf:
                            dist[v] = 1+dist[u]
                            nextq.append(v)
                        # there is a cycle if we reach u and v 
                        elif dist[u] <= dist[v]:
                            # can't break early here since it might not be the shortest cycle
                            res = min(res, dist[u] + dist[v] + 1)
                q = nextq
        return res if res != math.inf else -1
```
# Related







---
title:  "Cycle Detection in Directed Graphs"
created: 2023-01-06
---
# Using Topological Search (3 Coloring)

Use the following approach: consider we have three colors, and each vertex should be painted with one of these colors. 0 means that the vertex hasn't been visited yet. 1 means that we've visited the vertex but haven't visited all vertices in its subtree. 2 means we've visited all vertices in subtree and left the vertex. So, initially all vertices are 0. When we visit the vertex, we should paint it 1. When we leave the vertex (that is we are at the end of the _dfs()_ function, after going through all edges from the vertex), we should paint it 2. If you use that approach, you just need to change _dfs()_ a little bit. Assume we are going to walk through the edge u->v. If v is 0, go there. If v is 2, don't do anything. If v is 1, you've found the cycle because you haven't left v yet (it's 1, not 2), but you come there one more time after walking through some path.

# Union Find
- If two vertices that you are merging have the same parent, a cycle exists

# Related






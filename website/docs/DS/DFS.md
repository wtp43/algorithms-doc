---
---

## Pros vs BFS
- Space complexity O(depth) nodes compared to O(|V|) = O(n) for BFS

## Time Complexity

## Space Complexity


```python
seen = set()

def dfs(graph: Dict[int, List[int]], cur: int):
    if cur in seen: return
    seen.add(cur)
    for next in graph[cur]:
        dfs(graph, next)
```
- Alternatively, graph and seen can be set as global variables. 
- 'seen' does not need to be marked as `global` inside `dfs` to modify it because we are not reassigning its value using 
# Brute Force
We can traverse in a DFS fashion by linearly searching for the child nodes.
This will take O(n) to search for each child and in the worst case, the depth is n, time complexity will be O($n^n$).

# Use Cases

[Connected Components](</docs/DS/Connected Components.md>)- Start DFS at every node (except if it's already been visited) and mark all reachable nodes as being part of the same component
[LC-200. Number of Islands](</docs/Algos Practice/Leetcode Questions/LC-200. Number of Islands.md>)
## Depth-First-Search Traversals

### Pre-order Traversal

### In-order Traversal

### Post-order Traversal
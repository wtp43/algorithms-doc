---
title:  "Iterative Deepening Search (IDS)"
created: 2022-12-10
---

```toc 
style: number 
min_depth: 1 
max_depth: 6
```

# Iterative Deepening Search (IDS)
- Perform DFS 
# Implementation

```python
# Returns true if target is reachable from src within max_depth
def IDDFS(src, target, max_depth):
    for limit in range(max_depth)
       if DLS(src, target, limit):
           return True
    return False   

def DLS(src, target, limit):
    if (src == target)
        return true;

    # If reached the maximum depth, stop recursing.
    if (limit <= 0)
        return false;   

    for i in src.neighbors():
        if DLS(i, target, limit-1)             
            return true

    return false
```

## Optimizations

## Optimized Complexity

>[!Time Complexity]

>[!Space Complexity]



# Related

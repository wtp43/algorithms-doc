---
title:  "Floyd Warshall's Algorithm"
created: 2023-01-06
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Floyd Warshall's Algorithm
Dynamic Programming
# Implementation

```python
def floyd(G):
    dis = [[math.inf] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {sum(d <= maxd for d in dis[i]): i for i in range(n)}

        return res[min(res)]
```

## Optimizations

## Optimized Complexity

>[!Time Complexity]+

>[!Space Complexity]+



# Related

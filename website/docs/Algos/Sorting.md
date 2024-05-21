---
title:  "Sorting"
created: 2022-12-15
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Sorting


```python
def closest_values(arr):
	arr.sort()
	min_val, i = min((arr[i] - arr[i-1], i) for i in range(1, len(arr)))
	return min_val, i 
```

# Implementation

```python

```

## Optimizations

## Optimized Complexity

>[!Time Complexity]+

>[!Space Complexity]+



# Related

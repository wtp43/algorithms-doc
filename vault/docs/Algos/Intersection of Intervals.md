---
title:  "Intersection of Intervals"
created: 2023-01-05
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```

# Solving Interval Problems
1. Sort intervals/pairs in increasing order of the start position.
2. Scan the sorted intervals, and maintain an "active set" for overlapping intervals. At most times, we do not need to use an explicit set to store them. Instead, we just need to maintain several key parameters, e.g. the number of overlapping intervals (count), the minimum ending point among all overlapping intervals (minEnd).
3. If the interval that we are currently checking overlaps with the active set, which can be characterized by cur.start > minEnd, we need to renew those key parameters or change some states.
4. If the current interval does not overlap with the active set, we just drop current active set, record some parameters, and create a new active set that contains the current interval.

```csharp
int count = 0; // Global parameters that are useful for results.
int minEnd = INT_MAX; // Key parameters characterizing the "active set" for overlapping intervals, e.g. the minimum ending point among all overlapping intervals.
sort(points.begin(), points.end()); // Sorting the intervals/pairs in ascending order of its starting point
for each interval {
      if(interval.start > minEnd) { // If the 
	 // changing some states, record some information, and start a new active set. 
	count++;
	minEnd = p.second;
      }
     else {
	// renew key parameters of the active set
	minEnd = min(minEnd, p.second);
      } 
 }
return the result recorded in or calculated from the global information;
```
# Intersection of Intervals
Given n intervals $[li,ri)$ for $i = 0,...,n − 1,$ we wish to find a value x included in a maximum number of intervals. Here is a solution in time O(nlogn). 

We sort the endpoints, and then sweep them from left to right with an imaginary pointer x. 
A counter c keeps track of the number of intervals whose beginning has been seen, but not yet the end, hence it counts the number of intervals containing x.

Note that the order of processing of the elements of B guarantees that the right endpoints of the intervals are handled before the left endpoints of the intervals, which is necessary when dealing with intervals that are half-open to the right.
# Implementation

```python
def max_interval_intersec(S):
	B = ([(left, +1) for left, right in S] +
	[(right, -1) for left, right in S]) 
	B.sort()
	c = 0
	best = (c, None) 
	for x, d in B:
		c += d
		if best[0] < c:
			best = (c, x) 
	return best
```

## Optimizations

## Optimized Complexity

>[!Time Complexity]+

>[!Space Complexity]+



# Related
[[Sweep Line]]


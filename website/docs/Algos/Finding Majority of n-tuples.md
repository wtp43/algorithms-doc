---
title:  "Finding Majority of n tuples"

created: 2023-01-05
---




# Finding Majority of n-tuples
[Boyer-Moore Voting Algorith](</docs/Algos/Boyer-Moore Voting Algorithm.md>)# Dictionary Implementation

```python
def majority(L): count = {}
	for word in L:
		if word in count:
			count[word] += 1 
		else:
	        count[word] = 1
# Using min() like this gives the first word with
# maximal count "for free"
val_1st_max, arg_1st_max = min((-count[word], word) for word in count) 
return arg_1st_max

```

## Optimizations

## Optimized Complexity

:::Time-Complexity[Time Complexity] 

O($n^2k$)
The average complexity is O($nk$) but O($n^2k$) because of the use of a dictionary. In the worst case, your hash map will degenerate into a linked list and you will suffer an O(N) penalty for lookups, as well as inserts and deletions, both of which require a lookup operation.

:::

:::Space-Complexity[Space Complexity] 

O(n)

:::

# Related
[Boyer-Moore Voting Algorith](</docs/Algos/Boyer-Moore Voting Algorithm.md>)
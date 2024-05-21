---
dg-publish: true
title:  "LC 3. Longest Substring Without Repeating Characters"
created: 2023-01-23
---


# Description

# Brute Force
# Intuition

>[!danger]+ Intuition

# Implementation
```python
def lengthOfLongestSubstring(self, s: str) -> int:
	seen = set()
	i = 0
	max_length = 0
	for j,c in enumerate(s):
		while c in seen:
			seen.remove(s[i])
			i+=1
		seen.add(c)
		max_length = max(max_length, j-i+1)

	return max_length
```

>[!example]+ 


# Related

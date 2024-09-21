# KMP
## Pattern Matching

### Maximal Boundaries

- Maximal boundary is longest prefix that is also a suffix
>[!important]
>F is an array of maximal boundaries for every substring `s[0:i] for i in range(len(s))`

```python
def maximum_border_length(w):
	n = len(w)
	f = [0] * n # init f[0] = 0
	k = 0 # current longest border length
	for i in range(1, n): # compute f[i]
		while w[k] != w[i] and k > 0:
			k = f[k - 1] # mismatch: try the next border
		if w[k] == w[i]: # last characters match
			k += 1 # we can increment the border length
			f[i] = k # we found the maximal border of w[:i + 1]
	return f
```

### KMP

- Search t in s

```python
def KMP(s, t):
	w = t + "#" + s
	f = [0] * len(w) # init f[0] = 0
	k = 0 # current longest border length
	for i in range(1, len(w)): # compute f[i]
		while w[k] != w[i] and k > 0:
			k = f[k - 1] # mismatch: try the next border
		if w[k] == w[i]: # last characters match
			k += 1 # we can increment the border length
			f[i] = k # we found the maximal border of w[:i + 1]
			if f[i] == n:
				return i - 2*n #2n accounts for the searched word, -1 omitted for the separator used
	return f
```

```python
# kmp(word + '$' + target)
def kmp(self, s: str) -> str:
	a = [0]*len(s) 
	k = 0
	for i in range(1,len(s)): 
		k = a[i-1]
		while k and s[k] != s[i]: 
			k = a[k-1]
		f[i] = k + (s[k]==s[i]) 
	return a[:f[-1]]
```

Space/Time Complexity: O(m + n)
##### Searching for All Occurrences
https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/
- Don't return after once match
### Isomorphic Strings (Mapping)

```python
def isIsomorphic(self, s: str, t: str) -> bool:
	map_s = {}
	map_t = {}
	for c1, c2 in zip(s,t):
		if c1 not in map_s and c2 not in map_t:
			map_s[c1] = c2
			map_t[c2] = c1
		elif map_s.get(c1) != c2 or map_t.get(c2) != c1:
			return False
	return True
```

---
---
## Top K Frequent Elements
- Dictionary then sort by frequency
- Append 
- $O(nlogn)$
```python
d = {}
ans = []

for e in nums:
	d.append(e)
	
for key, val in sorted(d.items(), key = lambda x: x[1], reverse=True):
	k -= 1
	ans.append(key) 
	if k == 0:
		break
```
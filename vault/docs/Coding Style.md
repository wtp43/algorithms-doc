## Updating Result
### When result is updated before current element
- The result may not be updated by the last subarray
- Run to len(arr) + 1 
```python
def checkZeroOnes(self, s: str) -> bool:
	d = defaultdict(int)
	cur = 1
	for i in range(1,len(s)+1):
		if i == len(s) or s[i] != s[i-1]:
			d[s[i-1]] = max(d[s[i-1]], cur)
			cur = 1
		else:
			cur += 1
	return d['1']>d['0']
```

### Check if Binary String has at Most One Segment of Ones
- Left strip '0's, we should be left with all '1's
- Then left strip '1's
- Return true if string is empty


## Prefix, Suffix
- pre,suf = 0, sum(arr)
- for loop:
	- cur += i
	- suf -= i
## Transpose Matrix with Python Zip
- To get max values of each column
- Use transpose or zip
```python
transpose = [[matrix[j][i] for j in range(m)] for i in range(n)]
maxcol = {max(c) for c in zip(*matrix)}
```
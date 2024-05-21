---
created: ""
---
---
>[!summary]- Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```
# LC Hard
## Backtrack
#### Build sentence by inserting spaces into string given dictionary of valid words
+ Approach #1: Check index of i,j to see if it is a word that belongs in dictionary while backtracking
+ Approach #2: Loop through every valid word. Check if i:i+len(word)+1 is equal to the word
```python
def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
	res = []
	n = len(s)
	cur = []
	start = set()
	for word in wordDict:
		start.add(word[0])
	word = ''
	def backtrack(i,j):
		nonlocal word, cur
		if i >= n:
			res.append(' '.join(cur))
			return
		if j >= n:
			return
		if s[i] not in start:
			return
		word += s[j]
		if word in wordDict:
			cur.append(word)
			tmp = word
			word = ''
			backtrack(j+1, j+1)
			word = tmp
			cur.pop()
		backtrack(i, j+1) 
	backtrack(0,0)
	return res
```
https://leetcode.com/problems/word-break-ii/description/

## Binary Search
### Divide Chocolate
https://leetcode.com/problems/divide-chocolate/description/
- Divide chocolate with k cuts (k + 1 pieces)
- Binary search + greedy
- Return hi since we want the biggest
```python
def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
	#cuts can be represented by choosing a max chunk threshold
	if k < 1:
		return sum(sweetness)
	k += 1
	lo = min(sweetness)
	hi = max(sweetness) * math.ceil(len(sweetness)/k)
	while lo <= hi:
		mid = lo + (hi-lo)//2
		chunk = 0
		count = 1
		for s in sweetness:
			if s + chunk < mid:
				chunk += s
			else:
				count += 1
				chunk = 0
				if count > k:
					break
		if count > k:
			lo = mid + 1
		else:
			hi = mid - 1
	return hi
def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
	#cuts can be represented by choosing a max chunk threshold
	if k < 1:
		return sum(sweetness)
	k += 1
	lo = min(sweetness)
	# the maximum of the minimum chunk cannot be greater than the size of an even split
	hi = math.ceil(sum(sweetness)/(k))
	while lo <= hi:
		mid =lo + (hi-lo)//2
		chunk = 0
		count = 0
		#!!!! Update chunk after every num, not just 
			# if number of chunks not reached (ie: last chunk is less than threshold)
			# this means we can decrease the threshold
		for s in sweetness:
			chunk += s
			if chunk >= mid:
				count += 1
				chunk = 0
		# this is a left bisect
		if count >= k:
			lo = mid + 1
		else:
			hi = mid - 1
	return hi
```
- We only have a chunk if the threshold is met
- Enumerate possibilites
	- If count > k:
		- chunk threshold can be increased
	- if count == k:
		- chunk threshold can be increased
	- if count < k:
		- chunk threshold needs to be decreased
- Our binary search algorithm will keep increasing threshold until the count < k
	- Then it will decrease the chunk threshold until count == k or until hi < lo
	- Thus, our answer lies within lo - 1 = hi
### Split Array Largest Sum(Minimized)
- Minimize largest array after splitting array into k subarrays
- Key: count does not have to be to equal to k since we can have the last subarray to be smaller than the threshold
- Right Bisect on count - 1
- We want the first threshold such that count < k. In other words, the threshold is only too small if count = k - 2
- How to construct this: what happens if count >= k: (we have too many subarrays, threshold must be increased)
```python
def splitArray(self, nums: List[int], k: int) -> int:
	lo = max(nums)
	hi = max(nums) * math.ceil(len(nums)/k)
	while lo <= hi:
		mid = lo + (hi-lo)//2
		cur = 0
		count = 0
		for x in nums:
			cur += x
			if cur > mid:
				cur = x
				count += 1
		if count >= k:
			lo = mid + 1
		else:
			hi = mid - 1
	return lo
```
- the array threshold is increased until count < k
- the array threshold is then decreased until count == k
- since the answer is still valid if we have count = k - 1, which means the last subarray was just not added cause it didn't reach the threshold, we want to return lo
## Trie

```python
def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
	res = []
	m,n = len(board), len(board[0])
	trie = {} 
	WORD_KEY = '$$'
	VISITED = '=='

	def find(word):
		node = trie
		for c in word:
			if c in node:
				node = node[c]
			else:
				return False
		return node[WORD_KEY] == word 

	for word in words:
		node = trie
		for c in word:
			node = node.setdefault(c,{})
		node[WORD_KEY]= word
		
	def backtrack(row,col,parent):
		letter = board[row][col]
		cur = parent[letter]
		word_match = cur.pop(WORD_KEY, False)
		if word_match:
			res.append(word_match)

		# Set cell as visited
		board[row][col] = VISITED

		for y,x in [[0,1], [0,-1], [1,0], [-1,0]]:
			r = row+y
			c = col+x
			pos = (r, c)
			if  r< 0 or r >= m or c < 0 or c >= n: 
				continue 
			if not board[r][c] in cur:
				continue
			backtrack(r, c,cur) 
		# Restore cell	
		board[row][col] = letter
		# Prune visited leaf nodes
		if not cur:
			parent.pop(letter)

	# Be smart about where to start search, ie: only if starting letter is in trie
	for r in range(m):
		for c in range(n):
			if board[r][c] in trie:
				backtrack(r, c, trie)
	return res

```
**Complexity:** O(M(4x3)to the power of (L-1)) where M is number of cells in the grid, 4 for initial direction, 3 for possible directions to backtrack, and L is the length of the longest word in the trie
**Space:** O(Number of characters inside the dictionary) and x2 if we store the word inside too
https://leetcode.com/problems/word-search-ii/description

## Graphs

### MST
#### Critical and Pseudo-critical edges in MST
- Build MST to find min cost
- For every edge,
	- ignore it: if new mst built has higher cost, it is critical
	- force it: calculate a new mst starting with this edge. If new mst has the same cost, this edge is pseudo-critical
- Time Complexity: Building E MST's = O(EE Log E)
##### Alternative
https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solutions/1478977/100-faster-o-ev-building-mst-once-is-enough/
- Build MST
##### Optimized
https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solutions/698025/o-eloge-kruskal-tarjan/
- Use Kruskal and Tarjan's


https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/
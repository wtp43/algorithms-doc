---
title:  "Trie"
created: 2023-01-06
---
# Trie

## Implementation

```python
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.nodes = {}
            
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Inserts a word into the trie.
    def insert(self, word: str) -> None:
        cur = self.root;
        
        for c in word:
            if c not in cur.nodes:
                cur.nodes[c] = TrieNode()
            cur = cur.nodes[c]
            
        cur.isWord = True;

    # Returns if the word is in the trie
    def search(self, word: str) -> bool:
        cur = self.root
        
        for c in word:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]
            
        return cur.isWord
    # Returns if there is any word in the trie 
    # that starts with the given prefix. */
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for c in prefix:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]
            
        return True
```

### Without Class

```python
trie = {}
    for w in dictionary:
        cur = trie
        for ch in w:
            cur = cur.setdefault(ch,{})
        cur['$'] = w
    def find(w):
        cur = trie
        for ch in w:
            if ch not in cur:
                return True
            cur = cur[ch]
        return cur.get('$', False):
```

## Optimization:  Pre Order Traversal
To find all words in sorted order, iterate the alphabet instead of sorting the words.
Then we are guaranteed O(n) instead of O(nlogn) for the sort.


## Practice Problems
- [ ] [[LC-1268. Search Suggestions System]]
- Preorder traversal of a trie
	- Do not sort. Loop the alphabet instead


### Replace Words

```python
def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for w in dictionary:
            cur = trie
            for ch in w:
                cur = cur.setdefault(ch,{})
                cur = cur[ch]
            cur['$'] = w
        def find(w):
            cur = trie
            for ch in w:
                if ch not in cur:
                    return ''
                cur = cur[ch]
                if cur.get('$', ''):
                    return cur['$']
            return ''
        res = []
        words = sentence.split(' ')
        for w in words:
            root = find(w)
            if root:
                res.append(root)
            else:
                res.append(w)
        return ' '.join(res)
```


## DP + Trie

### [Construct String with Minimum Cost](https://leetcode.com/problems/construct-string-with-minimum-cost/)
> Construct target string from list of words with different costs
```python
def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
	dp = [math.inf]*(len(target)+1)
	dp[0] = 0
	trie = {}
	for w,cost in zip(words, costs):
		node = trie
		for c in w:
			node.setdefault(c, {})
			node = node[c]
		node['$'] = min(cost, node.get('$', inf))
	for i in range(len(target)):
		node = trie
		for j in range(i, len(target)):
			c = target[j]
			if c not in node:
				break
			node = node[c]
			cost = node.get('$', 0)
			if cost:
				dp[j+1] = min(dp[j+1], dp[i] + cost)

	return dp[-1] if dp[-1] != inf else -1
```

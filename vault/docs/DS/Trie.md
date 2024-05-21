---
title:  "Trie"
created: 2023-01-06
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Trie

# Implementation

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

# Pre Order Traversal
To find all words in sorted order, iterate the alphabet instead of sorting the words.
Then we are guaranteed O(n) instead of O(nlogn) for the sort.


## Optimizations

## Optimized Complexity

>[!Time Complexity]+

>[!Space Complexity]+



# Related

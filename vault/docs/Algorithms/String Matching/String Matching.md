---
---

- [ ] Huffman Encoding
- [ ] https://leetcode.com/problems/strings-differ-by-one-character/solutions/802871/rabin-karp-o-nm/
- [ ] Prefix Function: KMP: https://www.scaler.com/topics/data-structures/kmp-algorithm/
- [ ] https://leetcode.com/problems/palindrome-pairs/description/
- [ ] Rabin Karp for String Matching: https://cp-algorithms.com/string/rabin-karp.html
- [ ] Z Function: https://cp-algorithms.com/string/z-function.html#trivial-algorithm
- [ ] Suffix Array
	- [ ] https://cp-algorithms.com/string/suffix-array.html#practice-problems
- [ ] Aho-Corasick Algorithm (Similar to trie but with additional links that constructs a finite state machine in O(mk) time)
	- [ ] https://cp-algorithms.com/string/aho_corasick.html
- [ ] Suffix Tree (Advanced)


## Practice Problems
### Find Common Characters
- Take intersection of all word counters
	- Take the min of each key in the current word counter with the intersection word counter
```python
def commonChars(self, words: List[str]) -> List[str]:
        common_freq = Counter(words[0])
        res = []
        for i in range(1, len(words)):
            w_freq = Counter(words[i])
            for ch in common_freq:
                common_freq[ch] = min(common_freq[ch], w_freq[ch])
        
        for ch in common_freq:
            res.extend(ch*common_freq[ch])
        return res
```
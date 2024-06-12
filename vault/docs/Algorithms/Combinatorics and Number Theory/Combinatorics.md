---
---
# Combinatorics
- [x] https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/description/
- There are n monkeys at pos i in an array. 
- Each monkey must move once
- If they move in opposite directions, a collision happens.
- Return the number of collisions
- Is it easier to count the number of collisions or no collisions?
- No collisions = 2 for any n, because monkeys can all move cw or ccw
- Situations with collisions = $2^n - 2$

- [x] https://leetcode.com/problems/unique-paths/solutions/504514/unique-paths/
- [ ] In other words, we're asked to compute in how many ways one could choose p elements from p+k elements. In mathematics, that's called [binomial coefficients](https://en.wikipedia.org/wiki/Binomial_coefficient)
- [ ] The problem is a classical combinatorial problem: there are h+v moves to do from start to finish, h=m−1 horizontal moves, and v=n−1 vertical ones. One could choose when to move to the right, i.e. to define h horizontal moves, and that will fix vertical ones. Or, one could choose when to move down, i.e. to define v vertical moves, and that will fix horizontal ones.


![[Pasted image 20230203202802.png]]

- [ ] https://leetcodethehardway.com/tutorials/math/combinatorics




## DP
- Useful for aggregating multiple combinations/permutations

### Count number of answers 'with some conditions' that end in 'X'
https://leetcode.com/problems/student-attendance-record-ii/solutions/101639/pure-math-and-easy-to-understand-python-o-n-solution/

### DFS with States
https://leetcode.com/problems/student-attendance-record-ii/description/


### Count in Valid Intervals
https://leetcode.com/problems/plates-between-candles/description/



## Counting

### Sum Vowels of All Substrings
https://leetcode.com/problems/vowels-of-all-substrings/
- For a vowel at position i, how many substrings can be made with it? 
	- Group 1: There are i letters before it
	- Group 2: n-i letters after it
	- Append the ith vowel to one of the groups

```python
def countVowels(self, word: str) -> int:
        total = 0
        vowels = set('aeiou')
        for i,c in enumerate(word):
            if c in vowels:
               total += (i+1)*(len(word)-i)
        return total
```

### Sum Distinct Score of All Substrings
From that problem, we use the fact that each character appears in (i + 1) * (n - i) substrings. However, it does not contribute to the appeal of substrings on the left that already include that character. 
- Store indices of previous occurrences of the current character
```python
def appealSum(self, s: str) -> int:
        prev = defaultdict(lambda: -1)
        res = 0
        n = len(s)
        for i,ch in enumerate(s):
            res += (i-prev[ch]) * (n-i)
            prev[ch] = i
        return res

```
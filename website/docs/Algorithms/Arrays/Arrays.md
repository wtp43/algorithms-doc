---
---
Number of items in an array = j-i+1

# Arrays 

[LC-14. Longest Common Prefix](</docs/Some Leetcode Questions/LC-14. Longest Common Prefix.md>)- Find the longest common prefix that exists among all strings
- Update the common prefix after checking all strings in each loop

[LC-392. Is Subsequence](</docs/Some Leetcode Questions/LC-392. Is Subsequence.md>)	- two pointers 
	- returns true if the pointer corresponding to the subsequence is equal to n after all iterations

- [ ] https://leetcode.com/problems/unique-email-addresses/



## Max Sum of Pairs Minus Distance
- O(n): The best pair to choose with the current element is defined as (score - distance away from it)
https://leetcode.com/problems/best-sightseeing-pair/
```python
def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best = 0
        max_score = 0
        for x in values:
            max_score = max(max_score, best+x)
            # subtract 1 since we are moving further from the point
            best = max(best, x)-1
        return max_score
```


## Circular Array
https://leetcode.com/problems/maximize-greatness-of-an-array/submissions/1271130762/
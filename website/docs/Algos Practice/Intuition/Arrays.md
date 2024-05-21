---
---
Number of items in an array = j-i+1

# Arrays 

- [x] [[LC-128. Longest Consecutive Sequence]] T: O(n)
- For an unsorted array 3,100,200,2,1,4, the longest consecutive subsequence is 1234
- The start of the sequence cannot have a number to its left
- We do not have to iterate duplicates: for n in num_set
- Store every number in the sequence in a set.
- If he number to the left of the current number doesn't exist, we can try to build a subsequence
- Another possible solution is using union_find

[LC-14. Longest Common Prefix](</docs/Algos Practice/Leetcode Questions/LC-14. Longest Common Prefix.md>)- Find the longest common prefix that exists among all strings
- Update the common prefix after checking all strings in each loop

[LC-392. Is Subsequence](</docs/Algos Practice/Leetcode Questions/LC-392. Is Subsequence.md>)	- two pointers 
	- returns true if the pointer corresponding to the subsequence is equal to n after all iterations

- [ ] https://leetcode.com/problems/unique-email-addresses/
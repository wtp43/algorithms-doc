---
---
# Two pointers

## Subsequences
- Useful for subsequences since order is important unlike subsets
### Largest Subsequence Prefix 
https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/?envType=daily-question&envId=2024-06-03

- [ ] TwoSum: 
Find two elements in an array that sum to the target
- Sort then two pointers
- Or, store the complement in hashset and iterate
- O(n)
- [ ] ThreeSum (Reduces to TwoSum): 
Find three elements in an array that sum to the target
- Sort then run TwoSum starting at i+1 for i in range(n)
- Again, hashset the complement
- O(n)

- [ ] [[LC-189. Rotate Array]]
- k = k mod n
- reverse the entire array
- reverse the first k (0->k-1)
- reverse the last k

- [x] Valid Palindrome 
- Works for both even and odd length palindromes: while i < j
- Check the first and last character, if they don't match it's not a palindrome

- [ ] [[LC-977. Squares of a Sorted Array]] 
- We have a list` [-10,-5,0,1,2,20]` and require a list of squares in sorted order
- Two pointers is very useful here because the list is sorted, and either we take from the front or the back of the list

- [ ] [[LC-1268. Search Suggestions System]]
- Keep a left and right pointer that have the prefix 

---
dg-publish: true
title:  "LC 5. Longest Palindromic Substring"
created: 2023-02-01
---


# Description

# Brute Force
# Intuition

>[!danger]+ Intuition

# Implementation
```python
def longestPalindrome(self, s):
        n = len(s)
        max_p = 1
        p_start = 0
        if not s:
            return ""
        # 2d array: we check if there is a palindrome
        # starting at i and ending at j
        state = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            state[i][i] = 1 
        # recurrence relation
        # state[i][j] = (state[i+1][j-1] and s[i] == s[j])
        
       # bottom up dp: 
       # we have to build the smaller palindromes first
       # i = start
       # since our recurrence relation requires [i+1][j-1] is computed
       # we must build i from right to left and j from left to right
        for i in reversed(range(n)):
            # stop at n-i because those are computed already
            for j in range(i+1, n):
                if j-i > 1:
                    state[i][j] = (s[i] == s[j]) and state[i+1][j-1]
                else:
                    state[i][j] = (s[i] == s[j])
                if state[i][j] and j-i+1 > max_p:
                    max_p = j-i+1
                    p_start = i
        return s[p_start:p_start + max_p]
```

>[!example]+ 


# Related

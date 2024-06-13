---
title:  "Subset Sum"
created: 2023-01-13
---
# Subset Sum (Dynamic Programming)
Given a set of positive integers and an integer `k`, check if there is any non-empty subset that sums to `k`.
Backtracking would take O($n * 2^n$)

Special case of 0-1 Knapsack Problem. 
At each step we can either:
1. Include the current item
2. Exclude the current item
Return true if we get a subset by including or excluding the current item.

**Recurrence Relation**
isSubsetSum(set, n, sum) = (isSubsetSum(set, n-1, sum) || isSubsetSum(set, n-1, sum-set`[n-1]))

**Base Cases:**
isSubsetSum(set, n, sum) = false, if sum > 0 and n == 0
isSubsetSum(set, n, sum) = true, if sum == 0

# Recursive Implementation
```python
def subsetSum(arr, n, sum):
    if (sum == 0):
        return True
    if (n == 0):
        return False
 
    if (arr[n - 1] > sum):
        return subsetSum(arr, n - 1, sum)
 
    return subsetSum(arr, n-1, sum) or subsetSum(arr, n-1, sum-arr[n-1])
```

## Time and Space Complexity
- Time Complexity : O($2^n$), where n is equal to number of array elements. The recursive solution takes the form of a binary tree where there are 2 possibilities for every array element and the maximum depth of the tree could be n. The time complexity is exponential, hence this approach is exhaustive and results in _Time Limit Exceeded (TLE)_.
    
- Space Complexity: O(N) This space will be used to store the recursion stack. We can’t have more than nnn recursive calls on the call stack at any time.

# Implementation
`T[i][sum]` where i is the subset up to index i
```python
def subsetSum(A, k):
    n = len(A)
    # `T[i][j]` stores true if subset with sum `j` can be attained
    # using items up to first `i` items
    dp = [[False for x in range(k + 1)] for y in range(n + 1)]
 
    # if the sum is zero
    for i in range(n + 1):
        dp[i][0] = True
 
    # do for i'th item
    for i in range(1, n + 1):
        # consider all sum from 1 to sum
        for j in range(1, k + 1):
            # don't include the i'th element if `j-A[i-1]` is negative
            if A[i - 1] > j:
                dp[i][j] = T[i - 1][j]
            else:
                # find the subset with sum `j` by excluding or including the i'th item
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
 
    # return maximum value
    return T[n][k]
```

## Optimizations

## Optimized Complexity

:::Time-Complexity[Time Complexity] 


:::

:::Space-Complexity[Space Complexity] 


:::



# Related

---
title:  "0 1 Knapsack"
created: 2023-02-01
---


# Description
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack that has a capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack. Each item can only be selected once, as we don’t have multiple quantities of any item.
# Brute Force
```python
def knapSack(W, wt, val, n):
 
    # Base Case
    if n == 0 or W == 0:
        return 0
 
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))

if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    print knapSack(W, weight, profit, n)
 
```
# Intuition
Greedy algorithm only works for fractional knapsack. DP needed for 0-1 knapsack
[LC-2008. Maximum Earnings From Taxi](</docs/Algos Practice/Leetcode Questions/LC-2008. Maximum Earnings From Taxi.md>)
>[!danger]+ Intuition

# Bottom-Up Implementation
`dp[i][c]` will represent the maximum knapsack profit for capacity ‘c’ calculated from the first ‘i’ items

Recurrence relation:
- `dp[i][c] = max (dp[i-1][c], profits[i] + dp[i-1][c-weights[i]])`
- We can either take or exclude the current item

```python
def solve_knapsack(profits, weights, capacity):
  # basic checks
  n = len(profits)
  if capacity <= 0 or n == 0 or len(weights) != n:
    return 0

  dp = [[0]*(c+1) for _ in range(n)]

  # if we have only one weight, we will take it if it is not more than the capacity
  for c in range(capacity+1):
    if weights[0] <= c:
      dp[0][c] = profits[0]

  # iterate through all items
  for i in range(1, n):
	# iterate capacity
    for c in range(1, capacity+1):
      profit1, profit2 = 0, 0
      # include the item, if it is not more than the capacity
      if weights[i] <= c:
        profit1 = profits[i] + dp[i - 1][c - weights[i]]
      # exclude the item
      profit2 = dp[i - 1][c]
      # take maximum
      dp[i][c] = max(profit1, profit2)

  # maximum profit will be at the bottom-right corner.
  return dp[n - 1][capacity]


def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
```

>[!example]+ 

# How to find the selected items?

As we know that the final profit is at the bottom-right corner; therefore, we will start from there to find the items that will be going in the knapsack.

As you remember, at every step, we had two options: include an item or skip it. If we skip an item, then we take the profit from the remaining items (i.e., from the cell right above it); if we include the item, then we jump to the remaining profit to find more items.

Let’s understand this from the above example:

![widget](https://www.educative.io/api/collection/5668639101419520/5633779737559040/page/5666387129270272/image/5696910388101120?page_type=collection_lesson)

1.  ‘22’ did not come from the top cell (which is 17); hence we must include the item at index ‘3’ (which is the item ‘D’).
2.  Subtract the profit of item ‘D’ from ‘22’ to get the remaining profit ‘6’. We then jump to profit ‘6’ on the same row.
3.  ‘6’ came from the top cell, so we jump to row ‘2’.
4.  Again, ‘6’ came from the top cell, so we jump to row ‘1’.
5.  ‘6’ is different than the top cell, so we must include this item (which is item ‘B’).
6.  Subtract the profit of ‘B’ from ‘6’ to get the profit ‘0’. We then jump to profit ‘0’ on the same row. As soon as we hit zero remaining profit, we can finish our item search.
7.  So items going into the knapsack are {B, D}.


> [!important]+ Why this works
> If we included the current item i, then our weight cannot be equal to `dp[i-1][capacity]`.
> Otherwise, we excluded the current item and its weight is equal to `dp[i-1][capacity]`. 

```python
def print_selected_elements(dp, weights, profits, capacity):
  print("Selected weights are: ", end='')
  n = len(weights)
  totalProfit = dp[n-1][capacity]
  for i in range(n-1, 0, -1):
    if totalProfit != dp[i - 1][capacity]:
      print(str(weights[i]) + " ", end='')
      capacity -= weights[i]
      totalProfit -= profits[i]

  if totalProfit != 0:
    print(str(weights[0]) + " ", end='')
  print()
```

# Memoization

## Two rows (alternating)

Current row = i%2
Prev row = (i-1)%2
Last row = (n-1)%2

```python
def solve_knapsack(profits, weights, capacity):
  # basic checks
  n = len(profits)
  if capacity <= 0 or n == 0 or len(weights) != n:
    return 0

  dp = [[0 for x in range(capacity+1)] for y in range(2)]

  # if we have only one weight, we will take it if it is not more than the capacity
  for c in range(0, capacity+1):
    if weights[0] <= c:
      dp[0][c] = dp[1][c] = profits[0]

  # process all sub-arrays for all the capacities
  for i in range(1, n):
    for c in range(1, capacity+1):
      profit1, profit2 = 0, 0
      # include the item, if it is not more than the capacity
      if weights[i] <= c:
        profit1 = profits[i] + dp[(i - 1) % 2][c - weights[i]]
      # exclude the item
      profit2 = dp[(i - 1) % 2][c]
      # take maximum
      dp[i % 2][c] = max(profit1, profit2)

  return dp[(n - 1) % 2][capacity]
```

return `dp[(n-1)%2][capacity]`
- Consider the case when we only need 1 row. Then the answer is stored in row 0. 
- When there are 2 rows, then the answer is stored in row 1. 
- Thus, (n-1)%2

## Using a single row
- We have to iterate backwards inside the inner loop 

# Sorting weights does not optimize
- We need to check all subsets or we may stop prematurely without testing the pair such as (min, max). 

# Related
https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RM1BDv71V60


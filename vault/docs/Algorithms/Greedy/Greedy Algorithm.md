---
title:  "Greedy Algorithm"
created: 2023-01-06
---
# Greedy Algorithm
We want to take the biggest amount at every step. Track this to help solve the problem.




## Recognizing When Greedy Fails

> [!tip] Intuition
> Try to reducing to a common DP problem to see if Greedy will work.

- Coin Problem/Matching -> DP/Backtracking: You can't always match the largest x to the largest y
	- Ex: `x = [a,a,a,a,b,b,b], y = [3,2,2]`. The goal is to take `y[i]` quantities of identical objects in x 
	- If we sort both x and y, then we would match 3 to `a` but then we would be left with `[a,b,b,b]` instead of `[a,a,a,a]`

## Examples

- [ ] Fractional Knapsack
	- [ ] https://leetcode.com/problems/maximum-price-to-fill-a-bag/solutions/3103917/python-exchange-argument/?orderBy=most_votes

- [ ] https://leetcode.com/problems/increasing-triplet-subsequence/description/
- [ ] https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/
	- How do we keep track of the balloon with the greatest time?
		- Greedily keep track of the balloon with greatest removal time
		- Since we need two consecutive balloons of the same color for the removal to trigger, we won't have to worry about adding the largest removal time.
- [ ] Knapsack problem


## When Greedy Works
- If you want an algorithm that employs a greedy method, you should show the problem satisfies the greedy choice property (every locally optimal choice implies a globally optimal choice).


### Minimum Initial Energy
https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
- the variable to minimize is (minimum cost required - actual cost)
-  why? we want to start with the highest minimum cost with the lowest actual cost. 
-  this results in the next step being able to handle a higher minimum cost
-  sort key is `x[1]-x[0]` but we want it descending hence the reversed polarity

```python
def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: x[0]-x[1])
        ans = prev_saved = 0
        for cost, mmin in tasks:
            if prev_saved < mmin:
                ans += mmin - prev_saved
                prev_saved = mmin - cost
            else: 
                prev_saved -= cost
        return ans
```
# Related

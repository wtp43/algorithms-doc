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
- Minimum moves to spread stones over grid
	- BFS will not work since the least moves to allocate 1 stone is not necessarily the least moves to allocate all stones
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
### Examples of Valid Greedy Choice Properties
- Max profit: Choosing 1 element over another will result in a net difference (greedily take the largest net difference)
	- Key: Maximize expected value (Profit gained - opportunity cost of skipping )
- Max Event Scheduling: Sort by ending times, greedily take the next possible earliest ending interval
	- Key: choosing the earliest ending time will always leave more time for the next event (even if it started later in the series, a short job) 
	- https://stackoverflow.com/questions/32394987/greedy-algorithm-scheduling
## Max Profit

## [Max Profit With at Most K types from Arr1](https://leetcode.com/problems/mice-and-cheese/)
- `profit = reward1[i] - reward2[i]`, insert additive inverse into max heap

```python
def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diff = [(reward2[i] - reward1[i], i) for i in range(len(reward1))]
        diff.sort()
        res = 0
        for i in range(len(reward1)):
            if i < k:
                res += reward1[diff[i][1]]
            else:
                res += reward2[diff[i][1]]
        return res
```
### [Max Profit from Sequential Projects with Minimum Capital Requirement](https://leetcode.com/problems/ipo/description)
- Greedy: Take the highest profit project with the lowest required capital
- Use max heap of profits to manage which projects are available to take 
```python
def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # we want to start with projects with the lowest capital but highest profits
        # so we push all projects with requirement <= current money onto a maxheap
        projects = list(zip(capital, profits))
        projects.sort()
        n = len(profits)
        pq = []
        i = 0
        for j in range(k):
            while i < n and projects[i][0] <= w:
                heappush(pq, -projects[i][1])
                i += 1
            if not pq:
                break
            w += -heappop(pq)
        return w
```

### [Minimum Initial Energy](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/)
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
## Greedy Scheduling

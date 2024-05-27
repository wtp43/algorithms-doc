
## 

## Count Elements With Strictly Smaller and Greater Elements
- Get min and max
- x is valid if min < x < max
```python
def countElements(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        return sum(1 for x in nums if mn < x < mx)
```

## Count of Matches in Tournament 
- If the current number of teams is **even**, each team gets paired with another team. A total of `n / 2` matches are played, and `n / 2` teams advance to the next round.
- If the current number of teams is **odd**, one team randomly advances in the tournament, and the rest gets paired. A total of `(n - 1) / 2` matches are played, and `(n - 1) / 2 + 1` teams advance to the next round.
 - Notice that the losing team gets eliminated
 - Since there are n-1 teams that get eliminated, the # of matches played will always be n-1

## Valid Mountain Array
- A valid mountain array must be strictly increasing before the peak and strictly decreasing after the peak 
- Instead of saving a state to indicate if we are before or after the peak
- First, walk up to find the peak. Make sure the peak isn't the first or last element
- Walk down the hill, if we don't reach the end of the array, we have encountered another peak

## Count Odd Numbers in an Interval Range
- If range (high-low+1) is even, the number of even and odd numbers are equal
- If range is odd, we can add the number of odd numbers in the range(high-low), which is essentially raising low by one, then add one if low is odd.


## Count Number of Substrings with Only 1's
- Keep length of current valid substring
- Increment total result by the length of the current valid substring every loop
```python
def numSub(self, s: str) -> int:
        res = 0
        cur = 0
        for i in range(len(s)):
            if s[i] == '0':
                cur = 0
            else:
                cur += 1
            res += cur
        return res       
```


## Greedy
https://leetcode.com/problems/minimum-processing-time/description/
You have a certain number of processors, each having 4 cores. The number of tasks to be executed is four times the number of processors. Each task must be assigned to a unique core, and each core can only be used once.

You are given an array `processorTime` representing the time each processor becomes available and an array `tasks` representing how long each task takes to complete. Return the _minimum_ time needed to complete all tasks.
- Sort processors and tasks
- Match earliest processor with longest task

## Hashmap
https://leetcode.com/problems/count-special-quadruplets/description/

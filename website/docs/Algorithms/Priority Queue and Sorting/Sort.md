---
---
# Sort
- [ ] https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
- [x] Count/Bucket/Radix Sorts
- [x] Quick Sort
- [ ] Cyclic sort
	- [ ] https://emre.me/coding-patterns/cyclic-sort/
	- [ ] https://leetcode.com/discuss/study-guide/1902662/cyclic-sort-very-important-and-less-known-pattern
- [x] Merge Sort

- [ ] [[2099. Find Subsequence of Length K With the Largest Sum]]
- Find K largest numbers (quickselect): O(N) but worst case O(N^2)
- Sort by (nums[i], i) then sort again by the index i and return the largest k elements: O(NlogN)
- Keep a heap of the largest k items (nums[i], i). If cur num is smaller than the top of the heap, continue. If it is bigger, pop the top of the heap and insert the cur num: O(NlogK)

[LC-853. Car Fleet](</docs/Some Leetcode Questions/LC-853. Car Fleet.md>)- Finding intersections
- Sort by starting position and traverse backwards
	- We want to traverse backwards because the last car starts in a fleet of its own.
	- It gives us more information than the first car (we don't know how fast this fleet will end up going because we don't know when the cars in front will stop merging)
- Find the total time that the current car will take to get to the end: time_to_dest = (target-pos)/speed
- If time it takes to get to the end < max_time: we have a new fleet
- If time it takes to get to the end < max_time: the car is going faster and must join the fleet in front of it

- [ ] [[LC-953. Verifying an Alien Dictionary]]
	- sort words based on new ordering
	- Store an order_map
	- Compare all adjacent pairs
		- not sorted if: `j >= words[i][j+1]` or 
			- (`words[i][j] != words[i+1][j] and order_map[words[i][j]] > order_map[words[i + 1][j]])

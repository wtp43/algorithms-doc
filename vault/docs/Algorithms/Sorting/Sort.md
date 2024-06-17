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

- [ ] [[LC-853. Car Fleet]]
- Finding intersections
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


## Why Order Matters
- Greedy: we want to match the largest possible element to minimize differences

### [Put Boxes Into the Warehouse II](https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/)
> Boxes can be inserted in any order and from the left or right. Boxes are blocked if there is some room in the warehouse that is less than the height of the box
![](https://assets.leetcode.com/uploads/2020/08/30/22.png)

![](https://assets.leetcode.com/uploads/2020/08/30/22-1.png)

- By sorting, we guarantee that the tallest possible box is matched with the warehouse. The actual ordering will be different as subsequent warehouses may have lower heights.
- Since all taller boxes than the current warehouse are unable to move past, they won't be considered again
- Try to match either the left or right warehouse
```python
def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        res = 0
        box_i = len(boxes)-1
        i = 0
        j = len(warehouse)-1

        while i <= j and box_i >= 0:
            if boxes[box_i] <= warehouse[i]:
                res += 1
                i += 1
            elif boxes[box_i] <= warehouse[j]:
                res += 1
                j -= 1
            box_i -= 1
        return res

```
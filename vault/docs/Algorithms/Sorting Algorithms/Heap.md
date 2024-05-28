---
---
Max heaps
To make a max heap, push -x for x in array onto a min heap.

# Heaps
- [ ] [[LC-23. Merge k Sorted Lists]]
- Put the head of each linked list on a heap
- Extend the resulting linked list
- If the extended tail has a next node, put it back on the heap

- [ ] [[LC-1851. Minimum Interval to Include Each Query]]
- Find the smallest interval that can include each query (array of nums)
- Sort queries and intervals
- Put all intervals ``[l,r]`` that include q onto the heap with key ``[l-r+1, r]``
- Pop all intervals where `r` < q
- Store results in dictionary because we sorted our input 

- [ ] https://leetcode.com/problems/the-skyline-problem/description/

- [ ] https://leetcode.com/problems/task-scheduler/description/

- [ ] https://leetcode.com/problems/trapping-rain-water-ii/description/
- [ ] https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/

# Advanced Heaps

[[LC-2386. Find the K-Sum of an Array]]
- Find the k-th largest array where nums contains positive and negative numbers
- Maxheap (minheap with -nums)
- Keep a sorted list of abs(nums) in increasing order
- The next biggest sum sum can either be:
	- Adding the current number and subtracting the previous number
	- Not reverting the subtraction of the previous number and continuing to substract the current number
- Push the next biggest sum onto the heap
- O(NlogN + klogk) where NlogN is to sort all N numbers, and klogk is to maintain the heap since we push at most 2k sums to the heap.

```python
def kSum(self, nums: List[int], k: int) -> int:
        maxSum = sum([max(0, num) for num in nums])
        absNums = sorted([abs(num) for num in nums])
        maxHeap = [(-maxSum + absNums[0], 0)]
        nextSum = -maxSum
        for _ in range(k-1):
            nextSum, i = heappop(maxHeap)
            if i + 1 < len(absNums):
                heappush(maxHeap, (nextSum - absNums[i] + absNums[i + 1], i + 1))
                heappush(maxHeap, (nextSum + absNums[i + 1], i + 1))
        return -nextSum
```
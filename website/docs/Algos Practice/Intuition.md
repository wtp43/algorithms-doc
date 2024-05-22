---
---
Here, we are interested in building our intuition. In other words, our ability to reduce a hard problem to a simpler one. 


# Arrays 

[[LC-128. Longest Consecutive Sequence]] T: O(n)
- For an unsorted array 3,100,200,2,1,4, the longest consecutive subsequence is 1234
- The start of the sequence cannot have a number to its left
- We do not have to iterate duplicates: for n in num_set
- Store every number in the sequence in a set.
- If he number to the left of the current number doesn't exist, we can try to build a subsequence
- Another possible solution is using union_find

[LC-14. Longest Common Prefix](</docs/Algos Practice/Leetcode Questions/LC-14. Longest Common Prefix.md>)- Find the longest common prefix that exists among all strings
- Update the common prefix after checking all strings in each loop
https://leetcode.com/problems/is-subsequence/description/
https://leetcode.com/problems/unique-email-addresses/
https://leetcode.com/problems/distinct-subsequences/

# Backtracking

[LC-131. Palindrome Partitioning](</docs/Algos Practice/Leetcode Questions/LC-131. Palindrome Partitioning.md>)- We want to partition a string s such that every substring of the partition is a palindrome
- When backtracking, it's important to determine if we are at a valid step. Only if we are do we proceed to the next step (continue recursing).
https://leetcode.com/problems/palindromic-substrings/description/

https://leetcode.com/problems/robot-room-cleaner/solutions/265763/robot-room-cleaner/?orderBy=most_votes

knights tour

# Brainteasers

[LC-1007. Minimum Domino Rotations For Equal Row](</docs/Algos Practice/Leetcode Questions/LC-1007. Minimum Domino Rotations For Equal Row.md>)- We have to immediately recognize that it doesn't matter where we check but that every single domino must have at least one of the two numbers present.
- So if any domino doesn't have the top or bottom number of the first domino, no rotations are possible


# Binary Search
[LC-1752. Check if Array Is Sorted and Rotate](</docs/Algos Practice/Leetcode Questions/LC-1752. Check if Array Is Sorted and Rotated.md>)- Important to note that the first and last num are connected
- Check if the next number is bigger: This can only happen once if sorted and rotated
	- nums[i] > nums[(1+i)%n]


[LC-153. Find Minimum in Rotated Sorted Array](</docs/Algos Practice/Leetcode Questions/LC-153. Find Minimum in Rotated Sorted Array.md>)- Update the min every loop. The min will not always land on j or always on i
- `If nums[j] > nums[mid]: the min has to be on the left


[LC-33. Search in Rotated Sorted Array](</docs/Algos Practice/Leetcode Questions/LC-33. Search in Rotated Sorted Array.md>)
>[!danger]+ Intuition
>   enumerate possibilities
> 
1. `we are in the left portion ([6789] 123)
	    - `target > nums[mid]: i=mid+1
	    - ``nums[i] <= target < nums[mid] j=mid-1
	    - `target < nums[i]: i=mid+1
2. `we are in right portion (78 [123])
		- `target < num[mid]: j=mid-1
		- `nums[mid] < target <= nums[j]: i=mid+1
		- `target > nums[j]: j=mid-1

[[LC-74. Search a 2D Matrix]]

[[LC-981. Time Based Key-Value Store]]
- We want to store multiple values with different timestamps for the same key
- We notice that since time is strictly increasing, our list of values will in sorted order
- Create a dictionary of lists and binary search on the list
[[LC-34. Find First and Last Position of Element in Sorted Array]]
- Left and right bisect essentially move the same way when target != `nums[mid]
- The only difference is when the target == `nums[mid]
- Left bisect will set j = mid-1 and move left 
- Right bisect will set i = mid+1 and move right

[[LC-1268. Search Suggestions System]]
- Suggest at most 3 words based on the prefix
- Sort strings then bisect left on the prefix 

# Combinatorics
https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/description/
- There are n monkeys at pos i in an array. 
- Each monkey must move once
- If they move in opposite directions, a collision happens.
- Return the number of collisions
- Is it easier to count the number of collisions or no collisions?
- No collisions = 2 for any n, because monkeys can all move cw or ccw
- Situations with collisions = $2^n - 2$



# Dynamic Programming
https://leetcode.com/problems/minimum-cost-to-split-an-array/description/
https://leetcode.com/problems/minimum-cost-to-split-an-array/solutions/3083850/python3-dp/

https://leetcode.com/problems/concatenated-words/solutions/2822170/concatenated-words/?orderBy=most_votes
Why sliding window wouldn't work here:
- There is no window of k for our solution
	- The size of k will not encompass all the substrings that a word may contain
	- we need to do more comparisons
- Sorting does not allow us to find the answer in O(1)
	- we realize that we have to check more than just the word at the start of the window

# Data Structures (Advanced)
[LFU Cache](</docs/DS/LFU Cache.md>)https://leetcode.com/problems/lfu-cache/solutions/2815229/lfu-cache/
# Enumerate Options
https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/solutions/3083831/java-c-python-1-line-check-1/?orderBy=most_votes


# Graphs

## Union Find (Cycle detection)
Works for undirected graphs
[LC-684. Redundant Connection](</docs/Algos Practice/Leetcode Questions/LC-684. Redundant Connection.md>)- This is the case where the tree has no cycles and is an undirected graph. Then we just need to remove one of the two edges that make up the node with indegree 2.
- Use union find to detect if nodes u,v in the edge (u,v) have the same parent. If they do, this edge is redundant

[LC-685. Redundant Connection II](</docs/Algos Practice/Leetcode Questions/LC-685. Redundant Connection II.md>)-  A valid graph in this context is a single rooted tree (directed graph) with no cycles. This graph is given a single extra edge.
- An edge that is redundant if it is one of two edges that enter the same node or an edge in a cycle. In the case that both scenario happens, we need to remove the edge inside the cycle otherwise it only solves one of the two problems.
- Since we are not sure which edge to remove to ensure that the node has indegree of 1, we have to keep track both edges. We want to remove the edge that is part of a cycle if there exists one. 
- It will help to store the previous node of each node in a dictionary.
- Union find will help us detect the cycle

[LC-261. Graph Valid Tree](</docs/Algos Practice/Leetcode Questions/LC-261. Graph Valid Tree.md>)- A valid tree has 1 connected component with no cycles
- Reduces to redundant connection
- An extra check is required at the end to see if the edges have connected all the components

[LC-323. Number of Connected Components in an Undirected Graph](</docs/Algos Practice/Leetcode Questions/LC-323. Number of Connected Components in an Undirected Graph.md>)- Union find
- Reduce the number of connected components every time we take the union of nodes u and v


## DFS


Start DFS for every connected component. Make sure to mark connected components
When building out adjacency lists  for directed graphs, we need to make sure the directions are correct. In the case of course schedule, we want the courses to point to prerequisites because this tells us which prerequisites are needed.

In BFS, we need to do a check prior to adding the node to the queue. In DFS, it may not always be necessary to do a pre-check, we can check in the base case of the function call.

[LC-1971. Find if Path Exists in Graph](</docs/Algos Practice/Leetcode Questions/LC-1971. Find if Path Exists in Graph.md>)- Union find and connect all edges. 
	- Check if find(source) == find(destination) are the same. Don't check the parents because the path may not have been flattened yet.
- DFS
	- return True if cur_node == destination
	- For all neighbors of cur_node
		- if dfs(neighbor)
			- return True
	- return False



[LC-200. Number of Islands](</docs/Algos Practice/Leetcode Questions/LC-200. Number of Islands.md>)- '1' is marked as land while '0' is water
- Start DFS at every '1' while marking them as '0' to indicate they are visited
- Increment number of islands every time dfs is started at '1'

[[LC-695. Max Area of Island]]
- Start DFS at every '1' and mark them as visited
- Recursively sum up the area of the island by returning 1 + dfs(all dirs)


[LC-417. Pacific Atlantic Water Flow](</docs/Algos Practice/Leetcode Questions/LC-417. Pacific Atlantic Water Flow.md>)- Find all the squares that flow to and from the pacific/atlantic
The naive approach would be to BFS from each cell. It repeats computation because any result can only be applied to that cell. Start from the ocean(outer borders) and work backwards. The results here are used for multiple cells because every cell we visit must be connected to the ocean. 

[LC-994. Rotting Oranges](</docs/Algos Practice/Leetcode Questions/LC-994. Rotting Oranges.md>)- Since one fresh orange can be affected by multiple oranges, we want to find the shortest time in which it will be affected. 
- We need to modify our BFS to run in parallel. We can do this by keeping track of which iteration we are on using a delimiter in the queue and starting BFS at all rotten oranges. 
- Instead of a delimiter, we can also iterate the length of the current queue.

[LC-207. Course Schedule](</docs/Algos Practice/Leetcode Questions/LC-207. Course Schedule.md>)- Cycle detection but in a directed graph
- We can use topological sort which implements DFS
	- We have three states: unvisited, currently visiting, visited
	- A cycle is detected if we reach a node that we are currently visiting
- Append, the 
- Direction is important: Since this is a one to many relationship ``[course, prerequisite1], we need to build our edges directed in this way: graph[i].append(j)

[LC-286. Walls and Gates](</docs/Algos Practice/Leetcode Questions/LC-286. Walls and Gates.md>)- We want to find the distance from every empty cell to the nearest gate. 
- Instead of running DFS from every gate and taking the min (this results in extra computation), run BFS in parallel starting from each gate. 
- Thus we are guaranteed the shortest route. The distance to the cell is only updated if it is not inf and in the case it isn't, we know we have already visited it taking a shorter path.
- To run BFS in parallel, use a for loop to pop all items in the q at the current state with dist = i. After all these are popped increment dist
```python
while q:
	for _ in  range(len(q)):
		next = q.pop()
		cell[i][j] = dist
		seen.add((i,j))
		for x,y in dirs:
			row = i+x
			col = j+y
			if (row,col) in seen or (row and col out of bounds):
				continue
			q.append((row,col))
			seen.append((row,col))

	dist += 1
	
```

## BFS (Shortest path)
BFS is more useful than DFS in cases where we are interested in the shortest path.

[[LC-787. Cheapest Flights Within K Stops]]
Dijkstra wouldn't be the best solution here because we are limited to k steps.
We can run BFS: O(N + EK). In BFS: we have to pass the distance to the queue otherwise we may accidentally use the shortest distance ``(dist[city])`` that takes a different path because ``dist[city]`` may have been updated earlier by a different node.
This is also similar to Bellman Ford but relaxing only k+1 times: O((N+E)K) The N comes from swapping the temp and dist array after each round of relaxing all edges. If we do not store our previous result, we will accidentally use more than K steps.

## Shortest Path
https://leetcode.com/problems/network-delay-time/description/

# Greedy
https://leetcode.com/problems/maximum-price-to-fill-a-bag/solutions/3103917/python-exchange-argument/?orderBy=most_votes

# Hashing
https://leetcode.com/problems/strings-differ-by-one-character/solutions/801825/python-clean-set-string-hashing-solution-from-o-nm-2-to-o-nm/?orderBy=most_votes
Distinct islands

# Heap
To make a max heap, push -x for x in array onto a min heap.

https://leetcode.com/problems/task-scheduler/description/

# Advanced Heaps: IPQ, Fibonacci Heap
https://www.geeksforgeeks.org/fibonacci-heap-set-1-introduction/



# Intervals/Scheduling
https://leetcode.com/problems/remove-covered-intervals/
https://leetcode.com/problems/task-scheduler/description/

# Linked List

[LC-206. Reverse Linked List](</docs/Algos Practice/Leetcode Questions/LC-206. Reverse Linked List.md>)- The 3 components we need are prev, cur, and tmp. We need to store the next link because it is being updated.

[[LC-234. Palindrome Linked List]] 

- Fast slow pointer to find the middle of the linked list
- Reverse the 2nd half of the linked list

[[LC-138. Copy List with Random Pointer]]
- Make all the new nodes first and store them in a dictionary
- Traverse the original linked list and set the corresponding links using the dictionary on the new nodes.

```python
def copyRandomList(self, head: "Node") -> "Node":
        oldToCopy = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
```

# Maze  Solving Algorithms


# Knapsack 01 and Fractional Knapsack
https://www.geeksforgeeks.org/difference-between-0-1-knapsack-problem-and-fractional-knapsack-problem/?ref=rp

# K Problems
## Quick Select
[[LC-973. K Closest Points to Origin]]
https://leetcode.com/problems/k-closest-points-to-origin/solutions/1590679/k-closest-points-to-origin/?orderBy=most_votes
https://leetcode.com/problems/top-k-frequent-words/solutions/2516165/top-k-frequent-words/
# Sort
[[2099. Find Subsequence of Length K With the Largest Sum]]
- Find K largest numbers (quickselect): O(N) but worst case O(N^2)
- Sort by (nums[i], i) then sort again by the index i and return the largest k elements: O(NlogN)
- Keep a heap of the largest k items (nums[i], i). If cur num is smaller than the top of the heap, continue. If it is bigger, pop the top of the heap and insert the cur num: O(NlogK)

[LC-853. Car Fleet](</docs/Algos Practice/Leetcode Questions/LC-853. Car Fleet.md>)- Finding intersections
- Sort by starting position and traverse backwards
	- We want to traverse backwards because the last car starts in a fleet of its own.
	- It gives us more information than the first car (we don't know how fast this fleet will end up going because we don't know when the cars in front will stop merging)
- Find the total time that the current car will take to get to the end: time_to_dest = (target-pos)/speed
- If time it takes to get to the end < max_time: we have a new fleet
- If time it takes to get to the end < max_time: the car is going faster and must join the fleet in front of it

# Stack
Problems that require a stack are generally greedy.
Aside from scheduling which requires sorting, most of these problems take advantage of not requiring a sorted order. We input items onto a stack until we reach an item that invalidates previous entries. Pop all non-optimal items until you reach one that is optimal, then append the current item.

After every pop, it's important to update our results and if need be, push the updated results back onto the stack.
This is common when merging intervals (stock span, largest rectangle in histogram).

Always remember to clear non empty stack at the end of loops

## Useful tools we can make with stacks
- Monotonically inc/dec stacks
- Strictly inc/dec stacks
	- We build stacks in such a way that the top of the stack guarantees that we have the smallest/largest number
- Min/max stacks
	- Augmented stack that tells us the minimum/maximum in the history

[[LC-84. Largest Rectangle in Histogram]]
- Greedy algorithm:
	- We want to use as many bars as possible
	- We can use the entirety of the current bar if the previous bars are all higher
	- Popping criteria: we can only partially use the previous bars if the current bar's height is higher
	- We cannot extend a bar if the next bar is shorter. In this case, we calculate the maximum area using all the previous bars that are taller than the current bar. Pop  all previous bars while simultaneously calculating the area using the current height and the number of bars higher than it that have been popped.

[LC-735. Asteroid Collision](</docs/Algos Practice/Leetcode Questions/LC-735. Asteroid Collision.md>)- Asteroid collisions where the larger of the asteroid stays intact, negative moves left, positive moves right
- Store a stack of asteroids that we have already processed
- Compare the top of the stack with the current asteroid
	- Enumerate all possibilities
	- Crash is only possible if cur asteroid < 0 < stack[-1]
	- Then append the asteroid only if the last popped asteroid was not equal to it in size
		- Very useful to use while else, if we break then we don't go to the else

[LC-402. Remove K Digits](</docs/Algos Practice/Leetcode Questions/LC-402. Remove K Digits.md>)- Remove k digits to get the smallest number
[LC-84. Largest Rectangle in Histogra](</docs/Algos Practice/Leetcode Questions/LC-84. Largest Rectangle in Histogram.md>)- We want to pop everything before the current item if cur_item < stack[-1]
- Both these algorithms are greedy.
	- It's important to figure out the criteria of when to add and pop to the stack
	- In this question, we want to pop a number from the resulting number stack if the cur number is smaller than the prev
	- It's also important that we iterate list to right.
		- For instance A = 1axxx, B = 1bxxx. If a > b then A > B
- There is however 1 case that doesn't work, monotonically increasing, which we need to handle separately

![Pasted-image-20230124003324.png](</Algos-Practice/Leetcode-Questions/attachments/Pasted-image-20230124003324.png>)

[LC-901. Online Stock Span](</docs/Algos Practice/Leetcode Questions/LC-901. Online Stock Span.md>)
```python
class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        span = 1
        while self.s and price >= self.s[-1][0]:
            span += self.s.pop()[1]
            
        self.s.append((price,span))
        return span
```
- It's important to push the span back (update) after every pop. 

[LC-456. 132 Pattern](</docs/Algos Practice/Leetcode Questions/LC-456. 132 Pattern.md>)- Since we want i < j < k and nums[i] < nums[k] < nums[j], it would be useful to have the minimum nums[i] at each iteration. 
- Then we iterate the array backwards 
	- if nums[j] <= min_array[j]
		- continue, because we dont have a valid nums[i] to use
	- while our stack of nums[k] <= min_array[j]
		- stack.pop() until we have a valid nums[k]
		- because the solution we are searching for requires nums[k] < nums[j], we know that our stack is a in min stack otherwise we would have found a solution already
	- check if stack and stack[-1] < nums[j]. Then we have a valid k and i
	- Append the current j to the stack

[LC-394. Decode String](</docs/Algos Practice/Leetcode Questions/LC-394. Decode String.md>)- To convert a string '100' to integer: k = k * 10 + int(c)
	- Another way is to store the a num stack with delimiter [#,1,0,0,#]
- The hard part is dealing with nested strings
	- Every time we reach a ``'['``  , we need to push the current string back onto the stack
	- When we reach ``']'``, we need to process both the current string and the string on the top of the stack together

[[LC-1209. Remove All Adjacent Duplicates in String II]]
Bruteforce: O($n^2$/k)
- Time complexity: Think about what happens after k deletions? How long will the string be?: n-k. How many deletions can we do?: n/k. In the worst case, we do n/k deletions and we have to start from the beginning to see if new adjacent duplicates were created because of the deletion.
- We scan the string no more than n/k times
	iterate through the string:
-   If the current character is the same as the one before, increase the count.
    -   Otherwise, reset the count to `1`.
-   If the count equals `k`, erase last `k` characters.
- If the length of the string was changed, repeat starting from the first step.
What are some generic string properties?
- Index, consecutive frequency, character
Character and consecutive frequency will be useful here to help us rebuild the string
One property to note is that, it is not possible for multiple merges after one delete
- ie: bbb - bb - ccc - b, for k = 3
- This is because bbb would have already been deleted. Thus, we only have to look at the top of the stack after deleting

[LC-32. Longest Valid Parentheses](</docs/Algos Practice/Leetcode Questions/LC-32. Longest Valid Parentheses.md>)What is important? Where the last valid open bracket was.
Thus, we should store the index.
When we can update the longest valid parenthesis?
When we have popped an open bracket off the stack.
How do we know we've popped an open bracket?
We store the last invalid index before the next opening bracket at the start of the stack.
Length = j-i+1
This is because j and i are indices. (j-i) just gives us the difference.

[LC-85. Maximal Rectangle](</docs/Algos Practice/Leetcode Questions/LC-85. Maximal Rectangle.md>)![](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)
[LC-84. Largest Rectangle in Histogra](</docs/Algos Practice/Leetcode Questions/LC-84. Largest Rectangle in Histogram.md>)
To find all the rectangles, we have to look at every possible i,j. So the BTTC is O(NM).
To build our bars for the histogram, we can set the current row as the y axis and use DP. If the current cell is a 0, we cannot reuse the height form the previous rows, otherwise we can extend the bar.



# Sliding Window
In an array of size N, there are N - k + 1 windows.

General Template
```python
start = counter = 0
res = 0
for end in range(n):
	counter += nums[end]

	if start-end >= k-1:
		res = max(res, counter)
		counter -= nums[start]
		start += 1
```

Maximum Sum Subarray of Size K
- Keep track of where the current window starts and ends
- Build a window of size k
- Loop for all window_ends (for i in range(len(nums)))
- `counter += nums[i]
- When we have reached the last element of the window (k-1), 
	- Update maximum 
	- `counter -= nums[start]
	- start += 1

[LC-209. Minimum Size Subarray Su](</docs/Algos Practice/Leetcode Questions/LC-209. Minimum Size Subarray Sum.md>)- Find the smallest window where sum is at least target
- First find a window, then make it smaller while still satisfying the constraints.


[LC-239. Sliding Window Maximu](</docs/Algos Practice/Leetcode Questions/LC-239. Sliding Window Maximum.md>)- Find the maximum of all k sized windows
- Brute force: iterate all k sized windows. Time complexity: N-k+1 windows and k elements in each window = O(NK)
- Keep a monotonic decreasing stack of elements
	- For every new element, pop all elements smaller than it in the deque
	- Add the new element
	- If the left index is greater than q[0] (the greatest element), pop q[0]
- What we are doing here is reducing a heap
	- We don't need a full heap because we are only interested in the biggest item in a window of size k
	- This is possible because we don't need all the items 

[LC-340. Longest Substring with At Most K Distinct Characters](</docs/Algos Practice/Leetcode Questions/LC-340. Longest Substring with At Most K Distinct Characters.md>)- Keep track of all frequencies of characters. 
- When you reach a window containing k+1 characters, move start up until len(frequency) = k.  
- O(n)

[LC-904. Fruit Into Baskets](</docs/Algos Practice/Leetcode Questions/LC-904. Fruit Into Baskets.md>)- Window size can only have 2 distinct characters instead of k
- Brute force:
	- O(n^3)
	- Loop on the left index, the right index, and the current index in between left and right
- Keep track of frequencies in the current sliding window. The moment we exceed the frequencies, move the start of the window up and decrement for each of the elements until we reach the valid number of frequencies again.
- Update the max_count during every iteration (not just until we reach k+1 sized windows)
- O(n)

[LC-424. Longest Repeating Character Replacement](</docs/Algos Practice/Leetcode Questions/LC-424. Longest Repeating Character Replacement.md>)How is the biggest window made?
>It is the window containing the most number of repeated character (character with the highest frequency) + k other letters


[LC-3. Longest Substring Without Repeating Characters](</docs/Algos Practice/Leetcode Questions/LC-3. Longest Substring Without Repeating Characters.md>)- Keep set of seen letters
- If current letter has already appeared, move the start of the window up while simultaneously deleting the letter at index: start

[LC-567. Permutation in String](</docs/Algos Practice/Leetcode Questions/LC-567. Permutation in String.md>)- Check if s2 contains a permutation of s1
-  self.dictEquals(d1,d2) while moving up the sliding window and updating d2 (decrement the frequency of the previous window start, increment the current char)
- If we use Counter(), we can compare them directly (d1 == d2) instead of rewriting a dictionary comparison function

[LC-438. Find All Anagrams in a String](</docs/Algos Practice/Leetcode Questions/LC-438. Find All Anagrams in a String.md>)- Similar to permutation in string
- Keep counters of all characters
- Increment current letter, move window up, decrement the character at the previous start

[LC-76. Minimum Window Substring](</docs/Algos Practice/Leetcode Questions/LC-76. Minimum Window Substring.md>)- Find the smallest window that contains all letters of t in s including duplicates. (This can be reduced to permutation in string)

For minimum window strategies:
- Find a valid window first
	- Iteratively make the window smaller by moving up the start index
	- Check if the current smaller window still satisfies the constraints and update the minimum window

[LC-713. Subarray Product Less Than K](</docs/Algos Practice/Leetcode Questions/LC-713. Subarray Product Less Than K.md>)- We notice there are only positive numbers.
- First determine what an invalid state for the window would be
- For each new window, we can make j-i+1 windows that end on the element j
	- The only new windows we can add are only the ones that include the new element j.
	- Previous windows not including j would have been accounted for

[[LC-1493. Longest Subarray of 1's After Deleting One Element]]
- Given a binary array `nums`, you should delete one element from it.
- Return _the size of the longest non-empty subarray containing only_ `1`_'s in the resulting array_. Return `0` if there is no such subarray.

[[LC-1004. Max Consecutive Ones III]]
- Problem solving: 
	- What is the input? Does the input have negatives?
- We can use a non-shrinkable sliding window (we are finding maximum window not subset of windows)
- First figure out invalid state:
	- invalid: zeros > k

[[LC-581. Shortest Unsorted Continuous Subarray]]
- Approach 1: Finding the first and last out of place nums
	- create a sorted copy of nums
	- Find the first and last index where they differ to get the unsorted portion
	- In fact, we don't need to sort the entire array. 
- Approach 2: 

# String Matching
Rabin Karp
https://leetcode.com/problems/strings-differ-by-one-character/solutions/802871/rabin-karp-o-nm/
# Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/description/
https://leetcode.com/discuss/interview-question/1279773/google-interview-question-array-subset-sum-equals-k
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

# Two pointers
## TwoSum: 
Find two elements in an array that sum to the target
- Sort then two pointers
- Or, store the complement in hashset and iterate
- O(n)
## ThreeSum (Reduces to TwoSum): 
Find three elements in an array that sum to the target
- Sort then run TwoSum starting at i+1 for i in range(n)
- Again, hashset the complement
- O(n)

[LC-189. Rotate Array](</docs/Algos Practice/Leetcode Questions/LC-189. Rotate Array.md>)- k = k mod n
- reverse the entire array
- reverse the first k (0->k-1)
- reverse the last k

Valid Palindrome
- Works for both even and odd length palindromes: while i < j
- Check the first and last character, if they don't match it's not a palindrome

[[LC-977. Squares of a Sorted Array]]
- We have a list` [-10,-5,0,1,2,20]` and require a list of squares in sorted order
- Two pointers is very useful here because the list is sorted, and either we take from the front or the back of the list

[[LC-1268. Search Suggestions System]]
- Keep a left and right pointer that have the prefix 

# Tree

Zero based
- parent = (i-1)//2
- child1: 2i+1
- child2: 2i+2
one-based
- parent = i//2
- child1 = 2i
- child2 = 2i +1

# Trie
[[LC-1268. Search Suggestions System]]
- Preorder traversal of a trie
	- Do not sort. Loop the alphabet instead


# Fast and Slow Pointers

[LC-876. Middle of the Linked List](</docs/Algos Practice/Leetcode Questions/LC-876. Middle of the Linked List.md>)- Use two pointers that both start at the head
- While p2 and p2.next, move p1 up by one while p2 up by 2
- The middle will be at p1

# Mathematics

To get the number of items in a range ``[l,r]``: 
- size = r-l+1

[[LC-367. Valid Perfect Square]]
- The sqrt of a num is always <= num/2


# Questions for the Interviewer (Assumptions)

## Graphs
- Can we assume there are no cycles?
	- Not needed if structure is a tree
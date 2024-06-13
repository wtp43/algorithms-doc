---
created:
---
 # All Topics

After reviewing, update applications for each algo

# Data Structures
- [ ] AVL Trees
- [ ] Binary Search Tree
- [ ] Bloom Filter
- [ ] Circular Queue
	- [ ] Circular Deque
- [ ] Connected Components
- [x] Heap
	- [ ] Indexed Priority Heap
- [ ] D-ary Heap
	- [ ] Indexed D-ary Heap *
- [ ] Fibonacci Heap *
- [ ] Graph Structures
- [ ] Hash map
- [ ] LFU Cache
- [ ] Linked List
- [ ] Matrix Traversals
- [ ] Maximum Frequency Stack
- [ ] Minimum Queue
- [ ] Monotonic Queue
- [ ] Sparse Table  *
- [ ] Stacks
[LC-84. Largest Rectangle in Histogra](</docs/Some Leetcode Questions/LC-84. Largest Rectangle in Histogram.md>)[LC-735. Asteroid Collision](</docs/Some Leetcode Questions/LC-735. Asteroid Collision.md>)[LC-402. Remove K Digits](</docs/Some Leetcode Questions/LC-402. Remove K Digits.md>)[LC-456. 132 Pattern](</docs/Some Leetcode Questions/LC-456. 132 Pattern.md>)[LC-901. Online Stock Span](</docs/Some Leetcode Questions/LC-901. Online Stock Span.md>)[LC-394. Decode String](</docs/Some Leetcode Questions/LC-394. Decode String.md>)	- [ ] [[LC-1209. Remove All Adjacent Duplicates in String II]]
[LC-32. Longest Valid Parentheses](</docs/Some Leetcode Questions/LC-32. Longest Valid Parentheses.md>)[LC-85. Maximal Rectangle](</docs/Some Leetcode Questions/LC-85. Maximal Rectangle.md>)[LC-739. Daily Temperatures](</docs/Some Leetcode Questions/LC-739. Daily Temperatures.md>)- [ ] Trees (Todo - Incomplete notes)
- [x] Trie
- [x] Union Find

# Algos
- Strongly Connected Components
	- Kosaraju's Algorithm

## Graph

- [ ] BFS
	- [ ] Multi-source BFS: iterating queue in chunks/layers using length of queue at the current step
- [ ] DFS
	- [ ] Connected components
- [ ] IDS
- [ ] Union-find
	- [ ] Connected components
- [ ] Backtracking
	- [ ] N-queens

- [ ] Topological Sort 
	- [ ] Cycle Detection

### Review 
## Arrays
[Kadane's Algorith](</docs/Algorithms/Arrays/Kadane's Algorithm.md>)## Binary Search
- [x] Bisect-right
- [x] Bisect-left
- [x] Binary search

## Sliding Window
[Sliding Window](</docs/Algorithms/Arrays/Sliding Window.md>)	- Shrinkable/non-shrinkable approach

## Sorts
[Quick Sort](</docs/Algorithms/Priority Queue and Sorting/Quick Sort.md>)
## Data Structures
[Sorting and Heaps](</docs/Algorithms/Priority Queue and Sorting/Sorting and Heaps.md>)### Review
[LC-1752. Check if Array Is Sorted and Rotate](</docs/Some Leetcode Questions/LC-1752. Check if Array Is Sorted and Rotated.md>)	- Compare all neighbour elements `(a,b)` in `A`,  
		the case of `a > b` can happen at most once.
		
		Note that the first element and the last element are also connected.
		
		If all `a <= b`, `A` is already sorted.  
		If all `a <= b` but only one `a > b`,  
		we can rotate and make `b` the first element.  
		Else, return `false`.

[LC-153. Find Minimum in Rotated Sorted Array](</docs/Some Leetcode Questions/LC-153. Find Minimum in Rotated Sorted Array.md>)
# Intuition
- Smallest difference (array, bst nodes)
	- Sort then 1 pass: nlogn
	- in order traversal (BST)
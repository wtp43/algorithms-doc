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
	- [ ] [[LC-84. Largest Rectangle in Histogram]]
	- [ ] [[LC-735. Asteroid Collision]]
	- [ ] [[LC-402. Remove K Digits]]
	- [ ] [[LC-456. 132 Pattern]]
	- [ ] [[LC-901. Online Stock Span]]
	- [ ] [[LC-394. Decode String]]
	- [ ] [[LC-1209. Remove All Adjacent Duplicates in String II]]
	- [ ] [[LC-32. Longest Valid Parentheses]]
	- [ ] [[LC-85. Maximal Rectangle]]
	- [ ] [[LC-739. Daily Temperatures]]
- [ ] Trees (Todo - Incomplete notes)
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
- [ ] [[Kadane's Algorithm]]
## Binary Search
- [x] Bisect-right
- [x] Bisect-left
- [x] Binary search

## Sliding Window
- Constructing windows [[Sliding Window]]
	- Shrinkable/non-shrinkable approach

## Sorts
 - [[Quick Sort]]

## Data Structures
 - [[Heaps]]
### Review
- [[LC-1752. Check if Array Is Sorted and Rotated]]  
	- Compare all neighbour elements `(a,b)` in `A`,  
		the case of `a > b` can happen at most once.
		
		Note that the first element and the last element are also connected.
		
		If all `a <= b`, `A` is already sorted.  
		If all `a <= b` but only one `a > b`,  
		we can rotate and make `b` the first element.  
		Else, return `false`.

- [[LC-153. Find Minimum in Rotated Sorted Array]]

# Intuition
- Smallest difference (array, bst nodes)
	- Sort then 1 pass: nlogn
	- in order traversal (BST)
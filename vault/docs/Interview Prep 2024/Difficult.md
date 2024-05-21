---
created:
---
---
>[!summary]- Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```
# Arrays
## Kadane's Algorithm
- Keep expanding subarray until sum is  < 0, then restart 
- It's not possible for the start of a positive sum to be a negative # greater than the current sum
### Maximum Sum Circular Subarray
- Maximum subarray is either 
	- max subarray that doesn't wrap
	- if it wraps, then it is the total - min subarray in the middle
- Special case: take the maximum subarray if the minimum subarray is the entire array (all neg #'s)
```python
def maxSubarraySumCircular(self, nums: List[int]) -> int:
	max_subarray = nums[0] 
	min_subarray = nums[0] 
	cur_min = 0 
	cur_max = 0 
	total_sum = 0
	for x in nums:
	  # kadane's 
		cur_max = max(cur_max, 0) + x
		max_subarray = max(cur_max, max_subarray)

		# Min Kadane's
		cur_min = min(cur_min, 0) + x
		min_subarray = min(cur_min, min_subarray)
	  
		total_sum += x
	if total_sum == min_subarray:
		return max_subarray
	return max(max_subarray, total_sum - min_subarray
```
https://leetcode.com/problems/house-robber-iii/description/jj

# Binary Trees

## House Robber 3 (can't rob two directly linked nodes in a BT) 
- Similar to backtrack/dp, at each node, you can choose to rob it or not, creating diverging paths
- Bottom up recursion so we can take the max
```python
def rob(self, root: TreeNode) -> int:
	def dfs(node):
		# return [rob this node, not rob this node]
		if not node:
			return (0, 0)
		left = dfs(node.left)
		right = dfs(node.right)
		# if we rob this node, we cannot rob its children
		rob = node.val + left[1] + right[1]
		# else we could choose to either rob its children or not
		not_rob = max(left) + max(right)
		return [rob, not_rob]

	return max(dfs(root))
```
https://leetcode.com/problems/house-robber-iii/description/

## BST delete
- Predecessor: 1 left then loop right 
- Successor: 1 right then loop left 
- Bad solution: recursion and swap values
	- Recursively return the child node
	- If key is found, swap it with either the successor or predecessor
	- Then continue recursively to delete the value of the successor/predecessor
- Actually swap nodes: keep sentinel
	- If not key is not root
		- Delete predecessor/successor, link sentinel to predecessor/successor left/right child 
			- Edge cases: Pred/succ is direct child of the key node (don't set the sentinel's children otherwise you lose the opposite side of the root and also create a cycle on the same side)
		- Connect the sentinel to the new Pred/succ tree, keep track of which side the child node is one
	- Else key is root:
		- Return the successor/predecessor
```python
class Solution:
    # One step right and then always left
    def successor(self, root: TreeNode) -> int:
            root = root.right
            while root.left:
                root = root.left
            return root.val
        
    # One step left and then always right
    def predecessor(self, root: TreeNode) -> int:
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # The node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root
```
https://leetcode.com/problems/delete-node-in-a-bst/



# Dynamic Programming

# Data Structures
## LRU Cache
 - Hashmap: store key, value. Value can be a node
 - Doubly linked list to store LRU nodes
 - Get:
	 - Remove node
	 - Add node
- Put:
	- Add node
	- If over capacity, remove LRU 
- Remove:
	- Get node from hashmap
	- Update prev.next and next.prev
## LFU Cache
- Two hashmaps + doubly linked list: (freq, doubly linked list) and (key, value)
## Suffix Tree


# Graph
## Topological Sort
### Longest Increasing Path in a Matrix
- Starting point must have indegree = 0
- DFS times out here if not using dp because nodes are revisited multiple times in different paths
- Topological sort(bfs with kahn's) only appends the current node if indegree = 0, in other words, all nodes that can traverse to this node have already done so.
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

# Queue
> Always check that the q is non empty before any other condition
- Key: think about what (key) determines the simulation and keep it in a queue
	- what is being manipulated in the simulation (ie: elements or indices)
## Queue Simulation
>You will do the following steps repeatedly until all cards are revealed.
>1. Take the top card of the deck, reveal it, and take it out of the deck.
>2. If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
>3. If there are still unrevealed cards, go back to step 1. Otherwise, stop.
- Simulate the queue of indices ("no need to work backwards")
- The resulting simulation will be the order in which numbers are printed
	- Then assign the sorted numbers to this sequence
- key: the indices determine the order of sorted numbers
Return an ordering of the deck that would reveal the cards in increasing order.
```python
def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
	deck.sort()
	q = deque()
	# queue of indices
	for i in range(len(deck)):
		q.append(i)

	res = [0]*len(deck)
	for card in deck:
		# set the cards in sorted order
		# the index of this card will be at the start of the q
		res[q.popleft()] = card
		if q:
			q.append(q.popleft())

	return res
```
# Sliding Window
## Subarrays with K Different Integers
https://leetcode.com/problems/subarrays-with-k-different-integers/?envType=daily-question&envId=2024-03-30
```python
def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
	return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)

def slidingWindowAtMost(self, nums: List[int], distinctK: int) -> int:
	freq_map = defaultdict(int)
	left = 0
	total_count  = 0

	for right in range(len(nums)):
		freq_map[nums[right]] += 1

		# If the number of distinct elements in the window exceeds k,
		# we shrink the window from the left until we have at most k distinct elements.
		while len(freq_map) > distinctK:
			freq_map[nums[left]] -= 1
			if freq_map[nums[left]] == 0:
				del freq_map[nums[left]]
			left += 1

		# Update the total count by adding the length of the current subarray.
		total_count  += right - left + 1
	return total_count 
```


## DP
https://leetcode.com/problems/partition-array-for-maximum-sum/description/
https://leetcode.com/problems/palindrome-partitioning-ii/description/
https://leetcode.com/problems/number-of-great-partitions/description/
# Python
- Parameters are passed by assignment which is actually a reference to the object
- Lists passed as parameters can be mutated, .append, but not reassigned using  =
- String is immutable, to get around this, return a new string






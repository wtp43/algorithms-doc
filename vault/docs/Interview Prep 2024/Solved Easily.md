---
created: ""
---
---

# Arrays
# Binary Trees
### Trim a Binary Search Tree
remove all elements not in `[low, high]`
- recursively return child nodes based on root.val
https://leetcode.com/problems/trim-a-binary-search-tree/description/

### Flip Equivalent Binary Trees
determine if two trees are flip equivalent (equal if child subtrees can be flipped)
- check both root vals, then check child + child/flipped with recursion
- Note: to check if one root is null, `if not a or not b` is not equivalent to `if a or b` 
https://leetcode.com/problems/flip-equivalent-binary-trees/description/

### Check Completeness of a Binary Tree
- bfs with deque
- once a null node is reached, another non null node cannot exist
https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/ 

### Sum Root to Leaf Numbers
- dfs from root to leaf nodes, keep track of the sum and multiply it by 10 for any non null node
- note: multiplication and addition is intrinsically faster than concatenation and casting
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

### Symmetric Tree
Determine if the tree is a mirror of itself
- Compare both left and right children to see if they are equal
- If they are, compare the inner children(left.right, right.left) and the outer children (left.left, right.right)
```python
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
	def isMirror(r,l):
		if not r and not l:
			return True
		if not r or not l:
			return False
		return r.val == l.val and isMirror(l.left, r.right) and isMirror(l.right, r.left)
	return isMirror(root, root) 
```
https://leetcode.com/problems/symmetric-tree/description/

### Time Needed to Inform All Employees
This may look like bfs but iterating in levels is not needed since each employee does not have to wait until they are finished before notifying their subordinates
```python
def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
	employees = defaultdict(list)
	q = deque([(headID,0)])
	# build adjacency list
	for i,val in enumerate(manager):
		employees[val].append(i)
	time = 0
	while q:
		employee, t = q.popleft()
		t += informTime[employee]
		# Keep track of max time 
		time = max(time, t)
		for e in employees[employee]:
			q.append((e, t))
	return time
``` 
https://leetcode.com/problems/time-needed-to-inform-all-employees/description

### Valid Binary Search Tree
- Recursively update the low and high boundaries at each recursion
```python
 def isValidBST(self, root: TreeNode) -> bool:
	def validate(node, low=-math.inf, high=math.inf):
		if not node:
			return True
		if node.val <= low or node.val >= high:
			return False
		# the new low and high values should be updated with the current
		# node's val			
		return (validate(node.left, low, node.val) and
			   validate(node.right, node.val, high))

	return validate(root)
```
https://leetcode.com/problems/validate-binary-search-tree/description/

### Minimum Difference between BST Nodes
Nodes do not have to be adjacent
- In-order traversal
- Optimization: instead of saving the entire list, store the prev value and only compare adjacent values in the in order traversal
- Update prev after processing min_diff
https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

### Cutting Ribbons (get max length of ribbon length such that there can be k cuts)
- right bisect
- have to check every single ribbon
- Mininum ribbon size is not equal to smallest ribbon because the smallest ribbon can be omitted if number of ribbons > k
```python
def maxLength(self, ribbons: List[int], k: int) -> int:
	if sum(ribbons) < k:
		return 0
	hi = max(ribbons)
	lo = 1

	while lo <= hi:
		mid = lo + (hi-lo)//2
		c = 0
		for r in ribbons:
			c += r//mid
		if c >= k:
			lo = mid + 1
		else:
			hi = mid - 1
	return hi
```
https://leetcode.com/problems/cutting-ribbons/description/
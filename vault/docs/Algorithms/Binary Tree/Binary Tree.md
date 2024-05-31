## Binary Trees

### Basic Operations

#### Insert

```python
def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
	if not root:
		return TreeNode(val)
	if val > root.val:
		root.right = self.insertIntoBST(root.right, val)
	else:
		root.left = self.insertIntoBST(root.left, val)
	return root
```

https://leetcode.com/problems/insert-into-a-binary-search-tree/

#### Delete

#### Closest BST Value to Target

- Specify key for min function
- Traverse to left child if target is smaller than root.val, else go right

```python
def closestValue(self, root: TreeNode, target: float) -> int:
	closest = root.val
	while root:
		closest = min(root.val, closest, key = lambda x: abs(target - x))
		root = root.left if target < root.val else root.right
	return closes
```

### Width Type Questions

- ie: check for completeness
- level traversal with BFS

### Traversals

#### In Order Traversal to Balance BST

- Create sorted array with in order traversal
- Add middle node recursively

```python
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sortedArr = []
        def inorderTraversal(root):
            if not root:
                return None
            inorderTraversal(root.left)
            sortedArr.append(root)
            inorderTraversal(root.right)

        def sortedArrToBST(left, right):
            if left > right:
                return None

            mid = (right+left)//2 ## ceil of this also returns another valid balanced tree
            new_root = sortedArr[mid]
            new_root.left =  sortedArrToBST(left, mid-1)
            new_root.right = sortedArrToBST(mid+1, right)
            return new_root
        inorderTraversal(root)
        return sortedArrToBST(0, len(sortedArr)-1)
```

#### Level Order Traversal

- The position of the child node can be calculated with - left child: `pos*2 - 1` - right child: `pos*2`
  https://leetcode.com/problems/maximum-width-of-binary-tree/description/

#### Zigzag Order Traversal

The ordering of nodes on alternating levels should be reversed

- Use delimiter (ie: None) to indicate end of current level
- Edge case: Empty tree, results in infinite loop

```python
 def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
	res = []
	level = deque([])
	if not root:
		return None
	q = deque([root, None])
	reverse = True
	while q:
		node = q.popleft()
		if node:
			if reverse:
				level.append(node.val)
			else:
				level.appendleft(node.val)
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
		else:
			res.append(level)
			if q:
				q.append(None)
			level = deque()
			reverse = not reverse
	return res
```

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description

#### Vertical Order Traversal

![[Pasted image 20240304190355.png]]
res:`[[4],[9,5],[3,0,1],[8,2],[7]]`

- BFS with root set to col 0
- Left child has parent col - 1, right child has parent col + 1
- Since there can't be null cols, we don't have to sort col indices and just

```python
def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
	col = defaultdict(list)
	if not root:
		return []
	q = deque([(root,0)])
	min_col = max_col = 0

	while q:
		for i in range(len(q)):
			node, i = q.popleft()
			col[i].append(node.val)
			min_col = min(min_col, i)
			max_col = max(max_col, i)

			if node.left:
				q.append((node.left, i-1))
			if node.right:
				q.append((node.right, i+1))
	# Note there cannot be null cols because of the way
	# col is built
	return [col[i] for i in range(min_col, max_col+1)]
```

#### Vertical Order Traversal Sorted

- A row value is used to determine order for nodes with duplicate values
- Two types of sorting:
  - Global Sorting: O(NlogN)
  - Partition Sorting (Sort each column): O(Nlog(N/k))

```python
def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
	if root is None:
		return []

	col = defaultdict(list)
	min_col= max_col= 0

	q = deque([(root, 0, 0)])

	while q:
		node, r, c = q.popleft()

		if node is not None:
			# sort by row first
			col[c].append((r, node.val))
			min_col= min(min_col, c)
			max_col= max(max_col, c)
			q.append((node.left, r+1, c-1))
			q.append((node.right, r+1, c+1))

	res = []
	for c in range(min_col, max_col+ 1):
		# partition sort
		res.append([val for row, val in sorted(col[c])])
	return res
```

#### N-ary Tree Level Order

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        traversal = []
        q = [root]
        while q:
            current_layer = []
            traversal.append([])
            for node in q:
                traversal[-1].append(node.val)
                current_layer.extend(node.children)
            q = current_layer
        return traversal
```

### Verify Preorder

https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/editorial/?envType=weekly-question&envId=2024-04-08

- Mono dec. stack
- We can add a smaller number to the stack if we are the left side of the subtree
- Once we reach the right side of the subtree (number is greater than last one on the stack), we need to keep track of the value of the parent
  - New nodes on the right side of the subtree of cannot be smaller than the parent (since we are on the right side)

```python
def verifyPreorder(self, preorder: List[int]) -> bool:
	min_limit = -inf
	stack = []

	for num in preorder:
		while stack and stack[-1] < num:
			min_limit = stack.pop()

		if num <= min_limit:
			return False

		stack.append(num)

	return True
```

- Verifying in order is easy: list must be sorted
- Verifying post order: iterate list in reverse
  - pop from stack if we encounter a smaller number than top of stack
    - This means we are now on the left side of the tree, new nodes cannot be greater than this parent value
  - add to stack if we encounter numbers greater than the current (we are in the right side of the tree)


### LCA 
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
- If we are at the LCA, then p and q must be on different sides of the tree

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            elif left:
                return left
            else:
                return right
        
        return dfs(root)
```
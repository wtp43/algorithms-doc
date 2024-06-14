## Binary Search Tree

```python
# inorder Traversal
def traversal(node):
	if not node{
		traverse(node.left)
		process(node)
		traverse(node.right)
	}

# find min
min_node = root
while (min_node.left) {
	min_node = min_node.left
}

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


# Deleting a node
def deleteNode(root, key):

    if root is None:
        return root

    # Find the node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)

        root.key = temp.key

                                                                                                                                         oot.right = deleteNode(root.right, temp.key)

    return root
```
## Perfect Tree
- All its leaves are at the same distance from the root

## Quasi-Perfect tree
- All its leaves are on at most two levels. The second level form the bottom is completely full and all the leaves on the bottom level are grouped to the left. 

# Implementation

```python

```

## Optimizations

## Optimized Complexity

:::Time-Complexity[Time Complexity] 


:::

:::Space-Complexity[Space Complexity] 


:::



# Related
=======
---
## Trees

**Theorem**: An undirected graph is a tree iff it is minimally connected.
The following are equivalent

- A tree is an undirected graph G = (V, E) that is connected and acyclic.
- All the following are equivalent:
- G is a tree.
- G is connected and acyclic.
- G is minimally connected (removing any edge from G disconnects it.)
- G is maximally acyclic (adding any edge creates a cycle)
- G is connected and |E| = |V| - 1.

## Re-rooting Tree

##### Sum of Distances in Tree

https://leetcode.com/problems/sum-of-distances-in-tree/description/


## Practice Problems

- [ ] [[LC-108. Convert Sorted Array to Binary Search Tree]]
	- Height-balanced BST
	- Pick the middle as the root (l+r)//2
	- Recursively build the left and right child while omitting the middle
	- Base case: l > r

- [ ] [[LC-572. Subtree of Another Tree]]
	- Check the subtree for every node in the other tree
	- O(mn)
- [ ] [[LC-543. Diameter of Binary Tree]]
	- Precompute the maximum depth from the left and right child (# of nodes)
		- number of nodes = 1 + max(l,r)
	- res = max(res, l+r)
		- longest path = number of nodes in l - 1 + number of nodes in r + 1 + 2(for the edges connecting l and r through the root)
	- Store the result of the max diameter at each recursion because it may not pass through the root
```python
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            res = max(res, l + r)
            return 1 + max(l, r)

        dfs(root)
        return res
```

[LC-112. Path Su](</docs/Some Leetcode Questions/LC-112. Path Sum.md>)	- Find if there is a path from root-to-leaf, leaf = node with no children
```python
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.right and not root.left:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum-root.val) or \
            self.hasPathSum(root.right, targetSum-root.val)
```


**Leaf-Similar Trees**
https://leetcode.com/problems/leaf-similar-trees/description/
```python
def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node: 
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))
```

**Iterative Traversals**
```python
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack = root, []
        res = []
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            cur = stack.pop()
        return res
 def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        res = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

#post order traversal iteratively is very convoluted

	Append right, then left because of FILO
	Process node if it is a leaf or if it's left or right child has been visited
	Keep track of last processed nodey

def postorderTraversal(self, root: 'TreeNode'):
        if not root:
            return []
        stack, res = [root], []
        # used to record whether left or right child has been visited
        last = None

        while stack:
            root = stack[-1]
            # if current node has no left right child, or left child or right child has been visited, then process and pop it
            if not root.left and not root.right or last and (root.left == last or root.right == last):

                res.append(root.val)

                stack.pop()
                last = root
            # if not, push right and left child in stack
            else:
                # push right first because of FILO
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return res

            

```
**Level Order Traversal**
- Use queue
- `while len(queue)>0`

# Segment Trees
https://www.reddit.com/r/leetcode/comments/wrrrq0/when_to_use_monotonic_queue/

# BST Traversals
https://leetcode.com/problems/inorder-successor-in-bst/solutions/1104016/inorder-successor-in-bst/


# AVL Trees
https://www.youtube.com/watch?v=g4y2h70D6Nk
>>>>>>> 5a71c508d3099d93f3f323e8771832c0fd64195d

---
title:  "Trees"
created: 2023-01-05
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Trees

It is usually easier to consider one-indexed arrays. Let the root be at index 1, then the two children of a node $i$ are at $2i$ and $2i + 1$


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

>[!Time Complexity]+

>[!Space Complexity]+



# Related

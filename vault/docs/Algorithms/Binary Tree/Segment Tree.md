# Segment Tree
> Allows answering range queries over an array efficiently
- Tree with nodes storing information about array intervals

## 2D Segment Tree 
- Leaf nodes or leaf vertices have range = 1
- Since there are n leaf nodes, the tree will require $2^{n+1}$ nodes
- We pad the number of nodes to $2^{\text{floor}({log_2{n})}+2}$ to make a complete binary tree
- This prevents hard to query trees like the ones below
 ![[Pasted image 20240601175345.png]]
### Construction
1. Start at leaf vertices
2. Compute values of previous level using `merge` function
3. Repeat `merge`

### Sum Queries
> Compute sum of the segment `a[l..r]` in O(log$n$)

### Update Queries
- Each level of a segment Tree

## Python Implementation
- 1 indexed, root is at v=1, left child at = $v*2$, right child at = $v*2+1$
- 
```python
class SegmentTree:

    def __init__(self, a: List[int]):
        self.n = len(a)
        self.t = [0] * 4 * self.n
        self.buildTree(a, 1, 0, self.n-1)
    
    def buildTree(self, a, v, tl, tr):
        if tl == tr:
            self.t[v] = a[tl]
            return

        tm = (tl + tr) // 2
        self.buildTree(a, v*2, tl, tm)
        self.buildTree(a, v*2+1, tm+1, tr)
        self.t[v] = self.t[v*2] + self.t[v*2+1]


    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.t[v] = new_val
            return

        tm = (tl + tr) // 2
        if pos <= tm:
            self.update(v*2, tl, tm, pos, new_val)
        else:
            self.update(v*2+1, tm+1, tr, pos, new_val)

        self.t[v] = self.t[v*2] + self.t[v*2+1]

    def sumRange(self, v, tl, tr, l, r):
        if l > r:
            return 0

        if tl == l and tr == r:
            return self.t[v]

        tm = (tl + tr) // 2
        return self.sumRange(v*2, tl, tm, l, min(r, tm)) + self.sumRange(v*2+1, tm+1, tr, max(l, tm+1), r) 
```

## More Complex Queries
### Finding the Maximum

### Finding the Maximum and the Number of Times it Appears

## References
https://cp-algorithms.com/data_structures/segment_tree.html
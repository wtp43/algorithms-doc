# Structuring a Solution

### Find a starting point

- Where can I start building the solution
- Can I start from the minimum element?
  - Determine if this starting point passes edge cases
- What algorithms and data structures can I use?
- Does order in which we do the operations matter?

## Intuition

- Find minimum chunk after k cuts/Minimum group size
  - Binary search on group size then greedily make cuts once group reaches threshold
- Can the target we are optimizing be simplified?
  - Compute some `cost[i] = s[i] - t[i]`
- What does a valid solution/representation of f() look like?
  - Suppose we need to the minimum number of swaps to group all 1's in an array together
  - Then the result of this is a k sized window
- What operations can bring us to the target?
  - https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
  - Think about which elements are valid/can be used in a operation


## Subarray
- Prefix/Suffix sum
- Sliding window
## Subsets
- Order does not matter
- Dynamic programming

## Subsequence
- Order does matter
- Dynamic Programming

### Minimum Deletions to Make Character Frequencies Unique

- https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/
- Sort descending and keep track of max_freq_allowed that does not
- Initially set max_freq_allowed to 0
- Set max_freq_allowed to current valid freq -1

```python
def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        freq = sorted(freq.values(), reverse=True)
        max_freq_allowed = len(s)
        res = 0
        for f in freq:
            if f > max_freq_allowed:
                res += f-max_freq_allowed
                f = max_freq_allowed

            max_freq_allowed = max(0, f-1)
        return res
```


## Array Indices

- The number of items in i to j inclusive = i-j+1
- The number of steps to get from i to j = j - i
- The number of items between i and j non inclusive = j-i-1


## Recursion

- Update answer at a valid state

https://leetcode.com/problems/smallest-string-starting-from-leaf/description/

```python
def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
	ans = ""
	def dfs(root, cur_str):
		nonlocal ans
		if not root:
			return
		cur_str = chr(root.val+ord("a")) + cur_str
		# easier to update answer at a valid state
		# instead of min(left, right) and then having
		# to determine if left or right is valid
		if not root.left and not root.right:
			if not ans or cur_str < ans:
				ans = cur_str

		if root.left:
			dfs(root.left, cur_str)
		if root.right:
			dfs(root.right, cur_str)
	dfs(root, "")
	return ans
```

## DP Tricks

- Memoizing with dictionary by using sets as keys
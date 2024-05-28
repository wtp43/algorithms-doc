---
id: Revision Feb 2024
aliases: 
created: ""
---
	
---
# Structuring a Solution

### Find a starting point

- Where can I start building the solution
- Can I start from the minimum element?
  - Determine if this starting point passes edge cases
- ## What algorithms and data structures can I use?
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

- Memoizing with dictionary by using sets/lists as keys

# Essentials

## Arrays

- If range (inclusive): j-i+1
- If index/position difference: j-i

#### Prefix/Suffix Sum/Max

- Useful for subarrays not subsequences
- Hint: When question requires you to find a pair of indices that satisfies k
  - Store prefix sum in hashmap with `nums[i]` as key

##### Sum of Distances

https://leetcode.com/problems/sum-of-distances/description/

- Store occurences/indices in dictionary
- Iterate all indices of each key in the dictionary
- Build prefix and suffix sum for each key
- Complexity: O(n) for each number + O(n) to sum

```python
def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)

        arr = [0]*len(nums)
        for x in d:
            prefix = 0
            suffix = sum(d[x])
            n = len(d[x])
            p = 0
            for i in d[x]:
                arr[i] = i*p-prefix + suffix-i*(n-p)
                p += 1
                prefix += i
                suffix -= i
        return arr
```

#### Max Partitions Allowed to Make Sorted Array

- Split arr into maxiumum number of individually sorted partitions such that concatenated array is also sorted
- A partition is only possible if the maximum prefix is less than the minimum suffix

```python
def maxChunksToSorted(self, arr: List[int]) -> int:
        # a partition can be made if
        # max[:i+1] < min[i+1:]

        n = len(arr)
        minSuffix = [math.inf]*(n+1)
        for i in range(n-1, 0, -1):
            minSuffix[i] = min(arr[i], minSuffix[i+1])

        maxPrefix = 0
        partition = 0
        for i in range(n):
            maxPrefix = max(maxPrefix, arr[i])
            if maxPrefix <= minSuffix[i+1]:
                partition += 1
        return partition
```

### Kadane's

> Used to find max subarray (contiguous array)

https://leetcode.com/problems/substring-with-largest-variance/solutions/2579146/weird-kadane-intuition-solution-explained/

### Maximum Array after swapping equal length subarray

- Kadane's can be used to find the maximum subarray.
- INTUITION: We are trying to maximum the sum of the subarray after the swap. This is the same as precomputing a cost array for swapping the ith element.

```python
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        arr = [0]*n
        # compute cost (of swapping ith element) array
        for i in range(n):
            arr[i] = nums2[i] - nums1[i]
        # Run Kadane's twice
        cur = max_s = 0
        for i in range(n):
            cur = max(cur+arr[i], 0)
            max_s = max(max_s,cur)
        cur = max_t = 0
        for i in range(n):
            cur = max(cur-arr[i], 0)
            max_t = max(max_t, cur)
        return max(max_s+sum(nums1), max_t+sum(nums2))

```

## Backtracking

### Including or not including

- No for loop needed in each backtrack because there is only two options
  - Take i or don't take i compared to take or don't take for each of remaining numbers

#### Power Set

```python
def subsets(self, nums: List[int]) -> List[List[int]]:
	res = []
	n = len(nums)
	subset = []
	def backtrack(i):
		if i == n:
			res.append(subset.copy())
			return
		subset.append(nums[i])
		backtrack(i+1)
		subset.pop()
		backtrack(i+1)
	backtrack(0)
	return res
```

### Picking the element for the current position

#### Permutations

- Swap first num with all nums after it and backtrack (equivalent to choosing a num for every single position)

```python
def permute(self, nums: List[int]) -> List[List[int]]:ķ        res = []
	n = len(nums)
	def backtrack(i):
		if i == n-1:
			res.append(nums.copy())
			return
		for j in range(i, n):
			nums[i], nums[j] = nums[j], nums[i]
			backtrack(i+1)
			nums[i], nums[j] = nums[j], nums[i]
	backtrack(0)
	return res
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
	res = []
	n = len(nums)
	def backtrack(i):
		if i == n-1:
			res.append(nums.copy())
			return
		starting_num = set()
		for j in range(i, n):
			if nums[j] in starting_num:
				continue
			nums[i], nums[j] = nums[j], nums[i]
			backtrack(i+1)
			nums[i], nums[j] = nums[j], nums[i]
			starting_num.add(nums[j])

	backtrack(0)
	return res
```

#### Combinations

- build combination by picking a number from (i,n)
- keep track of how many numbers are needed (only backtrack if available numbers is enough for remaining numbers needed)

```python
def combine(self, n: int, k: int) -> List[List[int]]:
	combination, res = [], []

	def backtrack(i, need):
		if need==0:
			res.append(combination.copy())
			return

		remain = (n+1) - i
		available = remain-need

		for j in range(i, i + available + 1):
			combination.append(j)
	return res
```

#### n- queens

- Sets: col, row, neg diag, pos diag

```python
 def solveNQueens(self, n: int) -> List[List[str]]:
	res = []
	col = set()
	posDiag = set()  # (r + c)
	negDiag = set()  # (r - c)
	board = [['.']*n for i in range(n)]

	def backtrack(r):
		if r == n:
			copy = ["".join(row) for row in board]
			res.append(copy)
			return
		for c in range(n):
			if c in col or (r + c) in posDiag or (r - c) in negDiag:
					continue
			col.add(c)
			posDiag.add(r + c)
			negDiag.add(r - c)
			board[r][c] = "Q"

			backtrack(r + 1)

			col.remove(c)
			posDiag.remove(r + c)
			negDiag.remove(r - c)
			board[r][c] = "."


	backtrack(0)
	return res
```

### Paths

- Manhattan Distance: abs distance between start and destination

```python
def uniquePathsIII(self, grid: List[List[int]]) -> int:
	m,n = len(grid), len(grid[0])
	squares = 0
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				start = (i,j)
			elif grid[i][j] == 2:
				end = (i,j)
			if grid[i][j] != -1:
				squares += 1
	visited = set([start])
	squares-= 2
	paths = 0
	def backtrack(pos, squares):
		nonlocal paths
		i,j = pos
		if pos == end:
			paths += 1
			return
		for x,y in [[0,1], [0,-1], [1,0], [-1,0]]:
			new_x = j+x
			new_y = i+y
			new_pos = (new_y, new_x)
			if new_pos in visited or new_x < 0 or new_x >= n or new_y < 0 or new_y >= m or grid[new_y][new_x] == -1:
				continue
			if new_pos == end and squares > 0:
				continue
			manhattan_distance = abs(end[0] - new_pos[0]) + abs(end[1] - new_pos[1])
			if squares < manhattan_distance - 1:
				continue
			visited.add(new_pos)
			backtrack(new_pos, squares-1)
			visited.remove(new_pos)
	backtrack(start, squares)
	return paths
```

### 0-1 Knapsack

## Binary Search

> [!danger] Intuition
> Determine whether left or right bisect is needed. This is relevant for questions where more than one 'target' or 'x' can satisfy the conditions (but do we want the biggest 'target' or smallest 'target'). The 'target' to be searched is usually found on some range (which is sorted by default).

### Search for "X" on a Range

### Bisect Process

- What is the target?
- If the target is >= threshold, should we decrease or increase mid?
- Do we want to return hi or lo?
  - Depends on if we want rightmost x or leftmost x

### Bisect left/right

- Implementation differs only at the comparison
- Bisect left:
	- If condition is met:
		- always decrease right
-  Bisect right
	- If condition is met:
		- always increase left

```python
def bisect_left(arr, x):
	lo = 0
	hi = len(arr)-1
	while lo <= hi:
		mid = lo + (hi - lo)//2
    # in bisect left, to return lo, the condition must be strictly > or strictly <
		if arr[mid] < x:
			lo = mid + 1
		else:
			hi = mid - 1
	return lo

lo = first position where arr[lo] > x
hi = position before lo
	lo = 0
	hi = len(arr)-1
	while lo <= hi:
		mid = lo + (hi - lo)//2
		if arr[mid] <= x:
			lo = mid + 1
		else:
			hi = mid - 1
	return lo
```

### Framework for using Binary Search to Find Minimum Group Size

### Replacing DP

#### Minimize Maximum Difference of Pairs

- we don't need dp here because the minimum difference between two pairs occur next to each in a sorted array
- DP solution:
- Binary search
  - Sort (differences will be minimized)
  - Binary search the maximum difference on range (0, max difference of all pairs)

```python
def minimizeMax(self, nums: List[int], p: int) -> int:
	nums.sort()
	lo = 0
	hi = nums[-1]-nums[0]
	n = len(nums)
	while lo <= hi:
		mid = lo + (hi-lo)//2
		cnt = i = 0
		while i < n-1:
			if nums[i+1] - nums[i] <= mid:
				cnt += 1
				## skip the 2nd num used in the pair
				i += 1
			i += 1
		if cnt < p:
			lo = mid+1
		else:
			hi = mid-1
	return lo
	# nLogV + nlogn, V = maximum difference in array,
	# in each step of the binary search (total logV steps)
	# we have to determine how many pairs are valid (n steps)
```

### Median of Two Sorted Arrays

https://leetcode.com/problems/median-of-two-sorted-arrays/description/

- O(m+n): Merge both arrays and then binary search
- O(log(m + n)): smart binary search
  https://leetcode.com/problems/median-of-two-sorted-arrays/editorial/

### Advanced Binary Search

- Binary search can be used when f(x) is monotonic
- This is particularly efficient when searching for some f(x) on a range (a,b) where b-a is very large

#### Kth Smallest Amount With Single Denomination Combination

https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

```python
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        d = defaultdict(list)
        # lcm of all combinations: O(2**n)
        for i in range(1, n+1):
            for comb in itertools.combinations(coins, i):
                d[len(comb)].append(math.lcm(*comb))

        def count(d, target):
            ans = 0
            for i in range(1, n+1):
                for lcm in d[i]:
                    ans += target // lcm * pow(-1, i+1)
            return ans
        start, end = min(coins), min(coins) * k
        while start<= end:
            mid = (start + end) // 2
            c = count(d, mid)
            if c >= k:
                # continue iterating until we find a valid number
                end = mid -1
            else:
                start = mid+ 1
        if count(d, start) >= k:
            return start
        else:
            return end
```

### Kth Smallest Pair Distance

https://leetcode.com/problems/find-k-th-smallest-pair-distance

```python
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        start = 0
        end = max(nums)
        n = len(nums)
        # sort to calc min distances iteratively
        nums.sort()
        # how many pairs have less distance than cur
        def count(nums, dist):
            ans = i = j = 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= dist:
                    j += 1
                ans += j-i-1
                i += 1
            return ans

        while start <= end:
            mid = start + (end-start)//2
            if count(nums,mid) < k:
                start = mid + 1
            else:
                end = mid - 1
        return start
```

#### Largest Subarray Sum After K Splits

https://leetcode.com/problems/split-array-largest-sum/description/

```python
def splitArray(self, nums: List[int], k: int) -> int:
        def count(nums, limit):
            ans = 1
            cur = 0
            for x in nums:
                if cur + x > limit:
                    ans += 1
                    cur = 0
                cur += x
            return ans

        start, end = max(nums), sum(nums)
        while start <= end:
            mid = start + (end-start)//2
            if count(nums, mid) <=  k:
                end = mid-1
            else:
                start = mid+1
        return start
```

#### Kth Smallest Number in Multiplication Table

https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/

```python
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(x):
            ans = 0
            for i in range(1, m+1):
                ans += min(x//i, n)
            return ans
        lo, hi = 1, m*n
        while lo <= hi:
            mid = (lo + hi)//2
            if count(mid) < k:
                lo = mid+1
            else:
                hi = mid-1
        return lo
```

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

## Bit Operations

- Largest bit will be greater than all other bits combined

```python
& AND
| OR
^ XOR
~ NOT (equivalent to n-1 which flips all bits)
<< Bitwise left shift
>> Bitwise right shift

#Bitmask
#Check if ith bit is set
mask & 1 << i

#Flip ith bit
mask ^ 1 << i 

#Clear ith bit
mask & ~(1 << i)

#Check if number is divisible by 2 to the power of k
mask & (1<<k-1) == 0

#Check if an integer is a power of 2
mask and not (mask & (mask-1))

#Clear the right-most set bit
n & (n-1)
This works because n-1 flips all bits after the rightmost set bit of n

#Clear all trailing ones
n & (n+1)

#Set the last cleared bit
n | (n+1)

#Extract last set bit
n & -n

```

### Minimum Operations to Form Subsequence with Target Sum
https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/description/



### Brian Kernighan's Algorithm

- Count bits

```c++
int countSetBits(int n)
{
  int count = 0;
  while (n)
  {
    n = n & (n-1);
    count++;
  }
  return count;
}

```

### Mod 3 with XOR (Mimic hash map with multiple masks)
https://leetcode.com/problems/single-number-ii/description/?envType=study-plan-v2&envId=top-interview-150
### Detect Power of Two

- Set most significant bit to zero and compare result to zero
  `x & (x-1) == 0`

### Subtraction under modulo 2

- XOR operator is equivalent to subtraction under modulo 2
- Useful for storing prefix of a binary

### Binary Prefix

- XOR current mask = `str[:i+1]` and some `prefix[:j]` to determine f(i)
- Prefix masks can be stored in a hash map

#### Count Substrings Without Repeating Characters

- Sliding window
- Bitmask or hashmap
- Reduce window size if count of 2 is reached
- Setting i to the next position of where the previous s[j] occurred does not guarantee that the window has no repeating characters

```python
def numberOfSpecialSubstrings(self, s: str) -> int:
        i = mask = res = 0
        for j in range(len(s)):
            ind = ord(s[j])-ord("a")
            while i < j and mask & 1<<ind:
                mask ^= 1 << (ord(s[i]) - ord('a'))
                i += 1
            res += j-i+1
            mask ^= 1 << ind
        return res
```

##### Longest Substring with At Most One Character with Odd Count

https://leetcode.com/problems/find-longest-awesome-substring/description

```python
def longestAwesome(self, s: str) -> int:
        prefix = defaultdict(int)
        prefix[0] = -1
        mask = res = 0
        for i in range(len(s)):
            mask ^= 1 << int(s[i])

            # even length palindrome
            if mask in prefix:
                res = max(res, i-prefix[mask])
            else:
                prefix[mask] = i

            # odd length palindrome
            # fix one char to be the odd one
            for j in range(10):
                cur = mask ^ (1 << j)
                if cur in prefix:
                    res = max(res, i-prefix[cur])
        return res
```

#### Hamming Distance

```python
x.bit_count()
bin(x).count('1')

# get rightmost bit every loop
while x:
  count += x%2
  x//2
```

### Rolling Hash

- Remove most significant bit, add least significant bit

```python
val = ((val<<1) & all_one) | last_digit_of_new_hash
# all_one is a binary string of length k with all 1's
ex: k = 4, all_one = 1111
val = 1010, next_digit = 1
val<<1 & all_one = 0100
new_val = 0101
```

#### Check if A string Contains All Binary Codes of Size K

```python
def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1<<k
        seen = [False]*need
        all_one = need-1
        hash_val = 0
        for i in range(len(s)):
            hash_val = ((hash_val<<1)&all_one) | int(s[i])
            if i >= k-1 and not seen[hash_val]:
                seen[hash_val] = True
                need -= 1
                if need == 0:
                    return True

        return False
```

## Data Structures

- LFU/LRU cache

## Dynamic Programming

- Subsequence (the answer contains non adjacent elements) almost always requires DP

##### Longest Increasing Subsequence (LIS)

- DP: 0(n^2)
- Approach 1: Build LIS
- Approach 2: Binary search for first position cur num is smaller than `sequence[i]`

```python
def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)

def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for i in range(len(nums)):
            if not seq or nums[i] > seq[-1]:
                seq.append(nums[i])
            else:
                ind = bisect_left(seq, nums[i])
                seq[ind] = nums[i]
        return len(seq)
```

```python
def longestPalindromeSubseq(self, s: str) -> int:
	# current letter + longest palindrome subsequence of array of size 1 smaller
	# how to make a palindrome with the current letter:
	# find letter equal to current letter in a[0:i]
	# dp will be 2 + a[start+1:end-1] or max of subproblems(prefix and suffix with length of 1 smaller)

	n = len(s)

	dp = [[0]*n for _ in range(n)]

	for end in range(n):
		dp[end][end] = 1
		for start in range(end-1, -1, -1):
			if s[start] == s[end]:
				dp[start][end] =  2 + dp[start+1][end-1]
			else:
				dp[start][end] =max(dp[start][end-1], dp[start+1][end])

	return dp[0][-1]
```

### Subsequences

- It's only necessary to store the result of the subsequence
- ie: `dp[i][j]` is not the result of the array `[i:j]`

#### Length of Longest Subsequence that Sums to Target

https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

- Similar to coin change problem
- Base case: sum 0 has subsequence length 0
- Iterate over nums, update dp for num to target

```python
def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        res = 0
        n = len(nums)
        dp = [-math.inf]*(target+1)
        dp[0] = 0
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = max(dp[i], dp[i-num]+1)
        return dp[target] if dp[target] != -math.inf else -

# Coin Change
def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if c > i:
                    continue
                dp[i] =  min(dp[i], dp[i-c] + 1)
        return dp[-1] if dp[-1] != math.inf else -

```

## Graph Theory

- Be smart about where valid solutions can start

### Trees

**Theorem**: An undirected graph is a tree iff it is minimally connected.
The following are equivalent

- A tree is an undirected graph G = (V, E) that is connected and acyclic.
- All the following are equivalent:
- G is a tree.
- G is connected and acyclic.
- G is minimally connected (removing any edge from G disconnects it.)
- G is maximally acyclic (adding any edge creates a cycle)
- G is connected and |E| = |V| - 1.

#### Rerooting Tree

##### Sum of Distances in Tree

https://leetcode.com/problems/sum-of-distances-in-tree/description/

### DAG

- Acyclic
- Topological sort (Kahn's algorithm (in-degrees), DFS 3 color)

### DAG Scheduling

https://leetcode.com/problems/parallel-courses-ii/description/

```python
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        in_degrees = [0]*n
        graph = defaultdict(list)
        for u,v in relations:
            in_degrees[v-1] += 1
            graph[u-1].append(v-1)

        @lru_cache(None)
        def dfs(mask, in_degrees):
            if not mask:
                return 0
            # nodes that can be taken (if bit is 1)
            nodes = [i for i in range(n) if mask & 1 << i and in_degrees[i] == 0]
            ans = math.inf
            # Check all combinations with size k
            for k_nodes in combinations(nodes, min(k, len(nodes))):
                new_mask, new_in_degrees = mask, list(in_degrees)
                # set bit for all nodes in combination
                for node in k_nodes:
                    new_mask ^= 1 << node
                    for child in graph[node]:
                        new_in_degrees[child] -= 1
                # recurse
                ans = min(ans, 1+dfs(new_mask, tuple(new_in_degrees)))
            return ans
        return dfs((1<<n)-1, tuple(in_degrees))
```

#### Parallel Courses II

- Without the requirement `k`, this would be a topological problem
- Why do we need DP? There is no optimal subproblem on which course should be taken first.

### Representation

- Adjacency list: Dictionary, for sparse graphs
- Adjacency Matrix: for dense graphs

### BFS/DFS/IDS

- Level search
- Multi-source
### BFS vs DFS
- Space Complexity of DFS is only O(depth) while BFS is O(n) = O(|v|)
- BFS can guarantee shortest path
### BFS

```python
def bfs(graph: Dict[int, List[int]], start: int):

    q = deque([start])
    seen = [0]*n
    seen[start] = 1
	prev = [-1]*n

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if next in seen:
                continue
            q.append(next)
            seen[next] = 1
            prev[next] = cur
    return prev

def reconstruct_path(start, end, prev):
	path = []
	while end != -1:
		path.append(end)
		end = prev[end]
		if end == start:
			break
	path.reverse()

	# if traversing backwards starting from end gives
	# us the starting node, there exists a path
	if path[0] == s:
		return path
	return []
```

### DFS

#### Number of Increasing Paths in a Grid

https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/description/

- Build `dp[i][j]` from all neighbouring cells with DFS
- We don't have to start from the smallest valued cells since results are cached

```python
def countPaths(self, grid: List[List[int]]) -> int:
	# strictly increasing
	# compared 4-directionally

	m, n = len(grid), len(grid[0])
	mod = 10 ** 9 +7
	directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

	dp = [[-1] * n for _ in range(m)]

	def dfs(i, j):
		# If dp[i][j] is non-zero, it means we have got the value of dfs(i, j),
		if dp[i][j] != -1:
			return dp[i][j]

		answer = 1

		# Check its four neighbor cells, if a neighbor cell grid[prevI][prevJ] has a
		# smaller value, we move to this cell and solve the subproblem: dfs(prevI, prevJ).
		for di, dj in directions:
			prev_i, prev_j = i + di, j + dj
			if 0 <= prev_i < m and 0 <= prev_j < n and grid[prev_i][prev_j] < grid[i][j]:
				answer += dfs(prev_i, prev_j) % mod

		dp[i][j] = answer
		return answer

	return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod
```

### Bipartite Graph

- Thm: A graph is bipartite iff it contains no odd cycles

#### Bipartite Grouping

https://leetcode.com/problems/possible-bipartition/

- If a neighbor has the same color as the current node: no bipartite matching is possible
- Two color dfs: color all neighbors the opposite of the current node's color
  - Impossible if a neighbor has the same color as the current node
- Union Find: Union the first neighbor of U with all the other neighbors

```python
 def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # -1 is useful as the unvisited state
        # since 1,0 and can easily inversed
        state = [-1]*(n+1)
        graph = defaultdict(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(u,col):
            state[u] = col
            for v in graph[u]:
                if state[u] == state[v]:
                    return False
                if state[v] == -1:
                    if not dfs(v,1-col):
                        return False
            return True

        for i in range(1,n+1):
            if state[i] == -1:
                if not dfs(i,0):
                    return False
        return True
```

### A\* Search

> Requires a heuristic
> https://leetcode.com/problems/shortest-path-in-binary-matrix/editorial/

### Island Type Questions

#### Closed Island

- A closed island cannot have land on the edges of the grid
- Invalidate the island if any of it's squares on on the edge of a grid

```python
def closedIsland(self, grid: List[List[int]]) -> int:
	seen=set()
	res=0
	m,n = len(grid), len(grid[0])
	def dfs(r,c):
		nonlocal water
		if grid[r][c] == 1:
			return True
		if r == 0 or c == 0 or c == n-1 or r ==m-1:
			return False
		grid[r][c] = 1
		for ro, co in [(0,1), (0,-1), (1,0), (-1,0)]:
			row = ro + r
			col = co + c
			#if (row,col) in seen:
			#    continue
			#seen.add((row,col))
			# can't exit early otherwise not all 0's are marked
			#if not dfs(row,col):
			#    return False
			water &= dfs(row,col)
		return water
	for r in range(1,len(grid)-1):
		for c in range(1,len(grid[0])-1):
			# be smart about where to start dfs, corner zeros cannot build a valid island
			if (r,c) not in seen and grid[r][c] == 0:
				water = True
				#seen.add((r,c))
				if dfs(r,c):
					res += 1

	return res
```

https://leetcode.com/problems/number-of-closed-islands/description/

### Shortest Path Algorithms

- No weights: Use bfs
- Weights: use Dijkstra
- Negative weights/cycles: Bellman Ford (single source), Floyd Warshall (multi-source)

#### Bellman Ford

- SSSP (single source shortest path)
- Works for negative weights
- Relax all edges V-1 times

```python
def bellman_ford(graph, start):
	num_vertices = len(graph.get_vertices())
	edges = graph.get_edges()

	dist = [math.inf for i in range(num_vertices)]
	prev = [None for i in range(num_vertices)]

	dist[start] = 0
	#relax edges |V| - 1 times
	for _ in range(num_vertices - 1):
		for u, v, w in edges:
			new_dist = dist[u] + w
			if new_dist < dist[v]:
				dist[v] = new_dist
				prev[v] = u

	#detect negative cycles
	for u,v,w in edges:
		if dist[u] + w < dist[v]:
			raise NegativeWeightCycleError()
	return dist, prev
```

#### Floyd Warshall

- Shortest path algorithm from any vertex to all other vertices
- Works for negative weights and cycles

```python
def floyd(G):
    dis = [[math.inf] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
```

#### Dijkstra

- SSSP
- Finds the shortest path from the source node to all other nodes
- The result (shortest path tree) is not guaranteed to be a MST
- Works for both directed/undirected graphs
- Does not work for negative weights
- Works for graphs with cycles
- O(ElogV)

### Lazy Version of Dijkstra

- This version keeps a priority queue with Space Complexity O(E+V)
- Time Complexity: O(ElogE) vs O(ElogV) for "non-lazy"
  https://stackoverflow.com/questions/68977036/do-indexed-priority-queues-actually-speed-up-dijkstra
- This version works for negative weights as long as there is no negatively weighted cycle

```python
import heapq

def lazy_dijkstra(self, start):
	n = len(self.get_vertices())
	dist = [math.inf] * n
	prev = [None] * n
	dist[start] = 0
	seen = [0] * n
	pq = [(0, start)]
	heapq.heapify(pq)
	while pq:
		min_value, index = heapq.heappop(pq)
		# This must be a strict equality
	# If the cost is equal, we may not have updated it's neighbors yet
		if dist[index] < min_value:
			continue
		dist[index] = min_value
		seen.add(index)
		for u,v,w in self.get_edges(index):
			if seen[v]:
				continue
			new_dist = dist[index] + w
			if new_dist < dist[v]:
				dist[v] = new_dist
				prev[v] = u
				heapq.heappush(pq, (new_dist, v))
	return dist, prev
```

##### Minimum Cost to Buy Apples from n Cities
https://leetcode.com/problems/minimum-cost-to-buy-apples/description
- Modified dijkstra
- Instead of start dijkstra at every city, start at the min city and expand out while updating dist
- Start with heap of buying apple at the ith city without traveling
- Expand outwards from min city
```python
 def minCost(
        self, n: int, roads: List[List[int]], appleCost: List[int], k: int
    ) -> List[int]:
        graph = [[] for _ in range(n)]

        for city_a, city_b, cost in roads:
            graph[city_a - 1].append((city_b - 1, cost))
            graph[city_b - 1].append((city_a - 1, cost))

        result = list(appleCost)


        heap = [(apple_cost, start_city) 
                 for start_city, apple_cost in enumerate(appleCost)]
        heapify(heap)

        while heap:
            total_cost, curr_city = heapq.heappop(heap)
            if result[curr_city] < total_cost:
                continue
            for neighbor, cost in graph[curr_city]:
                if result[neighbor] > result[curr_city] + (k + 1) * cost:
                    result[neighbor] = result[curr_city] + (k + 1) * cost
                    heapq.heappush(heap, (result[neighbor], neighbor))
        return result       
```
##### Minimum Time to Visit Disappearing Nodes

https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

```python
def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
	ans = [math.inf]*n
	pq = [(0,0)]
	graph = defaultdict(list)

	for u,v,w in edges:
		graph[u].append((v,w))
		graph[v].append((u,w))
	while pq:
		u,time = heappop(pq)
		if time >= ans[u]:
			continue
		ans[u] = time
		for v,w in graph[u]:
			if ans[v] < time+w or disappear[v] <= time+w:
				continue
			heappush(pq,(v,time+w))
	for i,x in enumerate(ans):
		if x == math.inf:
			ans[i] = -1
	return ans
```

##### Number of Shortest Paths

https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/

- Only push neighbour to heap if cost is lower through the current node
  - Set the # of paths to v, to be equal to # of paths to u
- If the cost to get to the neighbour is equal to its current cost, we have found another route through u.
  - Append the # of paths from u onto v

```python
def countPaths(self, n: int, roads: List[List[int]]) -> int:
	pq = [[0,0]]
	min_time = math.inf
	paths = [0]*n
	paths[0] = 1
	time = [math.inf]*n
	graph = defaultdict(list)
	MOD = 10**9+7
	for u,v,t in roads:
		graph[u].append([v,t])
		graph[v].append([u,t])
	while pq:
		t,u = heappop(pq)
		# we don't skip if time[u] == t since
		# it's neighbors might not have been updated yet 
		if time[u] < t:
			continue
		for v, cost in graph[u]:
			# only add neighbor to q if we have
			# a shorter path
			if t + cost < time[v]:
				# must set time here and not after heappop
				paths[v] = paths[u]
				time[v] = t+cost
				heappush(pq, [time[v], v])
			elif t + cost == time[v]:
				paths[v] = (paths[v] + paths[u]) % MOD
	return paths[-1]
```

### Johnson's Algorithm (Modified Dijkstra) that works for negative weights (acyclic)

### Longest Path DAG

- In general, this is NP-Hard, but on a DAG this problem is solvable in O(V+E)
- Topological sort
- Process ordering sequentially
- Multiply edges values by -1 and find shortest path

### Minimum Spanning Tree Algorithms

- MST assumes graphs are inherently undirected
- A minimum cost tree that connects all nodes in the graph
- Does not guarantee the shortest path between two nodes in the original graph

**Theorem**: Let G be a connected, weighted graph. If all edge weights in G are distinct, G has exactly one MST
**Theorem (Cycle Property):** If (x, y) is an edge in G and is the heaviest edge on some cycle C, then (x, y) does not belong to any MST of G.
**Theorem (Cut Property):** Let (S, V – S) be a nontrivial cut in G (i.e. S ≠ Ø and S ≠ V). If (u, v) is the lowest-cost edge crossing (S, V – S), then (u, v) is in every MST of G.

#### Prim's

Greedy Algorithm

- Start at any vertex
- Repeatedly add the minimum edge that connects the tree to a new vertex
  - If each vertex has at most one edge to another vertex, then we are bounded by V here
- Complexity: O(E log V) with Priority Queue or O(E + VlogV) with a Fibonacci Heap

Implementation in python requires a modification of heapq since it does not provide a decrease-key function

- Typically, no decrease-key function is used and instead just append and invalidate entries later on in which case, the complexity is same as Kruskal's

- IMPORTANT: It does not matter which vertex you start at. There can be multiple MST's. This is because we are always choosing the lowest-cost edge for the current vertex

```python
MST-PRIM(G, w, r)
1  for each u ∈ G.V
2       u.key ← ∞
3       u.π ← NIL
4   r.key ← 0
5   Q ← G.V
6   while Q ≠ Ø
7       u ← EXTRACT-MIN(Q)
8       for each v ∈ G.Adjacent[u]
9           if v ∈ Q and w(u, v) < v.key
10              v.π ← u
11              v.key ← w(u, v)
```

**Using a Binary Heap**

1. The time complexity required for one call to `EXTRACT-MIN(Q)` is `O(log V)` using a min priority queue. The while loop at line 6 is executing total V times.so `EXTRACT-MIN(Q)` is called `V` times. So the complexity of `EXTRACT-MIN(Q)` is `O(V logV)`.
2. The `for` loop at line 8 is executing total `2E` times as length of each adjacency lists is `2E` for an undirected graph. The time required to execute line 11 is `O(log v)` by using the `DECREASE_KEY` operation on the min heap. Line 11 also executes total `2E` times. So the total time required to execute line 11 is `O(2E logV) = O(E logV)`.
3. The `for` loop at line 1 will be executed `V` times. Using the procedure to perform lines 1 to 5 will require a complexity of `O(V)`.
   Total time complexity of `MST-PRIM` is the sum of the time complexity required to execute steps 1 through 3 for a total of `O((VlogV) + (E logV) + (V)) = O(E logV)` since `|E| >= |V|`.
   **Using a Fibonacci Heap**
4. Same as above.
5. Executing line 11 requires `O(1)` amortized time. Line 11 executes a total of `2E` times. So the total time complexity is `O(E)`.
6. Same as above
   So the total time complexity of `MST-PRIM` is the sum of executing steps 1 through 3 for a total complexity of `O(V logV + E + V)=O(E + V logV)`.
   **Source**: https://stackoverflow.com/questions/20430740/time-complexity-of-prims-algorithm

##### Implementations

- Adjacency Matrix
- Adjacency List + Priority Queue (Heap)

```python
from collections import default dict
import heapq

edges = [(cost, v1, v2)...]
def prim(edges, start):
	mst = defaultdict(set)
	seen = set()
	graph = defaultdict(list)
	for u,v,cost in edges:
		graph[u].append([v,cost])
		graph[v].append([u,cost])

	total_cost = 0

  # start at any vertex
  # cost,u,v
  edges = [[0,1,2]]
  # Note: must call heapify(edges) if edges contain more than one initially
	while edges:
		cost, u, v = heapq.heappop(edges)
		# Important: There can be edges with visited nodes in the heap
		if v not in seen:
			seen.add(v)
			mst[u].add(v)

			total_cost += cost
			for w, ncost in graph[v]:
				# Update new reachable edges
				if w not in seen:
					heapq.heappush(edges,[ncost,v,w])
	return mst, total_cost
```

#### Kruskal's

- Greedy algorithm
- Repeatedly consider the minimum remaining edge
  - Only add it if the two vertices lie within different trees (to avoid cycles)
- Complexity: O(E log E) with Union-find and sorting edges

##### Implementations

- Union-find to store state of trees

```python
def kruskal(graph):
	mst = []
	uf = Union_find(graph.get_vertices())
	edges = graph.get_edges()
	# sort edges by cost
	edges.sort(key = lambda x: x[2])
	for u,v,cost in edges:
		# Only add edges that don't create a cycle
		if uf.find(u) != uf.find(v):
			mst.append([u,v,cost])
			uf.union(u,v)
	return mst

mst_weight = sum(t[2] for t in mst)
```

- If we know the upper bound of the cost of edges C, using count sort will allow us to sort in O(E + C), reducing the time complexity to just union-find: O()

#### Prim's vs Kruskal's

- Kruskal's is more efficient on sparse graphs than Prim's algorithm
- Kruskal's will not provide a valid MST mid algorithm unlike Prim

#### Enumerating all MST's

- Generate one MST
- Then generate all spanning trees and then filter by cost
  - Generating all spanning trees can be done by setting all edges to cost = 0 and using a MST algorithm

### Find Critical and Pseudo-Critical Edges in MST

> Critical edge: An edge that if removed from the graph, would increase the MST weight. (Critical edges appear in every MST)
> Pseudo-Critical edge: An edge that appears only in some MSTs

- Use Kruskal to calculate MST weight
- For each edge:

  - Check if it is critical (calculate MST while ignoring the edge). If weight is higher, the edge is critical.
  - If it is not critical, force the edge. If the weight is same as before, it is pseudo-critical.

  ```python
    class UnionFind:
        def __init__(self, n):
            self.size = [1]*n
            self.parent = list(range(n))

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            px = self.find(x)
            py = self.find(y)
            if px == py:
                return False
            if self.size[px] < self.size[py]:
                px, py = py,px
            self.parent[py] = px
            self.size[px] += self.size[py]
            return True

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [e+[i] for i,e in enumerate(edges)]
        edges.sort(key = lambda x:x[2])
        UF = self.UnionFind(n)
        std_weight = 0
        for u,v,w, _ in edges:
            if UF.union(u,v):
                std_weight += w
        critical = []
        pseudo_critical = []
        for u,v,w,i in edges:
            UF_ignore = self.UnionFind(n)
            ignore_weight = 0
            for x,y,w_ignore, j in edges:
                if i != j and UF_ignore.union(x, y):
                    ignore_weight += w_ignore
            if max(UF_ignore.size) < n or ignore_weight > std_weight:
                critical.append(i)
            else:
                UF_force = self.UnionFind(n)
                force_weight = w
                UF_force.union(u,v)
                for x,y,w_force, j in edges:
                    if i!=j and UF_force.union(x,y):
                        force_weight += w_force
                if force_weight == std_weight:
                    pseudo_critical.append(i)
        return [critical,pseudo_critical]
  ```

### Tarjan's

### Ternary Search

- When the function is not monotonic by but unimodal (there exists only one strict local maximum point m such that f is monotonically increasing for x <= m and monotonically decreasing for x >= m)
- More efficient than binary search for unimodal functions but still O(logn)

```python
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l < r:
            m1 = l + (r-l)//3
            m2 = r - (r-l)//3

            if arr[m1] < arr[m2]:
                l = m1 + 1
            else:
                r = m2 - 1
        return l

    # This can still be solved with binary search
        while l < r:
            mid = l + (r-l)//2
            if arr[mid] < arr[mid+1]:
                l = mid + 1
            else:
                r = mid

        return l
```

### Topological Sort

- Detecting cycles with DFS
- Only exists for Directed Acyclic Graphs (DAG)
- An ordering such that for all edges(u,v) u comes before v

#### Applications

- Find minimum number of vertices to reach all nodes: return all vertices whose indegree = 0

#### Modified DFS

- DFS and add nodes in reverse order (append left with deque)
- 3 color nodes: 0 = not visited, 1 = processing, 2 = processing complete
- If a node is visited during processing (not all of it's neighbors have completed processing), this means there is a cycle

```python
def topsort(self,graph):
	vis = defaultdict(lambda: 0)
	ordering = deque()
	for node in graph.get_vertices():
		self.dfs_topsort(graph, node, vis, ordering)
	return ordering

def dfs_topsort(self, graph, node, vis, ordering):
	if vis[node] == 2:
		return
	if vis[node] == 1:
		raise CycleError
	vis[node] = 1
	for nbor in graph.get_neighbors(node):
		self.dfs_topsort(graph, nbor, vis, ordering)
	ordering.appendleft(node)
	vis[node] = 2
```

#### Kahn's Topological Sort

Find vertices with no incoming edges and removing all outgoing edges from these vertices.

Maintain in-degree information of all graph vertices.
Removing an edge from u to v will decrement `indegree[u]` by 1.

If a cycle exists, then not all vertices will be able to achieve an indegree of 0. If the top_order does not have a length of n, then we must have encountered a cycle.

```python
def topsort(edges, n):
	top_order = deque()
	indegree = [0] * n
	adj_list = [[] for _ in range(n)]
	for u,v in edges:
		adj_list[u].append(v)
		indegree[v] += 1

	# Store all the nodes with no incoming edges
	q = deque([i for i in range(n) if indegree[i] == 0])
	while q:
		# extract front of queue
		u = q.popleft()
		# add the current vertex to the tail of the ordering
		top_order.append(u)
		for v in adj_list[u]:
			indegree[v] -= 1
			if indegree[v] == 0:
				q.append(v)

	if len(top_order) != n:
		print('Cycle Exists')
	return top_order
```

### Collect Coins in a Tree (Topsort)

https://leetcode.com/problems/collect-coins-in-a-tree/

- Collect all coins at a distance of at most 2 from the current vertex
- Move to any adjacent vertex
- Return minimum number of edges needed to go through
- Note: The minimum number of edges is is always 2\*(n_vertices-1) in the pruned tree
- Topsort to remove all leaves with 0 coins
- Remove all leaves
- Remove again all any new leaves that may have been created because we can get coins from two vertices away

```python
def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        if not edges:
            return 0
        leaves = []

        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)

        for u in graph:
            if len(graph[u]) == 1:
                leaves.append(u)

        for u in leaves:
            while len(graph[u]) == 1 and coins[u] == 0:
                v = graph[u].pop()
                del graph[u]
                graph[v].remove(u)
                u = v
        # two iterations since removing a leaf
        # can cause neighboring node to become a leaf
        # remove last leaf with coins
        # then remove it's parent if the parent becomes a leaf node
        # since we can get coins from 2 nodes away
        for _ in range(2):
            leaves = [u for u in graph if len(graph[u]) == 1]
            for u in leaves:
                p = graph[u].pop()
                del graph[u]
                graph[p].remove(u)
                if len(graph)<2:
                    return 0
        # return 2 * number of edges left
        return 2*(len(graph)-1)
```

### Finding Nodes in a Graph with Minimum Height

- Topological Sort then start with queue of leaf nodes (lowest indegree nodes)
- Pop leaf nodes and remove edges from neighbors
- Append neighbor to queue if indegree is 0

##### Simplified Version for Trees

```python
def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        while n > 2:
            n -= len(leaves)
            new_leaves = []

            while leaves:
                leaf = leaves.pop()
                neighbor = graph[leaf].pop()
                # because it's a leaf node, it only has one neighbor
                # otherwise, a loop is needed to remove edges from
                # all it's neighbors
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
```

### Determining Connectivity

- Bfs/dfs/union find

#### Union Find

- Parameters:
  - n: number of of elements
  - parent: array indicating root of component i
    - The value stored here is the index position of the root in the element array, not the actual element itself
  - rank: depth of each component
- Union(x,y) succeeds if x and y are found to have different parents
- Append higher ranked tree to lower ranked tree
- Optimization: Path compression when finding parents
- No operations are performed on the actual elements

```python
class Union_find:
	def __init__(self,n):
		self.n = n
		self.parent = list(range(n))
		self.rank = [1]*n

	#Path compression used to shorten path to parent O(loglogn)
	def find(self,x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	# Union modifies the parent array
	def union(self, x, y):
		px = self.find(x)
		py = self.find(y)

		if px == py:
			return
		# bigger parent stays the parent
		if self.rank[px] == self.rank[py]:gg
			self.parent[px] = pygg
			self.rank[py] += 1
		elif self.rank[px] < self.rank[py]:
			self.parent[px] = py
		else:
			SElf.rank[py] = self.rank[px]
```

##### Union-find Applications

- Cycle detection for undirected graphs only
- Longest consecutive sequence: union consecutive numbers
  - Use index of nums for union-find
  - Keep track of seen numbers
  - Union current current component to existing components

```python
def longest_consecutive_sequence(nums):
	d = {}
	uf = union_find(len(nums))
	for i, num in enumerate(nums):
		if num in d:
			continue
		d[num] = i
		if num-1 in d:
			uf.union(i, d[num-1])
		if num+1 in d:
			uf.union(i, d[num+1])
	return max(uf.size) if nums else 0
```

### Connected Components

- Union Find
- Set all nodes to unvisited
- Start DFS at the next unvisited node
  - Increment decrement components by one, update visited nodes

### Strongly Connected Components

### Bridges Algorithm

### Network Flow: Max Flow Algorithms

### Graph Theory Intuition

## Greedy

## Intervals

1. Sort intervals/pairs in increasing order of the start position.
2. Scan the sorted intervals, and maintain an "active set" for overlapping intervals. At most times, we do not need to use an explicit set to store them. Instead, we just need to maintain several key parameters, e.g. the number of overlapping intervals (count), the minimum ending point among all overlapping intervals (minEnd).
3. If the interval that we are currently checking overlaps with the active set, which can be characterized by cur.start > minEnd, we need to renew those key parameters or change some states.
4. If the current interval does not overlap with the active set, we just drop current active set, record some parameters, and create a new active set that contains the current interval.

> [!note]+ Using Heaps
> Heaps may be helpful in keeping track of interval with earliest end

### Merge Intervals

- Sort by start
- Take the max of each end in the current overlapping interval

```python
 def merge(self, intervals: List[List[int]]) -> List[List[int]]:
	#sort by start
	intervals.sort()
	merged = [intervals[0]]

	for start, end in intervals:
		prev_end = merged[-1][1]
		if start <= prev_end:
			merged[-1][1] = max(end, prev_end)
		else:
			merged.append([start, end])
	return merged
```

### Max Overlapping Intervals

https://leetcode.com/problems/meeting-rooms-ii/description/

- Sort by start
- Keep min heap of ending times in current overlapping range
- Pop one room (replace the meeting that is ending first, with the newest meeting, if it is ending),
  - otherwise a new room is needed

```python
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
	intervals.sort()
	rooms = [intervals[0][1]]

	for start, end in intervals[1:]:
		if start >= rooms[0]:
			heappop(rooms)
		heappush(rooms, end)
	return len(rooms)
```

### Scheduling Max Activities/Maximum Number of Events that can be Attended

https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/

- Sort by end and take the activity with the earliest end time
- Only add activity to the priority queue if day >= start_time
  - Sort by start days
  - Take the activity ending on the earliest day from a pool of activities with the same start day
  - Increment day by one after each activity

```python
def maxEvents(self, events: List[List[int]]) -> int:
	sorted_events = deque(sorted(events))
	pq = []
	res = day = 0

	while sorted_events or pq:
		if not pq:
			day = sorted_events[0][0]
		while sorted_events and sorted_events[0][0] == day:
			heappush(pq, sorted_events.popleft()[1])
		heappop(pq)
		res += 1
		day += 1
		while pq and pq[0]<day:
			heappop(pq)
	return res
```

## Hashing

## Heaps

### Top K

#### Top K Frequent Elements

## Linked List

### Cycle Detection

- Floyd's Algorithm (Tortoise and Hare) to find start of cycle
- Hare initially travels twice as fast a Tortoise
- Stop at meeting point
- Reset tortoise to starting position while hare stays at meeting point. Move both until at same speed until they meet again (at the entrance of the cycle) 

### Deletion node (Recursive/Iterative)

### Reverse Linked List

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
	prev, cur = None, head
	while cur:
		next_tmp = cur.next
		cur.next = prev
		prev = cur
		cur = next_tmp
	return prev
```

### Insert Into a Sorted Circular Linked List

- Step 1: Enumerate all cases (how can the node be inserted)
  - At the tail, in the middle

```python
def insert(self, head: 'Node', insertVal: int) -> 'Node':
	if head == None:
		newNode = Node(insertVal, None)
		newNode.next = newNode
		return newNode

	node = head
	while(node.next != head):
		if node.val <= node.next.val:
			if insertVal >= node.val and insertVal <= node.next.val:
				break
		else:
			if insertVal >= node.val or insertVal <= node.next.val:
				break
		node = node.next

	node.next = Node(insertVal, node.next)
	return head
```

### Reverse Nodes in k-Group

https://leetcode.com/problems/reverse-nodes-in-k-group/description/

- Reverse k nodes at a time
- Count number of k groups first
  - Store the ptr for the last node of group 1
  - This is used to set the next node for the last node of the first group (original root), so that the linked list doesn't break after the first group
- Keep a ptr for the previous node of the group
- Reverse k nodes
  - Point the previous of the group at the head of the k reversed nodes
  - Point the last node of the current group to the saved tmp(cur.next)

```python
def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
	cur = head
	groups = 0
	c = 0
	first_k = None
	# Find number of groups of size k
	while cur:
		c += 1
		if c == k:
			c = 0
			groups += 1
			if not first_k:
				first_k = cur.next

		cur = cur.next

	cur = head
	dummy =ListNode()
	group_prev = dummy
	prev = first_k

	while groups > 0:
		c = k
		last_node = cur
		while c > 0:
			tmp = cur.next
			cur.next = prev
			prev = cur
			cur = tmp
			c -= 1
		groups -= 1

		group_prev.next = prev
		group_prev = last_node
		last_node.next = tmp
		cur = tmp
	return dummy.next
```

## Hungarian Algorithm
- For solving the assignment problem
- Also known as Kuhn-Mankres Algorithm
### Assignment Problem Statement
- There are n jobs and n workers. Each worker can be assigned to only one job. Assign jobs to workers in a way that minimizes total cost.
- Given n x n matrix: Select one number from each row such that exactly one number is chosen from each column and the sum of the selected numbers is minimized.
- Given n x n matrix A:  Find permutation p of length n such that $\sum A[i][p[i]]$ is minimized
- Consider a complete bipartite graph with n vertices per part, where each edge is assigned a weight. Find a perfect matching with the minimum total weight
To modify for n x m matrix, pad with rows/columns with zero or infinite values.

### $O(n^4)$ Implementation
i

## Queue

### Circular Queue

## Sliding Window

- Sliding Window works on the assumption window only grows in one direction. -> Only works for positive numbers
- If negative numbers (window is bidirectional), try hashmap or DP

### Sliding Window Grouping

- Sliding window is useful when you require looking at fixed size groups
  https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/description/

#### Minimum Swaps to Group All 1's Together

- Sliding window of size k

```python
 def minSwaps(self, data: List[int]) -> int:
        zeros = sum(data)
        if not zeros:
            return 0
        res = math.inf
        cur = 0
        for j in range(len(data)):
            cur += data[j]
            if j >= zeros-1:
                res = min(res, zeros-cur)
                cur -= data[j-(zeros-1)]
        return res
```

## Sorts

### Cycle Sort

### Bucket/Count Sort

- Non-comparison stable sorting algorithm
- Stableness is only guaranteed if we iterate the unsorted array backwards
- Store freq of each element in `count`
- Store cumulative sum of elements from `count`
- Find index of each element of original array.
- Place it in the correct position and decrease its count by one
- Some modification needed if range includes negative numbers
- Separate pos and neg and do count sort on each, negate negative signs, build cumulative sum in reverse

```python
def countSort(self, arr: List[int]) -> List[int]:
  min_v = min(arr)
  max_v = max(arr)
  n = max_v - min_v + 1
  count = [0] * (n)
  size = len(arr)
  ans = [0]*size
  # Store count of every elem
  for i in range(size):
    count[arr[i]-min_v] += 1
  # Store cumulative count
  for i in range(1, n):
    count[i] += count[i-1]

  # Find index of each element of original array in count array
  for i in range(len(arr)-1, -1, -1):
    # cumulative sum stores the amount of numbers <= current number
    ans[count[arr[i]]-1] = arr[i]
    count[arr[i]] -= 1
  return ans
```

- Count sort can b used to find the kth greatest element in an array
- Iterate backwards in cumulative sum array (count) for k decrements

### Cyclic Sort

- Cycle decomposition
- Sort that results in the least memory operations/swaps
- Unstable because of swaps

```python
def cyclic_sort(nums):
  for i in range(len(nums)):
    while nums[i] != i:
      correct_ind = nums[i]
      nums[i], nums[correct_ind] = nums[correct_ind], nums[i]

# To find minimum swaps in an arbitrary array
def cyclic_sort(arr):
    pos = {x:i for i,x in enumerate(sorted(arr))}
    swaps = 0
    for i in range(len(arr)):
        while i != pos[arr[i]]:
      # This line is crucial for the actual swap to work
      # Index must be stored since arr[i] is being modified
            ind = pos[arr[i]]
            arr[i], arr[ind] = arr[ind], arr[i]
            swaps += 1
    return swaps

```

### Quick Sort

### Quick Select

> Repeatedly partition about half the remaining relevant array until pivot index = k-1

- not stable because of swaps

- kth-largest = qselect(arr, 0, len(arr)-1, len(arr)-k)
  - Alternatively: heappush first k elements, then heappop and heappush nums[i] if nums[i] > pq[0]
  - (keep k largest elements on heap)
- kth-smallest = qselect(arr, 0, len(arr)-1, k-1)

```python
def qselect(self, arr: List[int], left: int, right: int, k: int) -> int:
  p = partition(arr, l, r)
  if p < k:
    return qselect(arr, p+1, r, k)
  if p > k:
    return qselect(arr, l, p-1, k)
  return arr[p]

# Std partition process for Quick Sort
# i = ind of first element greater than pivot
def partition(arr,l,r):
  # can be randomly picked or using median of medians, the worst case can be improved to O(n) with a large constant
  pivot = arr[r]
  i = l
  for j in range(l, r):
    if arr[j] <= pivot:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
  arr[i], arr[r] = arr[r], arr[i]
  return i
```

## Stacks/Monotonic Stacks

> Mono Increasing:
> `while stack and (i == n or arr[i] <) `

- Figure out if a larger or smaller `arr[i]` will invalidate the current sum
- If larger element invalidates stack:
  - mono dec. stack
- else:
  - mono inc. stack

### Monotonically Increasing Stack

- The area of the rectangle with height at `stack[-1]` cannot grow if the current bar is smaller
  - Thus, a mono. increasing stack is required

#### Largest Rectangle in Histogram

https://leetcode.com/problems/largest-rectangle-in-histogram/description/

- Trick: Append index -1 to the start of the stack for the left border of the 0th bar

```python
 def largestRectangleArea(self, heights: List[int]) -> int:
	stack = [-1]
	area = 0
	n = len(heights)
	# monotonically increasing stack
	for i in range(n+1):
		# when the stack is empty (left boundary is -1), this means that every previous
		# bar was taller than this one
		while stack[-1] != -1 and (i == n or heights[i] <= heights[stack[-1]]):
			# height of the last bar in the stack
			h = heights[stack.pop()]
			# stack[-1] is the left boundary, the next highest bar in the stack
			# before the bar with height = h
			w = i-stack[-1] - 1
			area = max(area, h*w)
		if i < n:
			stack.append(i)
	return area
```

### Monotonically Decreasing Stack

#### Sliding Window Maximum

- Mono dec. stack while invalidating the max
- Invalidate the max (which is at `q[0]`) if it is not within the k sized window
- Invalidate elements on the stack smaller than the current element (since they will never be used)

```python
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
	q = deque([])

	# what would invalidate the ans
	# the maximum value is out of range
	# if the current number is not the max,
	# it will never be used
	i = 0
	n = len(nums)
	ans = []

	for i in range(k-1):
		while q and nums[i] > nums[q[-1]]:
			q.pop()
		q.append(i)
	for i in range(k-1, n):
		# invalidate stack
		while q and nums[i] > nums[q[-1]]:
			q.pop()
		while q and i-k >= q[0]:
			q.popleft()
		q.append(i)
		ans.append(nums[q[0]])
	return ans
```

#### Number of Subarrays where Boundary Elements are Maximum

https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

- Stack is invalidated if a greater element is encountered

```python
def numberOfSubarrays(self, nums: List[int]) -> int:
	ans = 0
	stack = []
	n = len(nums)
	d = defaultdict(int)
	for i in range(n):
		while stack and nums[i] > nums[stack[-1]]:
			d[nums[stack[-1]]] -= 1
			stack.pop()
		ans += d[nums[i]]
		stack.append(i)
		d[nums[i]] += 1
	return ans + n
```

## String

### Pattern Matching

#### Maximal Boundaries

- Maximal boundary is longest prefix that is also a suffix
- F is an array of maximal boundaries for every substring `s[0:i] for i in range(len(s))`

```python
def maximum_border_length(w):
	n = len(w)
	f = [0] * n # init f[0] = 0
	k = 0 # current longest border length
	for i in range(1, n): # compute f[i]
		while w[k] != w[i] and k > 0:
			k = f[k - 1] # mismatch: try the next border
		if w[k] == w[i]: # last characters match
			k += 1 # we can increment the border length
			f[i] = k # we found the maximal border of w[:i + 1]
	return f
```

#### KMP

- Search t in s

```python
def KMP(s, t):
	w = t + "#" + s
	n = len(t)
	f = [0] * n # init f[0] = 0
	k = 0 # current longest border length
	for i in range(1, len(w)): # compute f[i]
		while w[k] != w[i] and k > 0:
			k = f[k - 1] # mismatch: try the next border
		if w[k] == w[i]: # last characters match
			k += 1 # we can increment the border length
			f[i] = k # we found the maximal border of w[:i + 1]
			if f[i] == n:
				return i - 2*n #2n accounts for the searched word, -1 omitted for the separator used
	return f
```

Space/Time Complexity: O(m + n)
##### Searching for All Occurrences
https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/
- Don't return after once match
### Isomorphic Strings (Mapping)

```python
def isIsomorphic(self, s: str, t: str) -> bool:
	map_s = {}
	map_t = {}
	for c1, c2 in zip(s,t):
		if c1 not in map_s and c2 not in map_t:
			map_s[c1] = c2
			map_t[c2] = c1
		elif map_s.get(c1) != c2 or map_t.get(c2) != c1:
			return False
	return True
```

## Sweep Line

## Trie

- Ex: `trie = {c: {a: {t:{WORD_KEY: 'cat' }}}}`
- An alternative to class objects can be to set
  - `nodes[WORD_KEY] = word` to indicate a word

```python

def trieDictionary(words):
	trie = {}
	for w in words:
		node = trie
		for ch in w:
			node = node.setdefault(ch,{})

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.nodes = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Inserts a word into the trie.
    def insert(self, word: str) -> None:
        cur = self.root;

        for c in word:
            if c not in cur.nodes:
                cur.nodes[c] = TrieNode()
            cur = cur.nodes[c]

        cur.isWord = True;

    # Returns if the word is in the trie
    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]

        return cur.isWord
    # Returns if there is any word in the trie
    # that starts with the given prefix. */
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.nodes:
                return False
            cur = cur.nodes[c]

        return True
```

### Suffix Array/Tree

## Two Pointers

- Usually requires the array to be sorted
- We need some comparison function

- Common questions: count the number of pairs such that f() is true
- Make sure to always rearrange/substitute terms in f()

### Count Pairs in Two Arrays

https://leetcode.com/problems/count-pairs-in-two-arrays/description/

- Question gives: `nums1[i] + nums1[j] > nums2[i] + nums2[j]`
- Intuition: Reorganize terms so that i and j are on the same side -> `nums1[i] - nums2[i] > nums2[j] - nums1[j]`
- We also recognize that -LHS = RHS, therefore the largest RHS would be at the smallest LHS
- Sort a new array of LHS
- Let i = index of -RHS term = 0
- Let j = index of largest LHS term = 0
- We want to start at the largest RHS term and largest LHS term, then we can take all pairs in between

```python
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        a = [nums1[i] - nums2[i] for i in range(n)]
        a.sort()
        ans = 0
        i = 0
        j = n-1
        while i < j:
            if a[j] > -a[i]:
                ans += j-i
                j -= 1
            else:
                i += 1
        return an
```

## Python

- reverse a substring = `word[:i+1][::-1]`

- Sorting dictionary

```python
# Suppose we have a dictionary
{'A': [1, 0, 0, 'A'], 'B': [0, -2, 0, 'B'], 'C': [0, 0, 0, 'C']}

# Even though each list has nums and strings, we can sort using
sorted(d.key(),key=d.get)
# This returns the keys in sorted order and uses the last letter as alphabetical tie breaker

```

- Comparing min/max of two arrays with different lengths
  - Loop range of max(lenA, lenB)
  - Set comparison value to some default if past the max ind

```python
  for i in range(max(n1, n2)):
            i1 = int(v1[i]) if i < n1 else 0
            i2 = int(v2[i]) if i < n2 else
```

## Math

### Arithmetic Sequence Sum
$sum = (A[1] + A[n]) * n/2$ where `A[1], A[n]` are the first and last terms of the sequence and `n` is the length of the sequence

#### Minimum Possible Sum of Array with n distinct positive integers such that no two integers sum to Target
https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/description/
- The only possible integers that break this rule are numbers less than target
- We can take at most target//2 integers
```python
def minimumPossibleSum(self, n: int, target: int) -> int:
	x = target//2
	if n < x:
		return (1+n)*n//2%(10**9+7)
	total = (1+x)*x//2
	n -= x
	return (total+(target+target+n-1)*n//2) % (10**9+7)
```

### GCD for a List of Numbers

Basic Euclidean Algorithm for GCD:

The algorithm is based on the below facts.

    If we subtract a smaller number from a larger one (we reduce a larger number), GCD doesn’t change. So if we keep subtracting repeatedly the larger of two, we end up with GCD.
    Now instead of subtraction, if we divide the smaller number, the algorithm stops when we find the remainder 0.

gcd(a, b, c) = gcd(a, gcd(b, c))
= gcd(gcd(a, b), c)
= gcd(gcd(a, c), b)

```python
# Euclidean algorithm to find H.C.F of two numbers
# Time complexity of O(log min(x,y)) since larger number is reduced by at least half on each iteration of the algorithm
def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
 
# Some arbitrary list of numbers
l = [2, 4, 6, 8, 16]

num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1, num2)

for i in range(2, len(l)):
    gcd = find_gcd(gcd, l[i])

print(gcd)
```

### LCM
```python
def lcm(x,y):
	return x / gcd(x,y) * y  # divide first to avoid integer overflow
```

### Binary Exponentiation 
- Exponentiation by squaring allows calculating $a^n$ with only $O(logn)$ multiplications instead of $O(n)$ multiplications required by the naive approach
- Split the work using binary representation of the exponent
#### Number of Paths of Length k in a Graph

### Sieve of Eratosthenes

```python
def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

def PrimePairsWithTargetSum(n):
    for p in range(2, n+1):
      if prime[i] and prime[n-i] and i<= n-i:
        res.append([i,n-i])
```

### Matrix Exponentiation

https://www.geeksforgeeks.org/top-algorithms-and-data-structures-for-competitive-programming/
https://www.geeksforgeeks.org/matrix-exponentiation/

#### Misc

- To check if a number is a palindrome without string conversion:
- Use reverse number
- To get the first digit of a number, we can also do x // 10\*\*int(log10(x))

```python
def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x != 0):
            return False
        reverseX = 0
        y = x
        while y:
            reverseX = reverseX * 10 + y%10
            y //= 10

        # reverse can contain the middle number
        return reverseX == x or x == reverseX//1
```

### Absolute Value Rules

|–a| = |a|
|a| ≥ 0.
Products: |ab| = |a||b|
Quotients: |a / b| = |a| / |b|
Powers: |an| = |a|n
Triangle Inequality: |a + b| ≤ |a| + |b|

### Multiplication Tricks

#### By 11

- ab x 11 = 100a + 10(a+b) + b
- extrapolate for every adjacent pair in abc...z

#### ab x ac with 10 = b + c

- ans: (a x (a+1)) concat (b x c)
- 34 x 36 = 1224

#### Difference of squares: bc x de where d = b+1 and e = 10-c

- bc+e is the number between bc and de which is divisible by 10
- 13 x 27 = (bc+e)^2 - e^2

#### x^2

- x^2 = a x b + c^2
- where a = x+c and b = x-c
- 108^2 = 116 x 100 + 8^2

#### By 5

- Let x = a5 and y = b5
- If a + b is even: z = ab+(a+b)/2, xy = z25
- If a + b is odd: z = ab+(a+b)/2, xy = integer(z)25
- 15 x 25 = 375
- 45 x 125 = 5625

#### Other Tips

- Multiplying by 4 for a large number is equivalent to multiplying it by 2, twice

#### Division with fractions

- 374/25 = 374x2x2 / 100

#### Subtracting without borrowing

- Subtract pairs of digits instead of one to avoid borrowing

#### Fun fact: The remained of an integer n divided by 9 is the same as the sum of the digits of n mod 9

- This does not prove that the answer is correct however

### Principle of Inclusion and Exclusion

- |A ∪ B| = |A| + |B|−|A ∩ B| and |A ∪ B ∪ C| = |A| + |B| + |C|−|A ∩ B|−|A ∩ C|−|B ∩ C| + |A ∩ B ∩ C|.
- Add all intersections with odd size, subtract all intersections with even size
- Building a sequence of multiples for some set of nums
- Divide products of pairs by their gcd

```python
  ab = a*b//gcd(a, b)
  bc = b*c//gcd(b, c)
  ca = c*a//gcd(c, a)
  abc = ab*c//gcd(ab, c)
```

# Advanced

- Indexed priority queue

## Counting

### Greedy Counting

##### Maximum Alternating Elements

> Decrement 1 from a different element each loop. How many iterations is possible?
> https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/description/

- Wrong approach: use heap and take the two biggest and decrement by smaller number
- Consider `[100,100,100]`. Answer is 300 but using the above approach gives 201
- Intuition: We should match smaller numbers with the biggest
- If the biggest number is larger than the sum of all other numbers, we can only decrement rest \* 2 + 1
- If it is smaller or equal to the rest, we can always match a smaller element to it and decrement everything

### Two Sum

- Always check constraints

#### Count Pairs that Sum to a Power of 2

- 0 is not a power of 2...
- Since there is a constraint on `arr[i]` <= 2\*\*20, we only need to check 21 powers of 2
- For every power, for every x, check if the complement (p-x) is in the hash map
- Edge case: x == p/2, instead of `d[x] * d[p-x]`, increment by `d[x]` choose 2

## Combinatorics

### Stars and Bars
- Count the number of ways to group n identical objects into k groups
	- $x_1 + x_2 + ... + x_k = n$
- Sol: ${n+k-1}\choose{n}$
#### Ex: Number of Positive Integer Sums
- $x_1 + x_2 + ... + x_k = n$, with $x_i >= 1$
- Sol: $n-1 \choose k-1$
- Prevent two bars from being placed next to each other. n-1 is the number of gaps between stars
#### Number of Lower-bound Integer Sums
- Extended to integer sums with different lower bounds
- $x_1 + x_2 + ... + x_k = n$, with $x_i >= a_i$
- Substitute $x'_i := x_i -a_i$ 
- $(x'_1 + a_i)+(x'_2 + a_2) + ... + (x'_k + a_k)\iff x'_1 + x'_2 + ... + x'_k = n-a_1 -a_2-...-a_k$ with $x_i >= 0$

## Miscellaneous

### Boyer-Moore Voting Algorithm

- There can be at most k-1 majority elements which appear more than n//(k) in an array
- Keep count of candidates, increment if seen
- Decrement all candidates if current number is not any of the candidates
- Once count of any candidate is 0 (check from most likely candidate to least likely candidate), set the candidate to the current number and increment
- Do a second pass and count all candidates to check if they appear more than n//(k) times

```python
def majorityElement(self, nums: List[int]) -> List[int]:
        # 1st pass
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        # 2nd pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums)//3:
                result.append(c)

        return result
```

# Behavioural

https://www.techinterviewhandbook.org/behavioral-interview/

---
title:  "Bit Manipulation"
created: 2023-01-04
---
# Bit Manipulation

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
n & 1 << i

#Flip ith bit
n ^ 1 << i 

#Clear ith bit
n & ~(1 << i)

#Check if number is divisible by 2 to the power of k
n & (1<<k-1) == 0

#Check if an integer is a power of 2
n and not (n & (n-1))

#Clear the right-most set bit
n & (n-1)
This works because n-1 flips all bits after the rightmost set bit of n

#Clear all trailing ones
n & (n+1)

#Set the last cleared bit
n | (n+1)

#Extract last set bit
n & -n

#Isolate rightmost 1-bit and set all others bits to 0
n & (-n) 

```

### [Shortest Subarray With OR at Least K II](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/)
:::tip[tip] 

A hash map is required to store the count of bits when working with prefixes or previous states.

:::
- Sliding window + bit count
```python
def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
	cnt = [0]*30
	cur = i = 0
	res = math.inf
	if max(nums)>=k:
		return 1
	for j,x in enumerate(nums):
		for b in range(30):
			if 1<<b&nums[j]:
				if not cnt[b]:
					cur += 1<<b
				cnt[b] += 1

		while i <= j and cur >= k:
			for b in range(30):
				if 1 << b & nums[i]:
					cnt[b] -= 1
					if not cnt[b]:
						cur -= 1<<b
			res = min(res, j-i+1)
			i += 1
		
	return res if res != math.inf else -1
```

### Keeping Track of Numbers + Splitting Them Into Groups 
- Find the two numbers that occur only once in an array of numbers that occur twice
- If a number occurs twice, the XOR of both of them is 0
- Use a mask to first get the XOR of the two missing numbers
- To separate them, we need a second XOR mask that has the rightmost bit of the first mask set to 1. 
```python
def singleNumber(self, nums: int) -> List[int]:
        # difference between two numbers (x and y) which were seen only once
        bitmask = 0
        for num in nums:
            bitmask ^= num
        
        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)
        
        x = 0
        for num in nums:
            # bitmask which will contain only x
            if num & diff:
                x ^= num
        
        return [x, bitmask^x]
                
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

### AND + XOR Distributive Property
https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/solutions/1163992/java-c-python-easy-and-concise-o-1-space/
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


https://leetcode.com/problems/find-the-k-th-lucky-number/?envType=weekly-question&envId=2024-05-29
=======
### Bit Operation Properties
```python
a^b is equivalent to subtracting b from a
a^b == 0 if and  only if a == b
```

>>>>>>> 5a71c508d3099d93f3f323e8771832c0fd64195d
# Related
https://leetcode.com/problems/sum-of-two-integers/solutions/84278/A-summary:-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently/

https://leetcode.com/problems/sum-of-two-integers/solutions/678639/sum-of-two-integers/

https://leetcode.com/problems/single-number/description/
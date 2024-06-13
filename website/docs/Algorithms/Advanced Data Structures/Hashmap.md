---
title:  "Hashmaps"
created: 2022-12-10
---

---
title:  "Hashmap"
tags:

created: 2023-01-06
---




# Hashmap

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


# Hashmap
- Note that a hash table is slightly different than a hash map. A hash table is a structure for storing arbitrary data not necessarily consisting of a separate key and value. A hashmap is a particular type of hashtable which has distinct keys and values

## Load Factor
$\alpha$ = # of (key/value) pairs / Size of Hash Table

## Why should we choose $m$ to be a prime number as the modulo of the hash value? 
Consider the set of keys 𝐾={0,1,...,100}K={0,1,...,100} and a hash table where the number of buckets is 𝑚=12m=12. Since 33 is a factor of 1212, the keys that are multiples of 33 will be hashed to buckets that are multiples of 33:

-   Keys {0,12,24,36,...}{0,12,24,36,...} will be hashed to bucket 00.
-   Keys {3,15,27,39,...}{3,15,27,39,...} will be hashed to bucket 33.
-   Keys {6,18,30,42,...}{6,18,30,42,...} will be hashed to bucket 66.
-   Keys {9,21,33,45,...}{9,21,33,45,...} will be hashed to bucket 99.

If 𝐾K is uniformly distributed (i.e., every key in 𝐾K is equally likely to occur), then the choice of 𝑚m is not so critical. But, what happens if 𝐾K is not uniformly distributed? Imagine that the keys that are most likely to occur are the multiples of 33. In this case, all of the buckets that are not multiples of 33 will be empty with high probability (which is really bad in terms of hash table performance).

This situation is more common that it may seem. Imagine, for instance, that you are keeping track of objects based on where they are stored in memory. If your computer's word size is four bytes, then you will be hashing keys that are multiples of 4. Needless to say that choosing 𝑚 to be a multiple of 4 would be a terrible choice: you would have 3𝑚/4 buckets completely empty, and all of your keys colliding in the remaining 𝑚/4 buckets.

In general:

> Every key in 𝐾K that shares a common factor with the number of buckets 𝑚m will be hashed to a bucket that is a multiple of this factor.

Therefore, to minimize collisions, it is important to reduce the number of common factors between 𝑚 and the elements of 𝐾. How can this be achieved? By choosing 𝑚m to be a number that has very few factors: a **prime number**.

Reference: https://cs.stackexchange.com/questions/11029/why-is-it-best-to-use-a-prime-number-as-a-mod-in-a-hashing-function
# Collision Resolution
## Separate Chaining: 
- Common data structures used to implement chaining include: linked list, arrays, binary trees, self balancing trees, etc
- Disadvantage is that a lot of memory used to build linked lists could have just been to increase the table size
:::question[question] 

**How do you maintain O(1) insertion and lookup time complexity once the hashmap gets really full and linked list chains are long?** 

Sol: Create new hashmap with larger capacitiy and rehash all the items inside the old hashmap 

:::


## Open Addressing
- If cell is occupied, use **************************sequential probing************************** to find next available cell
- Searching for an item no requires additional checking
- Deletion requires reinsertion of all items after the hole
- The O(1) constant time behaviour attributed to hash tables assumes the load factor ($\alpha$) is kept below a certain fixed value. This means once $\alpha$ > threshold, we need to grow the table size (ideally exponentially, e.g. double)
### Linear Probing
$P(x) = ax + b$
- where a, b are constants
### Quadratic probing
$P(x) = ax^2 + bx + c$
- where a, b,c are constants
### Double Hashing
$P(k,x) = x*H_2(k)$ 
- where $H_2(k)$ is a secondary hash function
### Pseudo Random Number Generator
$P(k,x) = x*RNG(H(k),x)$ 
- where RNG is a random number generator seeded with $H(k)$

## Chaos with cycles
- Most randomly selected probing sequences modulo N will produce a cycle shorter than the table size
- This becomes problematic when you are trying to insert a key-value pair and all the buckets on the cycle are occupied because you will get stuck in an infinite loop
- Sol: Avoid this by restricting our domain of probing functions to those which produce a cycle of exactly length $N$ 
# Hashtable + Open Addressing Implementation
```python
def HashMap:
	def __init__(self, N):
		self.key_space = 2069
		self.hash_table = [None] * N

	def probing_func(x):
		return (3*x + 5) % self.key_space

	def hash_func(key):
		return key % self.key_space

	def insert(self, key, val):
		x = 1
		key_hash = self.hash_func(key)
		index = key_hash

		while hash_table[index] != null:
			index = (key_hash + self.probing_func(x)) % N
			x += 1
		sel.hash_table[index] = (key, val)

	def 

```
# Hashtable + Separate Chaining Implementation

```python

class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for k,v in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket.pop(i)
        

class MyHashMap:
    def __init__(self):
        # choose a prime
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]

    def insert(self, key: int, value: int) -> None:
        hash_key = self.get_hash(key)
        self.hash_table[hash_key].update(key,value)

    def get(self, key: int) -> int:
        hash_key = self.get_hash(key)
        return self.hash_table[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = self.get_hash(key)
        self.hash_table[hash_key].remove(key)

    def get_hash(self, key):
        return key % self.key_space


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```

## Optimizations

## Optimized Complexity

:::Time-Complexity[Time Complexity] 


:::

:::Space-Complexity[Space Complexity] 


:::


# Related

[LC-706. Design HashMap](</docs/Some Leetcode Questions/LC-706. Design HashMap.md>)- https://runestone.academy/ns/books/published/pythonds/SortSearch/Hashing.html
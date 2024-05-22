---
title:  "LFU Cache"
created: 2023-01-06
---

# LFU Cache
Design and implement a data structure for a [Least Frequently Used (LFU)](https://en.wikipedia.org/wiki/Least_frequently_used) cache.

Implement the `LFUCache` class:

-   `LFUCache(int capacity)` Initializes the object with the `capacity` of the data structure.
-   `int get(int key)` Gets the value of the `key` if the `key` exists in the cache. Otherwise, returns `-1`.
-   `void put(int key, int value)` Update the value of the `key` if present, or inserts the `key` if not already present. When the cache reaches its `capacity`, it should invalidate and remove the **least frequently used** key before inserting a new item. For this problem, when there is a **tie** (i.e., two or more keys with the same frequency), the **least recently used** `key` would be invalidated.

To determine the least frequently used key, a **use counter** is maintained for each key in the cache. The key with the smallest **use counter** is the least frequently used key.

When a key is first inserted into the cache, its **use counter** is set to `1` (due to the `put` operation). The **use counter** for a key in the cache is incremented either a `get` or `put` operation is called on it.

The functions `get` and `put` must each run in `O(1)`average time complexity.

**Example 1:**

**Input**
``["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
``[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
**Output**
``[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

**Explanation**
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=``[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=``[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=``[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=``[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=``[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=``[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=``[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=``[4,3], cnt(4)=2, cnt(3)=3

**Constraints:**

-   `0 <= capacity <= 104`
-   `0 <= key <= 105`
-   `0 <= value <= 109`
-   At most `2 * 105` calls will be made to `get` and `put`.
# Implementation (Maintaining 2 Hash Maps)
#### Intuition

We need to maintain all the keys, values and frequencies. Without invalidation (removing from the data structure when it reaches capacity), they can be maintained by a HashMap<Integer, Pair<Integer, Integer>>, keyed by the original `key` and valued by the `frequency`-`value` pair.

With the invalidation, we need to maintain the current minimum frequency and delete particular keys. Hence, we can group the keys with the same frequency together and maintain another HashMap<Integer, Set>, keyed by the frequency and valued by the set of `keys` that have the same frequency. This way, if we know the minimum frequency, we can access the potential keys to be deleted.

Also note that in the case of a tie, we're required to find the least recently used key and invalidate it, hence we need to keep the frequencies ordered in the Set. Instead of using a TreeSet which adds an extra O(log(N))O(log(N))O(log(N)) time complexity, we can maintain the keys using a LinkedList so that it supports finding both an arbitrary key and the least recently used key in constant time. Fortunately, LinkedHashSet can do the job. Once a `key` is inserted/updated, we put it to the end of the LinkedHashSet so that we can invalidate the first `key` in the LinkedHashSet corresponding to the minimum frequency.

The original operations can be transformed into operations on the 2 HashMaps, keeping them in sync and maintaining the minimum frequency.

Since C++ lacks LinkedHashSet, we have to use a workaround like maintaining a list of key and value pairs instead of the LinkedHashSet and keeping the iterator with the frequency in another unordered_map to keep this connection. The idea is similar but a little bit complicated. Another workaround would be to implement your own LRU cache with a doubly linked list.

#### Algorithm

To make things simpler, assume we have 4 member variables:

1.  `HashMap<Integer, Pair<Integer, Integer>> cache`, keyed by the original `key` and valued by the `frequency`-`value` pair.
2.  `HashMap<Integer, LinkedListHashSet<Integer>> frequencies`, keyed by frequency and valued by the set of `keys` that have the same frequency.
3.  `int minf`, which is the minimum frequency at any given time.
4.  `int capacity`, which is the `capacity` given in the input.

It's also convenient to have a private utility function `insert` to insert a `key`-`value` pair with a given frequency.

##### void insert(int key, int frequency, int value)

1.  Insert `frequency`-`value` pair into `cache` with the given `key`.
2.  Get the LinkedHashSet corresponding to the given `frequency` (default to empty Set) and insert the given `key`.

##### int get(int key)

1.  If the given `key` is not in the `cache`, return `-1`, otherwise go to step `2`.
2.  Get the `frequency` and `value` from the `cache`.
3.  Get the LinkedHashSet associated with `frequency` from `frequencies` and remove the given `key` from it, since the usage of the current key is increased by this function call.
4.  If `minf` == `frequency` and the above LinkedHashSet is empty, that means there are no more elements used `minf` times, so increase `minf` by 1.
5.  Call insert(`key`, `frequency` + 1, `value`), since the current key's usage has increased from this function call.
6.  Return `value`

##### void put(int key, int value)

1.  If `capacity` <= 0, exit.
2.  If the given `key` exists in `cache`, update the `value` in the original `frequency`-`value`(don't call insert here), and then increment the frequency by using get(`key`). Exit the function.
3.  If `cache.size()` == `capacity`, get the first (least recently used) value in the LinkedHashSet corresponding to `minf` in `frequencies`, and remove it from `cache` and the LinkedHashSet.
4.  If we didn't exit the function in step 2, it means that this element is a new one, so the minimum frequency cannot possibly be greater than one. Set `minf` to 1.
5.  Call insert(`key`, 1, `value`)
```python

```

## Optimizations

## Optimized Complexity

:::Time-Complexity[Time Complexity] 


:::

:::Space-Complexity[Space Complexity] 


:::



# Related
[LRU Cache](</docs/DS/LRU Cache.md>)
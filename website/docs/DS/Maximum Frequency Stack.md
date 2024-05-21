---
title:  "Maximum Frequency Stack"
created: 2023-01-24
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Maximum Frequency Stack
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the `FreqStack` class:

-   `FreqStack()` constructs an empty frequency stack.
-   `void push(int val)` pushes an integer `val` onto the top of the stack.
-   `int pop()` removes and returns the most frequent element in the stack.
    -   If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

**Example 1:**

**Input**
``["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
``[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
**Output**
``[null, null, null, null, null, null, null, 5, 7, 5, 4]

**Explanation**
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
# Implementation

Stack of Stacks + maintain frequency of every number + counter for max_freq
- Map freq to stack of elements. Update max_freq and frequency of every number accordingly during push/pop


```python
class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)
        self.maxfreq = 0
        
    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(val)
        

    def pop(self) -> int:
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return x
```

## Optimizations

## Optimized Complexity

-   Time Complexity:  O(1)O(1)O(1) for both `push` and `pop` operations.
    
-   Space Complexity:  O(N)O(N)O(N), where `N` is the number of elements in the `FreqStack`.


# Related
lc-hard: https://leetcode.com/problems/maximum-frequency-stack/
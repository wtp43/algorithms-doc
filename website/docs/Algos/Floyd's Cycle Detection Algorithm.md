---
title:  "Floyd's Cycle Detection Algorithm"
created: 2023-02-02
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Floyd's Cycle Detection Algorithm

# Implementation
```python
def detectLoop(head):
    slowPointer = head
    fastPointer = head
 
    while (slowPointer 
           and fastPointer 
           and fastPointer.next):
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        if (slowPointer == fastPointer):
            return 1
    return 0
```

# Finding where the Cycle Starts
X = Distance between the head(starting) to the loop starting point.

Y = Distance between the loop starting point and the first meeting point of both the pointers.

C = The distance of the loop

Before the two pointers meet.
The slow pointer has traveled $X + Y + s * C$ distance, where s is any positive constant number.
The fast pointer has traveled $X + Y + f * C$ distance, where f is any positive constant number.


Since the fast pointer is moving twice as fast as the slow pointer, we can say that the fast pointer covered twice the distance the slow pointer covered. Therefore:

$X + Y + f * C = 2(X + Y + s*c)$
$(f - 2c) * C = X + Y$

Thus:
$X = K * C - Y$ 

Now if reset the slow pointer to the head(starting position) and move both fast and slow pointer by one unit at a time, one can observe from 1st and 2nd equation that both of them will meet after traveling X distance at the starting of the loop because after resetting the slow pointer and moving it X distance, at the same time from the loop meeting point the fast pointer will also travel K * C – Y distance(because it already has traveled Y distance).
The next meeting point will be the start of the cycle.

```python
# reset slow pointer to head and traverse again
        slowPointer = head;
        while (slowPointer != fastPointer): 
            slowPointer = slowPointer.next;
            fastPointer = fastPointer.next;
		return slowPointer
```

# Related

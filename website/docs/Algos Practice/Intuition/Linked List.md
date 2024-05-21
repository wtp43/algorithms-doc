---
---
Linked List

- [ ] [[LC-206. Reverse Linked List]]
- The 3 components we need are prev, cur, and tmp. We need to store the next link because it is being updated.

- [ ] [[LC-234. Palindrome Linked List]] 

- Fast slow pointer to find the middle of the linked list
- Reverse the 2nd half of the linked list

- [ ] [[LC-138. Copy List with Random Pointer]]
- Make all the new nodes first and store them in a dictionary
- Traverse the original linked list and set the corresponding links using the dictionary on the new nodes.

```python
def copyRandomList(self, head: "Node") -> "Node":
        oldToCopy = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
```

https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/description/
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
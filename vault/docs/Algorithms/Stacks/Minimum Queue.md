---
---
- Keeps track of the minimum value so far but works like a queue

## Using Two Stacks 
- Worst case pop operation is O(n)
- Keep inbox and outbox
- Append inbox in reverse to outbox if outbox is empty
- During the reversal, the min has to be updated for each pair in outbox
- When inserting, we only consider the minimum in inbox because the outbox is constantly changing. Get_min therefore requires us to consider both stacks


```python
class min_queue:
	def __init__(self):
		self.inbox = self.outbox = []

	def insert(self, x):
		min_inbox = x if not min_inbox else min(x, self.inbox[-1][1])
		self.inbox.append([x, min_inbox])

	def get_min:
		if not self.inbox and not outbox:
			return None
		if not self.inbox:
			return self.outbox[-1][1]
		if not self.outbox:
			return self.inbox[-1][1]
		return min(self.outbox[-1][1],self.inbox[-1][1])

	def remove(self):
		if not self.outbox:
			while self.inbox:
				x = self.inbox.pop()
				min_x = x if not outbox else min(x, self.outbox[-1][1])
				self.outbox.append([x, min_x])
		return self.outbox.pop()
```


## Using Double Ended Queue
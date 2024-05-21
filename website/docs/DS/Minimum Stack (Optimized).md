---
---
## Unoptimized
```python
stack = []
new_min = new_elem if not stack else min(new_elem, stack[-1][1])
stack.append([new_elem, new_min])
```

## Optimized
- Use second stack

```python
class min_stack:
	def __init__(self):
		stack = []
		min_stack = []

	def push(self, x):
		self.stack.append(x)
		if not min_stack or self.get_min() > x:
			self.min_stack.append([x,1])
		else:
			self.min_stack[-1][1] += 1

	def pop(self, x):
		if self.get_min() == self.stack[-1]:
			self.min_stack[-1][1] -= 1
		if self.min_stack[-1][1] == 0:
			self.min_stack.pop()
		self.stack.pop() if stack

	def get_min(self):
		return self.min_stack[-1][0] if min_stack else None

	def top(self):
		return self.stack[-1] if stack else None
```
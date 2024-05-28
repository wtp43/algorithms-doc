---
dg-publish: true
---
# Frequent Errors

```python
A = [1, 2, 3] 

B=A # Beware! Both variables refer to the same object

A = [1, 2, 3] B = A[:] # B becomes a distinct copy of A

M = [[0] * 10] * 10 # Do not write this!

# Correct matrix initialization
M1 = [[0] * 10 for _ in range(10)] 
M2 = [[0 for j in range(10)] for i in range(10)]

```

# List Operations

```python
arr.sort()
arr.count(x)
arr.remove(x)
```

# Math

```python
# if x is a float
int(x) == floor(x)
```
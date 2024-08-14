---
---
# Intervals/Scheduling

- [ ] https://leetcode.com/problems/remove-covered-intervals/
- [ ] https://leetcode.com/problems/task-scheduler/description/



### [1094. Car Pooling](https://leetcode.com/problems/car-pooling/)
- Separate pickup and drop off timestamps
- Easier to process individual events
- Sort in a way that drop offs are processed first
```python 
def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
	timestamp = []
	for n,f,t in trips:
		timestamp.append([f,n])
		timestamp.append([t,-n])
	# this sort works because dropoffs are processed first
	timestamp.sort()
	used = 0
	for time, n in timestamp:
		used += n
		if used > capacity:
			return False
	return True
          
```
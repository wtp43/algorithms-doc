---
---
# Graphs

# Topological Search

## Intuition
### Identifying Cycles


- [ ] Prims

- [ ] Kruskals
- [ ] Dijkstras
- [ ] Topological Sort

- [ ] Strongly Connected Components
- [ ] https://emre.me/algorithms/tarjans-algorithm/

- [ ] Floyd Warshall
	- [ ] https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
	- [ ] https://leetcode.com/problems/evaluate-division/
	- [ ] https://leetcode.com/problems/cheapest-flights-within-k-stops/
	- [ ] https://leetcode.com/problems/course-schedule-iv/
	- [ ] https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/
- [ ] Bellman Ford
- [ ] Network Flow
- [ ] Hierholzer's Algorithm for Eulerian Circuits
	- [ ] https://leetcode.com/problems/reconstruct-itinerary/
- [ ] A* Search
	- [ ] https://leetcode.com/problems/sliding-puzzle/
- [ ] Kosaraju's
- [ ] Flood Fill Algo
- [ ] Euler's and Hamilton's Algo
- [ ] Ford Fulkerson
- [ ] Kahn's
- [ ] Max Flow, Min-Cut
	- [ ] https://leetcode.com/problems/maximum-students-taking-exam/
- [ ] Articulation Points and Bridges
	- [ ] https://leetcode.com/problems/critical-connections-in-a-network/





## DFS


Start DFS for every connected component. Make sure to mark connected components
When building out adjacency lists  for directed graphs, we need to make sure the directions are correct. In the case of course schedule, we want the courses to point to prerequisites because this tells us which prerequisites are needed.

In BFS, we need to do a check prior to adding the node to the queue. In DFS, it may not always be necessary to do a pre-check, we can check in the base case of the function call.

- [x] [[LC-1971. Find if Path Exists in Graph]] (Valid Path)
- Union find and connect all edges. 
	- Check if find(source) == find(destination) are the same. Don't check the parents because the path may not have been flattened yet.
- DFS
	- return True if cur_node == destination
	- For all neighbors of cur_node
		- if dfs(neighbor)
			- return True
	- return False



- [x] [[LC-200. Number of Islands]]
- '1' is marked as land while '0' is water
- Start DFS at every '1' while marking them as '0' to indicate they are visited
- Increment number of islands every time dfs is started at '1'

- [ ] [[LC-695. Max Area of Island]]
- Start DFS at every '1' and mark them as visited
- Recursively sum up the area of the island by returning 1 + dfs(all dirs)

- [ ] [[LC-417. Pacific Atlantic Water Flow]] 
- (Starting dfs such that the results can be reused in the next dfs call)
- Find all the squares that flow to and from the pacific/atlantic
The naive approach would be to BFS from each cell. It repeats computation because any result can only be applied to that cell. Start from the ocean(outer borders) and work backwards. The results here are used for multiple cells because every cell we visit must be connected to the ocean. 

- [ ] [[LC-994. Rotting Oranges]] (Parallel BFS)
- Since one fresh orange can be affected by multiple oranges, we want to find the shortest time in which it will be affected. 
- We need to modify our BFS to run in parallel. We can do this by keeping track of which iteration we are on using a delimiter in the queue and starting BFS at all rotten oranges. 
- Instead of a delimiter, we can also iterate the length of the current queue.

- [ ] [[LC-207. Course Schedule]]
- Cycle detection but in a directed graph
- We can use topological sort which implements DFS
	- We have three states: unvisited, currently visiting, visited
	- A cycle is detected if we reach a node that we are currently visiting
- Append, the 
- Direction is important: Since this is a one to many relationship ``[course, prerequisite1], we need to build our edges directed in this way: graph[i].append(j)

- [ ] [[LC-286. Walls and Gates]] (Parallel BFS)
- We want to find the distance from every empty cell to the nearest gate. 
- Instead of running DFS from every gate and taking the min (this results in extra computation), run BFS in parallel starting from each gate. 
- Thus we are guaranteed the shortest route. The distance to the cell is only updated if it is not inf and in the case it isn't, we know we have already visited it taking a shorter path.
- To run BFS in parallel, use a for loop to pop all items in the q at the current state with dist = i. After all these are popped increment dist
- We need to add the neighbor to the visited set immediately, before we actually visit it or we will end up visiting it twice. For example, the first layer adds 1 as the last neighbor. In the second layer, the first node can add 1 to the queue again because 1 hasn't been visited. This means we are not using the shortest path. 
```python
while q:
	for _ in  range(len(q)):
		next = q.pop()
		cell[i][j] = dist
		seen.add((i,j))
		for x,y in dirs:
			row = i+x
			col = j+y
			if (row,col) in seen or (row and col out of bounds):
				continue
			q.append((row,col))
			# ADD NODE BEFORE WE VISIT IT
			seen.append((row,col))

	dist += 1
	
```

## BFS (Shortest path)
BFS is more useful than DFS in cases where we are interested in the shortest path.

- [ ] [[LC-787. Cheapest Flights Within K Stops]]
	- Dijkstra wouldn't be the best solution here because we are limited to k steps.
	- We can run BFS: O(N + EK). In BFS: we have to pass the distance to the queue otherwise we may accidentally use the shortest distance ``(dist[city])`` that takes a different path because ``dist[city]`` may have been updated earlier by a different node.
	- This is also similar to Bellman Ford but relaxing only k+1 times: O((N+E)K) The N comes from swapping the temp and dist array after each round of relaxing all edges. If we do not store our previous result, we will accidentally use more than K steps.

- [ ] [[LC-1129. Shortest Path with Alternating Colors]]
- BFS since we want the shortest path from source=0 to all vertices
- Since we can only take alternating edges, we need to store the prev color of the edge that took us to the current node
	- u,prev_col = q.popleft()
- trick: we can visit a node twice either through a red edge or blue edge
- then we should store (v,col) in seen instead of just v

## Shortest Path
- [ ] https://leetcode.com/problems/network-delay-time/description/

# Connected Components
[[LC-305. Number of Islands II]] (Connected Components)
- grid of 0's initially, Perform land operations which turns water to land, Return number of islands
- Instead of storing parents as a 2d grid, we can store their land position as $i*n + m$
- Components: either dfs or union find (faster than dfs)
- Initializing the parent and rank arrays is O(mn)
- Store the number of connected components and decrement it every time a valid union-set is completed.
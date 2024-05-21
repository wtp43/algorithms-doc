---
---
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


## Union Find (Cycle detection)
Works for undirected graphs
[LC-684. Redundant Connection](</docs/Algos Practice/Leetcode Questions/LC-684. Redundant Connection.md>)- This is the case where the tree has no cycles and is an undirected graph. Then we just need to remove one of the two edges that make up the node with indegree 2.
- Use union find to detect if nodes u,v in the edge (u,v) have the same parent. If they do, this edge is redundant

[LC-685. Redundant Connection II](</docs/Algos Practice/Leetcode Questions/LC-685. Redundant Connection II.md>)-  A valid graph in this context is a single rooted tree (directed graph) with no cycles. This graph is given a single extra edge.
- An edge that is redundant if it is one of two edges that enter the same node or an edge in a cycle. In the case that both scenario happens, we need to remove the edge inside the cycle otherwise it only solves one of the two problems.
- Since we are not sure which edge to remove to ensure that the node has indegree of 1, we have to keep track both edges. We want to remove the edge that is part of a cycle if there exists one. 
- It will help to store the previous node of each node in a dictionary.
- Union find will help us detect the cycle

[LC-261. Graph Valid Tree](</docs/Algos Practice/Leetcode Questions/LC-261. Graph Valid Tree.md>)- A valid tree has 1 connected component with no cycles
- Reduces to redundant connection
- An extra check is required at the end to see if the edges have connected all the components

[LC-323. Number of Connected Components in an Undirected Graph](</docs/Algos Practice/Leetcode Questions/LC-323. Number of Connected Components in an Undirected Graph.md>)- Union find
- Reduce the number of connected components every time we take the union of nodes u and v


## DFS


Start DFS for every connected component. Make sure to mark connected components
When building out adjacency lists  for directed graphs, we need to make sure the directions are correct. In the case of course schedule, we want the courses to point to prerequisites because this tells us which prerequisites are needed.

In BFS, we need to do a check prior to adding the node to the queue. In DFS, it may not always be necessary to do a pre-check, we can check in the base case of the function call.

[LC-1971. Find if Path Exists in Graph](</docs/Algos Practice/Leetcode Questions/LC-1971. Find if Path Exists in Graph.md>)- Union find and connect all edges. 
	- Check if find(source) == find(destination) are the same. Don't check the parents because the path may not have been flattened yet.
- DFS
	- return True if cur_node == destination
	- For all neighbors of cur_node
		- if dfs(neighbor)
			- return True
	- return False



[LC-200. Number of Islands](</docs/Algos Practice/Leetcode Questions/LC-200. Number of Islands.md>)- '1' is marked as land while '0' is water
- Start DFS at every '1' while marking them as '0' to indicate they are visited
- Increment number of islands every time dfs is started at '1'

- [ ] [[LC-695. Max Area of Island]]
- Start DFS at every '1' and mark them as visited
- Recursively sum up the area of the island by returning 1 + dfs(all dirs)

[LC-417. Pacific Atlantic Water Flow](</docs/Algos Practice/Leetcode Questions/LC-417. Pacific Atlantic Water Flow.md>)- (Starting dfs such that the results can be reused in the next dfs call)
- Find all the squares that flow to and from the pacific/atlantic
The naive approach would be to BFS from each cell. It repeats computation because any result can only be applied to that cell. Start from the ocean(outer borders) and work backwards. The results here are used for multiple cells because every cell we visit must be connected to the ocean. 

[LC-994. Rotting Oranges](</docs/Algos Practice/Leetcode Questions/LC-994. Rotting Oranges.md>)- Since one fresh orange can be affected by multiple oranges, we want to find the shortest time in which it will be affected. 
- We need to modify our BFS to run in parallel. We can do this by keeping track of which iteration we are on using a delimiter in the queue and starting BFS at all rotten oranges. 
- Instead of a delimiter, we can also iterate the length of the current queue.

[LC-207. Course Schedule](</docs/Algos Practice/Leetcode Questions/LC-207. Course Schedule.md>)- Cycle detection but in a directed graph
- We can use topological sort which implements DFS
	- We have three states: unvisited, currently visiting, visited
	- A cycle is detected if we reach a node that we are currently visiting
- Append, the 
- Direction is important: Since this is a one to many relationship ``[course, prerequisite1], we need to build our edges directed in this way: graph[i].append(j)

[LC-286. Walls and Gates](</docs/Algos Practice/Leetcode Questions/LC-286. Walls and Gates.md>)- We want to find the distance from every empty cell to the nearest gate. 
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

[LC-1129. Shortest Path with Alternating Colors](</docs/Algos Practice/Leetcode Questions/LC-1129. Shortest Path with Alternating Colors.md>)- BFS since we want the shortest path from source=0 to all vertices
- Since we can only take alternating edges, we need to store the prev color of the edge that took us to the current node
	- u,prev_col = q.popleft()
- trick: we can visit a node twice either through a red edge or blue edge
- then we should store (v,col) in seen instead of just v

## Shortest Path
- [ ] https://leetcode.com/problems/network-delay-time/description/

# Connected Components
[LC-305. Number of Islands II](</docs/Algos Practice/Leetcode Questions/LC-305. Number of Islands II.md>)- grid of 0's initially, Perform land operations which turns water to land, Return number of islands
- Instead of storing parents as a 2d grid, we can store their land position as $i*n + m$
- Components: either dfs or union find (faster than dfs)
- Initializing the parent and rank arrays is O(mn)
- Store the number of connected components and decrement it every time a valid union-set is completed.
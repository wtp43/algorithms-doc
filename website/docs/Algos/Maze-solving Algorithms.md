---
title:  "Maze solving Algorithms"
created: 2023-01-05
---




# Maze solving Algorithms

# Wall Follower
[![](https://upload.wikimedia.org/wikipedia/commons/f/f7/Maze01-02.png)](https://en.wikipedia.org/wiki/File:Maze01-02.png)
Uses the right hand rule. If all the walls are connected together or to the maze's outer boundary, then by keeping one hand in contact with one wall of the maze, the solver is guaranteed to not get lost and will reach a different exit if there is one.

Wall-following should start at the entrance to the maze. If the maze is not simply-connected and one begins wall-following at an arbitrary point inside the maze, one could find themselves trapped along a separate wall that loops around on itself containing no entrances or exists. The starting point should be marked so you can conclude if a cycle exists.

Disjoint mazes can be solved with the wall follower method so long as the entrance and exit are on the outer walls of the maze.

Implemented using a depth-first in-order tree traversal

# Pledge Algorithm
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Pledge_Algorithm.png/220px-Pledge_Algorithm.png)](https://en.wikipedia.org/wiki/File:Pledge_Algorithm.png)
Left: Left-turn solver trapped   
Right: Pledge algorithm solution

Choose an arbitrary direction to go toward.

# Implementation

```python

```

## Optimizations

## Optimized Complexity

:::Time-Complexity[Time Complexity] 


:::

:::Space-Complexity[Space Complexity] 


:::



# Related
[LC-489. Robot Room Cleaner](</docs/Algos Practice/Leetcode Questions/LC-489. Robot Room Cleaner.md>)- https://en.wikipedia.org/wiki/Maze-solving_algorithm#Wall_follower

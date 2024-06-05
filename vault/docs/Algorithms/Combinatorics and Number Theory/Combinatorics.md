---
---
# Combinatorics
- [x] https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/description/
- There are n monkeys at pos i in an array. 
- Each monkey must move once
- If they move in opposite directions, a collision happens.
- Return the number of collisions
- Is it easier to count the number of collisions or no collisions?
- No collisions = 2 for any n, because monkeys can all move cw or ccw
- Situations with collisions = $2^n - 2$

- [x] https://leetcode.com/problems/unique-paths/solutions/504514/unique-paths/
- [ ] In other words, we're asked to compute in how many ways one could choose p elements from p+k elements. In mathematics, that's called [binomial coefficients](https://en.wikipedia.org/wiki/Binomial_coefficient)
- [ ] The problem is a classical combinatorial problem: there are h+v moves to do from start to finish, h=m−1 horizontal moves, and v=n−1 vertical ones. One could choose when to move to the right, i.e. to define h horizontal moves, and that will fix vertical ones. Or, one could choose when to move down, i.e. to define v vertical moves, and that will fix horizontal ones.


![[Pasted image 20230203202802.png]]

- [ ] https://leetcodethehardway.com/tutorials/math/combinatorics




## DP
- Useful for aggregating multiple combinations/permutations

### Count number of answers 'with some conditions' that end in 'X'
https://leetcode.com/problems/student-attendance-record-ii/solutions/101639/pure-math-and-easy-to-understand-python-o-n-solution/

### DFS with States
https://leetcode.com/problems/student-attendance-record-ii/description/


### Count in Valid Intervals
https://leetcode.com/problems/plates-between-candles/description/
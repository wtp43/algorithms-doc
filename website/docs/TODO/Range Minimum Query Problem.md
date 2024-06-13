---
---
Given an array _A_`[1 … n]` of n objects taken from a [totally ordered](https://en.wikipedia.org/wiki/Total_order "Total order") set, such as integers, the range minimum query RMQ_A_(_l_,_r_) =``arg min A[k]`` (with 1 ≤ _l_ ≤ _k_ ≤ _r_ ≤ _n_) returns the position of the minimal element in the specified sub-array `A[l … r]`.

For example, when ``A =[0,5,2,5,4,3,1,6,3]``, then the answer to the range minimum query for the sub-array `A[3 … 8] = [2,5,4,3,1,6]` is 7, as `A[7] = 1`.

# Solution
[Sparse Table](</docs/Algorithms/Advanced Data Structures/Sparse Table.md>)
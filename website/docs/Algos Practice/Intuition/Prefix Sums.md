---
---
Helps in subarray problems because subarrays are made up of contiguous elements

Useful for sum of ranges.
sum i to j = `prefix[j] - prefix[i-1]

Subarray sum = k? 
- prefix sum
- we are essentially looking to see if the prefix sum: `prefix_sum[i]-k` exists.

# Questions
Remember to initialize the base cases fore the prefix sums.

# Use the help of a hashmap
These questions are an extension of twosum.
We use a hashmap to find if a previous prefix_sum exists.

[[LC-560. Subarray Sum Equals K]]
- We have to store a counter for the number of prefix sums because you can add a 0 to the same subarray and get a new subarray with the same sum.
	- Take this example:  5,  2,  2,  0,  3
	- For k = 3, we can take the subarray (0,3) or (3)
- We want to see if we can jump from index 0 to index `prefix_sum[i]-k` for every i
- Initialize `prefix_sum[0]=1` for the case that we use the entire prefix_sum

[[LC-523. Continuous Subarray Sum]]
- Reduces to subarray sum equals k. 
- Initialize `prefix_sums[0] = 1` for the case that we use the entire prefix_sum

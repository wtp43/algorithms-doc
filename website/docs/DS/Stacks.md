---
---
# Stacks
Problems that require a stack are generally greedy.
Aside from scheduling which requires sorting, most of these problems take advantage of not requiring a sorted order. We input items onto a stack until we reach an item that invalidates previous entries. Pop all non-optimal items until you reach one that is optimal, then append the current item.

After every pop, it's important to update our results and if need be, push the updated results back onto the stack.
This is common when merging intervals (stock span, largest rectangle in histogram).

Always remember to clear non empty stack at the end of loops

## Useful tools we can make with stacks
- Monotonically inc/dec stacks
- Strictly inc/dec stacks
	- We build stacks in such a way that the top of the stack guarantees that we have the smallest/largest number
- Min/max stacks
	- Augmented stack that tells us the minimum/maximum in the history
- Monotonic queues + prefix sums

- [ ] [[LC-84. Largest Rectangle in Histogram]]
- Greedy algorithm:
	- We want to use as many bars as possible
	- We can use the entirety of the current bar if the previous bars are all higher
	- Popping criteria: we can only partially use the previous bars if the current bar's height is higher
	- We cannot extend a bar if the next bar is shorter. In this case, we calculate the maximum area using all the previous bars that are taller than the current bar. Pop  all previous bars while simultaneously calculating the area using the current height and the number of bars higher than it that have been popped.

[LC-735. Asteroid Collision](</docs/Algos Practice/Leetcode Questions/LC-735. Asteroid Collision.md>)- Asteroid collisions where the larger of the asteroid stays intact, negative moves left, positive moves right
- Store a stack of asteroids that we have already processed
- Compare the top of the stack with the current asteroid
	- Enumerate all possibilities
	- Crash is only possible if cur asteroid < 0 < stack[-1]
	- Then append the asteroid only if the last popped asteroid was not equal to it in size
		- Very useful to use while else, if we break then we don't go to the else

[LC-402. Remove K Digits](</docs/Algos Practice/Leetcode Questions/LC-402. Remove K Digits.md>)- Remove k digits to get the smallest number
[LC-84. Largest Rectangle in Histogra](</docs/Algos Practice/Leetcode Questions/LC-84. Largest Rectangle in Histogram.md>)- We want to pop everything before the current item if cur_item < stack[-1]
- Both these algorithms are greedy.
	- It's important to figure out the criteria of when to add and pop to the stack
	- In this question, we want to pop a number from the resulting number stack if the cur number is smaller than the prev
	- It's also important that we iterate list to right.
		- For instance A = 1axxx, B = 1bxxx. If a > b then A > B
- There is however 1 case that doesn't work, monotonically increasing, which we need to handle separately
- Wrong intuition: keep a stack of the largest numbers in increasing order and remove the last number. However, this is reduced to "the largest k numbers which is O(nlogn)". The one difference here is that we do not care about the order. So we deduce that this problem should be solved in O(n). Generally for stacks, we just care about the current and previous number. If the condition is met, we can continuously compare and pop from the stack until the condition is broken.
![Pasted-image-20230124003324.png](</Algos-Practice/Leetcode-Questions/attachments/Pasted-image-20230124003324.png>)

[LC-901. Online Stock Span](</docs/Algos Practice/Leetcode Questions/LC-901. Online Stock Span.md>)	- Why do we start from the back?
	- Because traversing from the future means we know for sure the maximum price in the future. 
	- Traversing from the past means we do not know the future

```python
class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        span = 1
        while self.s and price >= self.s[-1][0]:
            span += self.s.pop()[1]
            
        self.s.append((price,span))
        return span
```
- It's important to push the span back (update) after every pop. 

[LC-456. 132 Pattern](</docs/Algos Practice/Leetcode Questions/LC-456. 132 Pattern.md>)- Since we want i < j < k and nums[i] < nums[k] < nums[j], it would be useful to have the minimum nums[i] at each iteration. 
- Then we iterate the array backwards 
	- if nums[j] <= min_array[j]
		- continue, because we dont have a valid nums[i] to use
	- while our stack of nums[k] <= min_array[j]
		- stack.pop() until we have a valid nums[k]
		- because the solution we are searching for requires nums[k] < nums[j], we know that our stack is a in min stack otherwise we would have found a solution already
	- check if stack and stack[-1] < nums[j]. Then we have a valid k and i
	- Append the current j to the stack

[LC-394. Decode String](</docs/Algos Practice/Leetcode Questions/LC-394. Decode String.md>)- To convert a string '100' to integer: k = k * 10 + int(c)
	- Another way is to store the a num stack with delimiter [#,1,0,0,#]
- The hard part is dealing with nested strings
	- Every time we reach a ``'['``  , we need to push the current string back onto the stack
	- When we reach ``']'``, we need to process both the current string and the string on the top of the stack together

- [ ] [[LC-1209. Remove All Adjacent Duplicates in String II]]
Bruteforce: O($n^2$/k)
- Time complexity: Think about what happens after k deletions? How long will the string be?: n-k. How many deletions can we do?: n/k. In the worst case, we do n/k deletions and we have to start from the beginning to see if new adjacent duplicates were created because of the deletion.
- We scan the string no more than n/k times
	iterate through the string:
-   If the current character is the same as the one before, increase the count.
    -   Otherwise, reset the count to `1`.
-   If the count equals `k`, erase last `k` characters.
- If the length of the string was changed, repeat starting from the first step.
What are some generic string properties?
- Index, consecutive frequency, character
Character and consecutive frequency will be useful here to help us rebuild the string
One property to note is that, it is not possible for multiple merges after one delete
- ie: bbb - bb - ccc - b, for k = 3
- This is because bbb would have already been deleted. Thus, we only have to look at the top of the stack after deleting

[LC-32. Longest Valid Parentheses](</docs/Algos Practice/Leetcode Questions/LC-32. Longest Valid Parentheses.md>)What is important? Where the last valid open bracket was.
Thus, we should store the index.
When we can update the longest valid parenthesis?
When we have popped an open bracket off the stack.
How do we know we've popped an open bracket?
We store the last invalid index before the next opening bracket at the start of the stack.
Length = j-i+1
This is because j and i are indices. (j-i) just gives us the difference.

[LC-85. Maximal Rectangle](</docs/Algos Practice/Leetcode Questions/LC-85. Maximal Rectangle.md>)![](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)
[LC-84. Largest Rectangle in Histogra](</docs/Algos Practice/Leetcode Questions/LC-84. Largest Rectangle in Histogram.md>)
To find all the rectangles, we have to look at every possible i,j. So the BTTC is O(NM).
To build our bars for the histogram, we can set the current row as the y axis and use DP. If the current cell is a 0, we cannot reuse the height form the previous rows, otherwise we can extend the bar.


# Monotonic Stack
https://leetcode.com/problems/daily-temperatures/description/




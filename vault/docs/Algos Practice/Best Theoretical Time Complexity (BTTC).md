---
---

# Identify the Best Theoretical Time Complexity of the solution
- The BTTC of finding the sum of numbers in array is O(n) because you have to look at every value in the array at least once
- The BTTC of finding the number of groups of anagrams is O(nk) where n is the number of words and k is the maximum number of letters in a word because you have to look at each word at least once and look at each character in each word at least once
- The BTTC of finding the number of islands in a matrix is O(nm) where n is the number of rows and m is the number of columns because you have to look at each cell in the matrix at least once


 Identify overlapping and repeated computation​
A naive/brute force solution often executes the same operation over and over again. When the code is doing an expensive operation that has been done before, take a moment to step back and consider if you can reuse results from previous computations. Dynamic programming (DP) is the most obvious type of questions you can entirely leverage past computations. There are non-DP questions that can leverage this technique too, although not as straightforward and might require a preprocessing step.

Example​
The Product of Array Except Self question is a good example of a problem which contains overlapping/repeated work. To get the value for an index, you need to multiply the values at all other positions. Doing this for every value in the array would take O(n2) time. However, see that:

result[n]: Product(nums[0] … nums[n-1]) * Product(nums[n + 1] … nums[N - 1])
result[n + 1]: Product(nums[0] … nums[n]) * Product(num[n + 2] … nums[N - 1])
There's a ton of duplicated work in computing the result[n] vs result[n + 1]! This is an opportunity to reuse earlier computations made while computing result[n] to compute result[n + 1]. Indeed, we can make use of a prefix array to help us arrive at the final solution in O(n) time at the cost of more space.

3. Try different data structures​
Choice of data structures is key to coding interviews. It can help you to reach a solution for the problem, it can also help you to optimize your existing solution. Sometimes it's worth going through the exercise of iterating through the data structures you know once again.

Is lookup time slowing your algorithm down? In general, most lookup operations should be O(1) with the help of a hash table. If the lookup operation in your solution is the bottleneck to your solution's time complexity, more often than not, you can use a hash table to optimize the lookup.

Example​
The K Closest Points to Origin question can be solved in a naive manner by calculating the distance of each point, sorting them and then taking the K smallest values. This takes O(nlog(n)) time because of the sorting. However, by using a Heap data structure, the time complexity can be reduced to O(nlog(k)) as adding/removing from the heap only takes O(log(k)) time when the size of the heap is capped at K elements. Changing the data structure made a whole ton of difference to the efficiency of the algorithm!

4. Identify redundant work​
Here are a few examples of code which is doing redundant work. Although making these mistakes might not change the overall time complexity of your code, you are also evaluated on coding abilities, so it is important to write as efficient code as possible.

Don't check conditions unnecessarily​
These are Python examples where the second check is redundant.

if not arr and len(arr) == 0 - the first check already ensures that the array is empty so there is no need for the second check.
x < 5 and x < 10 - the second check is a subcondition of the first check.
Mind the order of checks​
if slow() or fast() - There are two operations in this check, of varying durations. As long as one of the operations evaluates to true, the condition will evaluate to true. Most computers execute operations in order from left to right, hence it is more efficient to put the fast() on the left.
if likely() and unlikely() - This example uses a similar argument as above. If we execute unlikely() first and it is false, we don't have to execute likely().
Don't invoke methods unnecessarily​
If you have to refer to a property multiple times in your function and that property has to be derived from a function call, cache the result as a variable if the value doesn't change throughout the lifetime of the function. The length of the input array is the most common example. Most of the time, the length of the input array doesn't change, declare a variable at the start called length = len(array) and use length in your function instead of calling len(array) every time you need it.

Early termination​
Early termination. Stop after you already have the answer, return the answer immediately. Here's an example of leveraging early termination. Consider this basic question "Determine if an array of strings contain a string regardless of case sensitivity". The code for it:

def contains_string(search_term, strings):
  result = False
  for string in strings:
    if string.lower() == search_term.lower():
      result = True
  return result


Does this code work? Definitely. Is this code as efficient as it can be? Nope. We only need to know if the search term exists in the array of strings. We can stop iterating as soon as we know that there exists the value.

def contains_string(search_term, strings):
  for string in strings:
    if string.lower() == search_term.lower():
      return True # Stop comparing the rest of the array/list because the result won't change.
  return False


Most people already know this and already do this outside of an interview. However, in a stressful interview environment, people tend to forget the most obvious things. Terminate early from loops where you can.

Minimize work inside loops​
Let's further improve on the example above to solve the question "Determine if an array of strings contain a string regardless of case sensitivity".

def contains_string(search_term, strings):
  for string in strings:
    if string.lower() == search_term.lower():
      return True
  return False


Note that you are calling search_term.lower() once per loop of the for loop! It's a waste because the search_term doesn't change throughout the lifecycle of the function.

def contains_string(search_term, strings):
  search_term_lowercase = search_term.lower()
  for string in strings:
    if string.lower() == search_term_lowercase:
      return True
  return False


Minimize work inside loops and don't redo work you have already done if it doesn't change.

Be lazy​
Lazy evaluation is an evaluation strategy which delays the evaluation of an expression until its value is needed. Let's use the same example as above. We could technically improve it a little bit:

def contains_string(search_term, strings):
  if len(strings) == 0:
    return False
  # Don't have to change the search term to lower case if there are no strings at all.
  search_term_lowercase = search_term.lower()
  for string in strings:
    if string.lower() == search_term_lowercase:
      return True
  return False


This is considered a micro-optimization and most of the time, strings won't be empty, but I'm using it to illustrate the example where you don't have to do certain computations if they aren't needed. This also applies to initialization of objects that you will need in your code (usually hash tables). If the input is empty, there's no need to initialize any variables!


# Reference
https://www.techinterviewhandbook.org/coding-interview-techniques/
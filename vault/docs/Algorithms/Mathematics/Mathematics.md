---
---
# Mathematics

To get the number of items in a range ``[l,r]``: 
- size = r-l+1

- [x] [[LC-367. Valid Perfect Square]] 
- The sqrt of a num is always <= num/2

Combining two numbers without using string concatenation
- [32, 45] -> 3245
```python
def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        i,j = 0,len(nums)-1
        while i <= j:
            if i < j:
                res += nums[i] * pow(10, int(log10(nums[j]))+1)+nums[j]
            else:
                res += nums[i]
            i += 1
            j -= 1
        return res
            
```

- Add two integers into array form
```python
def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            k, num[i] = divmod(num[i] + k, 10)
        return [int(i) for i in str(k)] + num if k else num
```

- Division is transitive

## Min/Max Manhattan Distance using Chebyshev Distance
 >**Chebyshev distance** (or **Tchebychev distance**), **maximum metric**, or **L∞ metric**[[1]](https://en.wikipedia.org/wiki/Chebyshev_distance#cite_note-1) is a [metric](https://en.wikipedia.org/wiki/Metric_(mathematics) "Metric (mathematics)") defined on a [real coordinate space](https://en.wikipedia.org/wiki/Real_coordinate_space "Real coordinate space") where the [distance](https://en.wikipedia.org/wiki/Distance "Distance") between two [points](https://en.wikipedia.org/wiki/Point_(geometry) "Point (geometry)") is the greatest of their differences along any coordinate dimension

https://codeforces.com/blog/entry/57534
**Max difference in a 1D array**
$Gap_x$=$max⁡(x)−min⁡(x)$
**Max Manhattan distance between a bunch of 2D points?**
$\text{Gap}_{x,y}$= $\max(\text{Gap}_{x+y},\text{Gap}_{x-y})$ 
**Max Manhattan distance between a bunch of 3D points?**
$\text{Gap}_{x,y,z} = \max(\text{Gap}_{x+y,z},\ \text{Gap}_{x-y,z}) \\ = \max(\text{Gap}_{x+y+z},\ \text{Gap}_{x+y-z},\ \text{Gap}_{x-y+z},\ \text{Gap}_{x-y-z})$ 

### 1131. Maximum of Absolute Value Expression
https://leetcode.com/problems/maximum-of-absolute-value-expression/description/
Consider the inputs as a set of `[(x[0], y[0], 0), (x[1], y[1], 1), ...]`

```python
```

## Factorization

### Finding kth Factor of n
- Sieve of Eratosthenes
- If n is a perfect square, skip it in the second step since it was already checked in the first loop

```python
def kthFactor(self, n: int, k: int) -> int:
        divisors, sqrt_n = []
        for x in range(1, sqrt_n + 1):
            if n % x == 0:
                k -= 1
                divisors.append(x)
                if k == 0:
                    return x
        
        # If n is a perfect square
        # we have to skip the duplicate 
        # in the divisor list
        if (sqrt_n * sqrt_n == n):
            k += 1
                
        n_div = len(divisors)
        return n // divisors[n_div - k] if k <= n_div else -1
```


## Modular Arithmetic

### First Missing Non-Negative Number
https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/description/

```python
def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = Counter(a % value for a in nums)
        stop = 0
        for i in range(value):
            if count[i] < count[stop]:
                stop = i
	    return value * count[stop] + stop
```




## Number Theory

### Fractions
https://en.wikipedia.org/wiki/Mediant_(mathematics)#Properties
- Mediant Property: $\frac{a}{c} < \frac{a+b}{c+d} < \frac{b}{d}$ 
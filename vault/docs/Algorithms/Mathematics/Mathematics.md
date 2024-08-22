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

## Math

### Arithmetic Sequence Sum
$sum = (A[1] + A[n]) * n/2$ where `A[1], A[n]` are the first and last terms of the sequence and `n` is the length of the sequence

#### Minimum Possible Sum of Array with n distinct positive integers such that no two integers sum to Target
https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/description/
- The only possible integers that break this rule are numbers less than target
- We can take at most target//2 integers
```python
def minimumPossibleSum(self, n: int, target: int) -> int:
	x = target//2
	if n < x:
		return (1+n)*n//2%(10**9+7)
	total = (1+x)*x//2
	n -= x
	return (total+(target+target+n-1)*n//2) % (10**9+7)
```

### GCD for a List of Numbers

Basic Euclidean Algorithm for GCD:

The algorithm is based on the below facts.

If we subtract a smaller number from a larger one (we reduce a larger number), GCD doesn’t change. So if we keep subtracting repeatedly the larger of two, we end up with GCD.
Now instead of subtraction, if we divide the smaller number, the algorithm stops when we find the remainder 0.

gcd(a, b, c) = gcd(a, gcd(b, c))
= gcd(gcd(a, b), c)
= gcd(gcd(a, c), b)

```python
# Euclidean algorithm to find H.C.F of two numbers
# Time complexity of O(log min(x,y)) since larger number is reduced by at least half on each iteration of the algorithm
def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
 
# Some arbitrary list of numbers
l = [2, 4, 6, 8, 16]

num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1, num2)

for i in range(2, len(l)):
    gcd = find_gcd(gcd, l[i])

print(gcd)
```

### LCM
```python
def lcm(x,y):
	return x / gcd(x,y) * y  # divide first to avoid integer overflow
```

### Binary Exponentiation 
- Exponentiation by squaring allows calculating $a^n$ with only $O(logn)$ multiplications instead of $O(n)$ multiplications required by the naive approach
- Split the work using binary representation of the exponent
#### Number of Paths of Length k in a Graph

### Sieve of Eratosthenes

```python
def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

def PrimePairsWithTargetSum(n):
    for p in range(2, n+1):
      if prime[i] and prime[n-i] and i<= n-i:
        res.append([i,n-i])
```

### Prime Factorization
```python
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
```

### Matrix Exponentiation

https://www.geeksforgeeks.org/top-algorithms-and-data-structures-for-competitive-programming/
https://www.geeksforgeeks.org/matrix-exponentiation/

#### Misc

- To check if a number is a palindrome without string conversion:
- Use reverse number
- To get the first digit of a number, we can also do x // 10\*\*int(log10(x))

```python
def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x != 0):
            return False
        reverseX = 0
        y = x
        while y:
            reverseX = reverseX * 10 + y%10
            y //= 10

        # reverse can contain the middle number
        return reverseX == x or x == reverseX//1
```


### Calculating Sqrt(x):
- Bitshift
- Binary search
- Newtons's Method (Fastest)
	- $x_{k+1} = \frac{1}{2}[x_k+\frac{x}{x_k}]$ converges to $\sqrt{x}$ if $x_0 = x$
	- Define the error to be less than 1 and proceed iteratively
	- https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Rough_estimation
```python
def NewtonsWithoutSeedTrimming(self, x: int) -> int:
	if x < 2:
		return x

	x0 = x
	x1 = (x0 + x / x0) / 2
	while abs(x0 - x1) >= 1:
		x0 = x1
		x1 = (x0 + float(x) / x0) / 2

	return int(x1)
```
### Absolute Value Rules

|–a| = |a|
|a| ≥ 0.
Products: |ab| = |a||b|
Quotients: |a / b| = |a| / |b|
Powers: |an| = |a|n
Triangle Inequality: |a + b| ≤ |a| + |b|

### Multiplication Tricks

#### By 11

- ab x 11 = 100a + 10(a+b) + b
- extrapolate for every adjacent pair in abc...z

#### ab x ac with 10 = b + c

- ans: (a x (a+1)) concat (b x c)
- 34 x 36 = 1224

#### Difference of squares: bc x de where d = b+1 and e = 10-c

- bc+e is the number between bc and de which is divisible by 10
- 13 x 27 = (bc+e)^2 - e^2

#### x^2

- x^2 = a x b + c^2
- where a = x+c and b = x-c
- 108^2 = 116 x 100 + 8^2

#### By 5

- Let x = a5 and y = b5
- If a + b is even: z = ab+(a+b)/2, xy = z25
- If a + b is odd: z = ab+(a+b)/2, xy = integer(z)25
- 15 x 25 = 375
- 45 x 125 = 5625

#### Other Tips

- Multiplying by 4 for a large number is equivalent to multiplying it by 2, twice

#### Division with fractions

- 374/25 = 374x2x2 / 100

#### Subtracting without borrowing

- Subtract pairs of digits instead of one to avoid borrowing

#### Fun fact: The remained of an integer n divided by 9 is the same as the sum of the digits of n mod 9

- This does not prove that the answer is correct however

### Principle of Inclusion and Exclusion

- |A ∪ B| = |A| + |B|−|A ∩ B| and |A ∪ B ∪ C| = |A| + |B| + |C|−|A ∩ B|−|A ∩ C|−|B ∩ C| + |A ∩ B ∩ C|.
- Add all intersections with odd size, subtract all intersections with even size
- Building a sequence of multiples for some set of nums
- Divide products of pairs by their gcd

```python
  ab = a*b//gcd(a, b)
  bc = b*c//gcd(b, c)
  ca = c*a//gcd(c, a)
  abc = ab*c//gcd(ab, c)

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

## Definitions
- Idempotent: Denoting an element of a set is unchanged in value when multiplied or otherwise operated on by itself



## Misc

### Josephus Problem/Permutation
> Counting-out game
https://en.wikipedia.org/wiki/Josephus_problem
![[Pasted image 20240708143231.png]]
- DP recurrence relation for n people and every $k^{th}$ person is out: 
	- $f(n,k) = (f(n-1), k) +k)$ mod $n$ with $f(1,k) = 1$ if the positions are 0 indexed
	- `+ k`  because after each iteration, the indices are incremented by k

###  Modular Arithmetic
if a + b = c, then b%c = (-a)%c

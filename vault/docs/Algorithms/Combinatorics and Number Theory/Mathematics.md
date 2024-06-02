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
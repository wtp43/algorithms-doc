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
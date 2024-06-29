# Random Sampling

## Reservoir Sampling
- Randomly sample with equal probability
## Sample k Random Numbers from an Array of Undetermined Size (Streaming)
- Problem: You don't know N (size of the stream) in advance, which means you can't directly generate k random indices
- Two passes are not needed. 
- Append the first k elements to the reservoir
- For all numbers after the first k with index i:
	- Generate a random number `ind` in`[0, i]` 
	- If `ind` is in `[0, k-1]`, replace the element at `ind`
	### Why does this work?
- Prove that every element has P($\frac{1}{n}$) of being picked
#### For the last N-k items
Consider the last item. P(ind < k) = k/n
Then for the second item, P(ind_secondlast < k and ind_last != ind_secondlast) = $k/(n-1) \cdot (n-1)/n = k/n$ 
Prove by induction for the indices k to n.

#### For the first k items
- Probability that the item is picked and not removed later on is $[k/(k+1)] \cdot [(k+1)/(k+2)] \cdot ... \cdot [(n-1)/n] = k/n$

```python
def sample(iterable, k):
    reservoir = []
    for i, x in enumerate(iterable):
        if i < k:
            reservoir.append(x)
        else:
            ind = random.randint(0, i)
            if ind < k:
                reservoir[ind] = x
    return reservoir
```

## [Random Pick Index](https://leetcode.com/problems/random-pick-index/) (Offline: when N is known)
> Pick a random index of a given non unique targets, N is known
- Hash map to store indices of all elements
```python
class Sample:
	def __init__(self, nums: List[int]):
        self.d = defaultdict(list)
        for i,x in enumerate(nums):
            self.d[x].append(i)
    
    def pick(self, target: int) -> int:
        return self.d[target][randint(0, len(self.d[target])-1)]
```

## Weighted Reservoir Sampling (Streaming)

> Pavlos Efraimidis and Paul Spirakis
- Sample from a weighted distribution
- Assign each item a key $k_i$ , let $w_i$ be the weight of that item, let $u_i$ be a random number between 0 and 1.
- $k_i$ is a random number to the $n^{th}$ root where $n$ is the weight of that item in the stream
- $k_i = u_i^\frac{1}{w_i}$ 
- Now keep the top $n$ items ordered by keys where $n$ is the size of your sample

```python
heapq.nlargest(k, items, key=lambda item: math.pow(random.random(), 1/weight(item)))
```


## [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/)
- Since all elements are known, we can build a probability distribution with the given weights
- Use prefix sums of weights and then generate a random float from 0 to 1 
- Binary search on the distribution for the given target = random x total_sum
```python
class Sample:

    def __init__(self, w: List[int]):
        self.distribution = []
        cursum = 0
        for wi in w:
            cursum += wi
            self.distribution.append(cursum)
        self.total = cursum

    def pickIndex(self) -> int:
        target = self.total * random.random()
        ind = bisect_left(self.distribution, target)
        return ind
```


## Distributed Reservoir Sampling 
Source: https://gregable.com/2007/10/reservoir-sampling.html
- Split the input equally across all machines and have them each generate a weighted reservoir sample
- Merge process:
	- You must use the original 'key' weights computed in the first pass
	- For example, If one of your 10 machines processed only 10 items in a size-10 sample, and the other 10 machines each processed 1 million items, you would expect that the one machine with 10 items would likely have smaller keys and hence be less likely to be selected in the final output. If you recompute keys in the final process, then all of the input items would be treated equally when they shouldn't.
	- Why do we expect the there to be larger keys on machines that process more items? Since we only keep the largest keys, more random 

## [Random Pick with Blacklist](https://leetcode.com/problems/random-pick-with-blacklist/) (Offline)
- Given `n` total items, map blacklisted indices in the range `[0, n-len(blacklist)-1]` to whitelisted indices in the range`[n-len(blacklist), n-1]
```python
class Sample:

    def __init__(self, n: int, blacklist: List[int]):
        blacklist = set(blacklist)
        self.mapping = defaultdict(int)
        self.N = n-len(blacklist)
        key = [x for x in blacklist if x < n-len(blacklist)]
        val = [x for x in range(n-len(blacklist), n) if x not in blacklist]
        self.mapping = dict(zip(key, val))

    def pick(self) -> int:
        i = randint(0, self.N-1)
        return self.mapping.get(i, i)
```
---
title:  "Bidirectional Dictionary"
created: 2023-01-22
---

>[!summary]+ Contents
>```toc
>style: number
>min_depth:1
>max_depth:6
>```

# Description
Here is a class for a bidirectional `dict`, inspired by [Finding key from value in Python dictionary](https://stackoverflow.com/questions/7657457/finding-key-from-value-in-python-dictionar) and modified to allow the following 2) and 3).

Note that :

-   1.  The _inverse directory_ `bd.inverse` auto-updates itself when the standard dict `bd` is modified.
-   2.  The _inverse directory_ `bd.inverse[value]` is always a **list** of `key` such that `bd[key] == value`.
-   3.  Unlike the `bidict` module from [https://pypi.python.org/pypi/bidict](https://pypi.python.org/pypi/bidict), here we can have 2 keys having same value, this is _very important_.

# Intuition

>[!danger]+ Intuition

# Implementation
Subclassing dict

```python
class bidict(dict):
    def __init__(self, *args, **kwargs):
        super(bidict, self).__init__(*args, **kwargs)
        self.inverse = {}
        for key, value in self.items():
            self.inverse.setdefault(value, []).append(key) 

    def __setitem__(self, key, value):
        if key in self:
            self.inverse[self[key]].remove(key) 
        super(bidict, self).__setitem__(key, value)
        self.inverse.setdefault(value, []).append(key)        

    def __delitem__(self, key):
        self.inverse.setdefault(self[key], []).remove(key)
        if self[key] in self.inverse and not self.inverse[self[key]]: 
            del self.inverse[self[key]]
        super(bidict, self).__delitem__(key)
```

>[!example]+ 
>```python
bd = bidict({'a': 1, 'b': 2})  
print(bd)                     # {'a': 1, 'b': 2}                 
print(bd.inverse)             # {1: ['a'], 2: ['b']}
bd['c'] = 1                   # Now two keys have the same value (= 1)
print(bd)                     # {'a': 1, 'c': 1, 'b': 2}
print(bd.inverse)             # {1: ['a', 'c'], 2: ['b']}
del bd['c']
print(bd)                     # {'a': 1, 'b': 2}
print(bd.inverse)             # {1: ['a'], 2: ['b']}
del bd['a']
print(bd)                     # {'b': 2}
print(bd.inverse)             # {2: ['b']}
bd['b'] = 3
print(bd)                     # {'b': 3}
print(bd.inverse)             # {2: [], 3: ['b']}



# Related
Source: https://stackoverflow.com/questions/3318625/how-to-implement-an-efficient-bidirectional-hash-table
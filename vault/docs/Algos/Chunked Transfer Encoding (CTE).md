---
title:  "Chunked Transfer Encoding (CTE)"
created: 2023-01-13
---

>[!summary]+ Contents
>```toc
>style: number
>min_depth:1
>max_depth:6
>```

# Description


# Intuition

>[!danger]+ Intuition

# Implementation


```python
class Codec:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        x = len(x)
        # bit AND the last 8 bits 
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        # Since we read the bytes backwards we need to reverse them
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # encode here is a workaround to fix BE CodecDriver error
        return ''.join(self.len_to_str(x) + x.encode('utf-8') for x in strs)
        
    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output
```

>[!example]+ 


# Related

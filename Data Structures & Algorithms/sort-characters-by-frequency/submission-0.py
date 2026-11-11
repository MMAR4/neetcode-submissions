from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        d = sorted(d.items(),key = lambda x: (-x[1],x[0]))
        res =''
        for i in d:
           res += i[0] * i[1]
        return res

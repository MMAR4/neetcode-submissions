from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # method 1
        # return len(s) == len(t) and sorted(s) == sorted(t)
        #method 2
        # if len(s) != len(t):
        #     return False
        # d1 = {}
        # d2 = {}
        # for i in range(len(s)):
        #     d1[s[i]] = d1.setdefault(s[i],0) + 1
        #     d2[t[i]] = d2.setdefault(t[i],0) + 1
        # print(d1,d2)
        # return d1 == d2

        # method 3
        if len(s) != len(t):
            return False 
        arr = [0] * 256
        for c1,c2 in zip(s,t):
            arr[ord(c1)] += 1
            arr[ord(c2)] -=1
        return all(x == 0 for x in arr) 
        # method 4 using counter library
        # return Counter(s) == Counter(t)
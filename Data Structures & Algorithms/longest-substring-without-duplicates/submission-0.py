class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # method 1 brute force
        # maxcount =0
        # for i in range(len(s)):
        #     map1 = set()
        #     count = 0
        #     for j in range(i,len(s)):
        #         if s[j] in map1:
        #             break
        #         if s[j] not in map1:
        #             map1.add(s[j])
        #         count +=1
        #     maxcount = max(count,maxcount)
        # return maxcount
        
        # method 2
        # map1 = {}
        # left =0
        # maxlen = 0
        # for i,ch in enumerate(s):
        #     if ch in map1 and map1[ch] >= left:
        #         left = map1[ch] + 1
        #     map1[ch] = i
        #     maxlen= max(maxlen,i - left + 1)
        #     print(maxlen, ch, map1)
        # return maxlen

        # method 3
        hashset = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l +=1
            hashset.add(s[r])
            res = max(res,r - l +1)
        return res
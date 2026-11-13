class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        # this is brute force (some test cases fails cuz its O(K^2))
        # l = 0
        # n =len(cardPoints)
        # r = n - 1
        # maxi = 0
        # for i in range(k + 1):
        #     sum1=0
        #     for j in range(k - i):
        #         sum1 +=  cardPoints[j]
        #     for j in range(i):
        #         sum1 += cardPoints[n - j - 1]
        #     maxi = max(maxi, sum1)
        # return maxi
        
        #method 2 sliding window 
        # n = len(cardPoints)
        # leftsum= 0
        # for i in range(k):
        #     leftsum += cardPoints[i]
        
        # rightsum = 0
        # maxsum = leftsum
        # for i in range(k):
        #     leftsum -= cardPoints[k - 1 -i]
        #     rightsum += cardPoints[n - 1 - i] 
        #     maxsum = max(maxsum,leftsum + rightsum)
        # return maxsum
        n = len(cardPoints)
        window_size = n - k
        total = sum(cardPoints) 
        currsum = sum(cardPoints[:window_size])
        minsum = currsum
        for i in range(k):
            currsum += cardPoints[window_size + i]
            currsum -=  cardPoints[i]
            minsum = min(currsum,minsum)
        return total - minsum
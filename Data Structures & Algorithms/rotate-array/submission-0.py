class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        # method 1 slicing
        # nums[:] = nums[-k:] + nums[:-k] 

        # method 2 using extra space O(N)
        temp = [0] * n
        j = 0
        for i in range(n-k,n):
            temp[j] = nums[i]
            j +=1
        
        for i in range(n-k):
            temp[j] = nums[i]
            j +=1
        for i in range(n):
            nums[i] = temp[i]

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # method 1 2ms
        # is_zero = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[is_zero], nums[i] = nums[i], nums[is_zero]
        #         is_zero +=1

        # method 2 for easy understanding 7ms
        is_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[is_zero] == 0:
                nums[is_zero], nums[i] = nums[i], nums[is_zero]
                is_zero +=1
            if nums[is_zero] != 0:
                is_zero +=1 

        # method 3
        # index = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[index] = nums[i] 
        #         index +=1
        # while index < len(nums):
        #     nums[index] = 0
        #     index +=1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        hashset = set()
        nums.sort()
        i = 0
        while nums[i] <=0 and i < len(nums)-2:
            l = i +1
            r = len(nums) - 1
            if i >0 and nums[i] == nums[i-1]:
                i +=1
                continue

            while l < r:
                currsum = nums[l] + nums[r] + nums[i]
                if currsum == 0:
                    res.append([nums[l] , nums[r] , nums[i]])
                    l +=1
                    r -=1
                    while l < r and nums[l] == nums[l -1]:
                        l +=1
                    while l < r and nums[r] == nums[r + 1]:
                        r -=1
            
                elif currsum < 0:
                    l +=1
                else:
                    r -=1
            i +=1
        return res
                
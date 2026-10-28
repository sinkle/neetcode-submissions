class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr = [1] * len(nums)
        su = [1] * len(nums)
        
        i = 1
        while i < len(nums):
            pr[i] = pr[i-1] * nums[i-1]
            i += 1

        i = len(nums) - 2
        while i >= 0:
            su[i] = su[i+1] * nums[i+1]
            i -= 1

        res = [None] * len(nums)
        for i in range(len(nums)):
            res[i] = pr[i] * su[i]

        return res
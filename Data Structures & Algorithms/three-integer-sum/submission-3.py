class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_ = len(nums)
        if len_ < 3:
            return []
        sorted_nums = sorted(nums)
        res = set()
        for i in range(1, len_ - 1):
            left, right = 0, len_ - 1
            while left < i < right:
                sum_ = sorted_nums[left] + sorted_nums[i] + sorted_nums[right]
                if sum_ == 0:
                    res.add((sorted_nums[left], sorted_nums[i], sorted_nums[right]))
                    left += 1
                    continue
                elif sum_ < 0:
                    left += 1
                else:
                    right -= 1
            
        return list(res)

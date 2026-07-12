class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        while l < r - 1 :
            i = ((r - l) // 2) + l
            if nums[i] > target:
                r = i
            elif nums[i] < target:
                l = i
            else:
                return i
        return -1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existed_term = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in existed_term:
                existed_term[n] = i
            else:
                return [existed_term[diff], i]

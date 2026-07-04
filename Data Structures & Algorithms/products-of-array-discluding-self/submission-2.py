class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefixes = [1]
        for i in range(1, l):
            prefixes.append(prefixes[i - 1] * nums[i-1])

        postfixes = [1]
        for i in range(1, l):
            postfixes.append(postfixes[i - 1] * nums[-i])

        res = []
        for i in range(l):
            res.append(prefixes[i] * postfixes[l - i - 1])

        return res

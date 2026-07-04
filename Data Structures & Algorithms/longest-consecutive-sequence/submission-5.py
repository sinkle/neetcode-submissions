class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_ = 0
        l = set(nums)
        for n in nums:  
            n_max = 1
            i = 1
            while (n - i) in l:
                n_max += 1
                i += 1

            i = 1
            while (n + i) in l:
                n_max += 1
                i += 1
            
            max_ = max(max_, n_max)
        
        return max_
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        max_seq = 0
        for i, n in enumerate(nums): 
            if n - 1 not in a:           
                temp_max_seq = 1
                curr_val = n
                while curr_val + 1 in nums:
                    temp_max_seq += 1
                    curr_val += 1
                max_seq = max(max_seq, temp_max_seq)
            
        return max_seq




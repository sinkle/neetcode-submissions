class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return self._with_set(nums)

    @staticmethod
    def _with_set(nums: List[int]):
        set_check = set()
        for n in nums:
            if n not in set_check:
                set_check.add(n)
            else:
                return True
        return False 
    
    @staticmethod
    def _by_len(nums: List[int]):
        return len(set(nums)) != len(nums)

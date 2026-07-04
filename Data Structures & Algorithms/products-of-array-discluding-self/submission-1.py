class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.n_square_complexity(nums)
    
    @staticmethod
    def n_square_complexity(nums: List[int]):
        output = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    output[i] *= nums[j]
        return output



        

            

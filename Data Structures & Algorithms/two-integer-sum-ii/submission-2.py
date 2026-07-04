class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self._with_two_pointers(numbers, target)
        # num_dict = {}
        # for i in range(len(numbers)):
        #     a = target - numbers[i]
        #     if a in num_dict:
        #         return [num_dict[a] + 1, i + 1]
        #     num_dict[numbers[i]] = i

        # return []
    
    @staticmethod
    def _with_two_pointers(numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right: 
            sum_ = numbers[left] + numbers[right]
            if sum_ == target:
                return [left + 1, right + 1]
            elif sum_ < target:
                left += 1
            else:
                right -= 1
        return []
            
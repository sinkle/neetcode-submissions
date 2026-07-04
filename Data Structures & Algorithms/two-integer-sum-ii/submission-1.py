class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(numbers)):
            a = target - numbers[i]
            if a in num_dict:
                return [num_dict[a] + 1, i + 1]
            num_dict[numbers[i]] = i

        return []
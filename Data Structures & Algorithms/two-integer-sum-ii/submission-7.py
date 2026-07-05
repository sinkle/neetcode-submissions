class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, 1
        switch = True
        while True:
            a, b = numbers[i], numbers[j]
            if a + b == target:
                return [i+1, j+1]
            elif a + b > target:
                j -= 1
                numbers.pop()
            else:
                if j == len(numbers)-1:
                    i += 1
                else:
                    j += 1
            

    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     i, j = 0, 1
    #     switch = True
    #     while True:

            
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            if not stack or temperatures[stack[-1]] >= t:
                stack.append(i)
            else:

                while stack and (temperatures[stack[-1]] < t):
                    last_stack_i = stack.pop()
                    res[last_stack_i] = i - last_stack_i

                stack.append(i)

        return res
            


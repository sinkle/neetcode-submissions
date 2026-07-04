class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        actions = ('+', '-', '/', '*')
        for t in tokens:
            if t not in actions:
                stack.append(t)
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(str(int(eval(f'{left}{t}{right}'))))

        return int(stack.pop())
        
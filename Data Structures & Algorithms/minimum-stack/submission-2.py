class MinStack:

    def __init__(self):
        self.value = []
        

    def push(self, val: int) -> None:
        self.value.append(val)
        

    def pop(self) -> None:
        self.value.pop()
        

    def top(self) -> int:
        return self.value[-1]
        

    def getMin(self) -> int:
        return min(*self.value) if len(self.value) > 1 else self.value[0]

        

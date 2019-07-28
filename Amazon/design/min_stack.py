class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        elif x <= self.min[-1]:
            self.min.append(x)

    def pop(self) -> None:
        if not self.stack:
            return None 
        value = self.stack.pop()
        if self.min[-1] == value:
            self.min.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]
        
    def getMin(self) -> int:
        if not self.min:
            return None
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
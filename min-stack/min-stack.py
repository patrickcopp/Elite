class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []
        self.minstack.append(999999999999999999999999999999999999)

    def push(self, val: int) -> None:
        if len(self.minstack) > 0 and val <= self.minstack[-1]:
            self.minstack.append(val)
        self.stack.append(val)
        
    def pop(self) -> None:
        if len(self.minstack) > 0 and self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1] if len(self.minstack) > 0 else -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minstack or value < self.minstack[-1]:
            self.minstack.append(value)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.minstack.pop() 
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

minstack = MinStack()
minstack.push(-2)
minstack.push(0)
minstack.push(-3)
minstack.getMin()
minstack.pop()
minstack.top()
minstack.getMin()
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
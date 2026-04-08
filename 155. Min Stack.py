class MinStack:

    def __init__(self):
        self.minstack = []
    def push(self, val: int) -> None:
        if not self.minstack:
            self.minstack.append((val,val))
        else:
            current_min = min(val,self.minstack[-1][1])
            self.minstack.append((val,current_min))

    def pop(self) -> None:
        return self.minstack.pop()

    def top(self) -> int:
        return self.minstack[-1][0]

    def getMin(self) -> int:
        return self.minstack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
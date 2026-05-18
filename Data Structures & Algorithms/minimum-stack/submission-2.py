class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []
        self.current_minimum = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.current_minimum is None or val < self.current_minimum:
            self.current_minimum = val
        self.minimum_stack.append(self.current_minimum)


    def pop(self) -> None:
        self.stack.pop()
        self.minimum_stack.pop()
        if self.stack:
            self.current_minimum = self.minimum_stack[-1]
        else:
            self.current_minimum = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]


"""
#self.current_minimum is redundant, cleaner version:
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minimum_stack:
            self.minimum_stack.append(val)
        else:
            self.minimum_stack.append(min(val, self.minimum_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minimum_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]
"""

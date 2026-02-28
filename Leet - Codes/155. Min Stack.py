class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

    def pop(self) -> None:
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        m = self.stk[0]
        for i in self.stk:
            if i < m:
                m = i
        return m


if __name__ == "__main__":
    obj = MinStack()

    obj.push(3)
    obj.push(5)
    obj.push(2)
    obj.push(1)

    print("Top element:", obj.top())
    print("Minimum element:", obj.getMin())

    obj.pop()

    print("Top after pop:", obj.top())
    print("Minimum after pop:", obj.getMin())

    # Summary:
    # This program implements a stack with push, pop, top, and getMin operations.
    # getMin() iterates through the stack to find the minimum element.
    # All elements are stored in a list, and standard stack operations are applied.
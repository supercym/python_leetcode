# Author: cym

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = None


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_val is None or self.min_val > x:
            self.min_val = x


    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) != 0:
            self.stack = self.stack[:len(self.stack)-1]
        if len(self.stack) == 0:
            self.min_val = None
        else:
            self.min_val = min(self.stack)

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
            return self.stack[len(self.stack)-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

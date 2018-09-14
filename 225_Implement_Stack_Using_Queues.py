# Author: cym

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []


    def push_to_back(self, x):
        self.stack.append(x)

    def pop_from_front(self):
        head = self.stack[0]
        self.stack = self.stack[1:]
        return head

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.push_to_back(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        length = self.size()
        if length > 1:
            for i in range(length-1):
                x = self.pop_from_front()
                self.push_to_back(x)
        return self.pop_from_front()



    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        x = self.pop()
        self.push_to_back(x)
        return x


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.is_empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

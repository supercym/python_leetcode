# Author: cym

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push_to_top(self, x):
        self.queue.append(x)

    def pop_from_top(self):
        x = self.queue[self.size()-1]
        self.queue = self.queue[:self.size()-1]
        return x

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.push_to_top(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        tmp = MyQueue()
        for i in range(self.size()-1):
            x = self.pop_from_top()
            tmp.push_to_top(x)
        ans = self.pop_from_top()
        for i in range(tmp.size()):
            x = tmp.pop_from_top()
            self.push_to_top(x)
        return ans


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        tmp = MyQueue()
        for i in range(self.size()-1):
            x = self.pop_from_top()
            tmp.push_to_top(x)
        ans = self.pop_from_top()
        self.push_to_top(ans)
        for i in range(tmp.size()):
            x = tmp.pop_from_top()
            self.push_to_top(x)
        return ans


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.is_empty()

# Author: cym

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归
        # if head is None or head.next is None:
        #     return head
        # h = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return h

        # 迭代
        if head is None or head.next is None:
            return head
        p1 = head
        p2 = head.next
        p1.next = None
        while p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        return p1

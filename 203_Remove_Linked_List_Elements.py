# Author: cym

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None

        while head.val == val:
            head = head.next
            if head is None:
                return None

        tmp = head
        while tmp and tmp.next:
            while tmp.next.val == val:
                tmp.next = tmp.next.next
                if tmp.next == None:
                    return head
            tmp = tmp.next
        return head

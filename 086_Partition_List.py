# Author: cym

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lt, ge = ListNode(None), ListNode(None)
        node = head
        lthead = lt
        gehead = ge
        while node != None:
            if node.val < x:
                lt.next = node
                lt = lt.next
            else:
                ge.next = node
                ge = ge.next
            node = node.next
        ge.next = None # 防止结果中出现环
        lt.next = gehead.next
        return lthead.next

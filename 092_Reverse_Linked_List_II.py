# Author: cym

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or m == n:
            return head
        pre, cur = None, head
        start, end = ListNode(None), ListNode(None)
        c = 1
        while True:
            if c <= m:
                if c == m:
                    start, end = pre, cur
                pre, cur = cur, cur.next
            elif c <= n:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            else:
                if start is None:
                    head = pre
                else:
                    start.next = pre
                end.next = cur
                break
            c += 1
        return head

        

# Author: cym

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        even = ListNode(None)
        evenHead = even
        node = head
        while node is not None:
            even.next = node.next
            even = even.next
            if node.next is None:
                break
            else:
                node.next = node.next.next
                if node.next is None:
                    break
                else:
                    node = node.next
        if even is not None:
            even.next = None
        node.next = evenHead.next
        return head
                

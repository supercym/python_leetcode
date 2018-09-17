# Author: cym
# 先确定链表中点，将链表后半段翻转，比较前后半段是否相同

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next is None:
            rev = self.reverseList(slow)
        elif fast.next.next is None:
            slow = slow.next
            rev = self.reverseList(slow)
        p1 = head
        p2 = rev
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


    def reverseList(self, head):
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


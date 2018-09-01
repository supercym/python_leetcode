# Author: cym

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        ita = headA
        itb = headB
        while ita and itb:
            if ita.val == itb.val:
                return ita
            else:
                ita = ita.next
                itb = itb.next
                if ita is None and itb is None:
                    return None
                if ita is None:
                    ita = headB
                if itb is None:
                    itb = headA
        return None

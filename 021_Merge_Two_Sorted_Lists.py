# Author: cym
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = ListNode(l1.val)
                l1 = l1.next
                ptr = ptr.next
            else:
                ptr.next = ListNode(l2.val)
                l2 = l2.next
                ptr = ptr.next
        if l1 is None:
            ptr.next = l2
        else:
            ptr.next = l1
        return dummyRoot.next
        # *********  Method 2  **************
        # tmp = []
        # while l1:
        #     tmp.append(l1.val)
        #     l1 = l1.next
        # while l2:
        #     tmp.append(l2.val)
        #     l2 = l2.next
        # tmp.sort()
        # dummyRoot = ListNode(0)
        # ptr = dummyRoot
        # for number in tmp:
        #     ptr.next = ListNode(number)
        #     ptr = ptr.next
        # return dummyRoot.next

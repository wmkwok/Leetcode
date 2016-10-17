# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        while ptr != None:
            tmp = ptr.next.val
            ptr.next.val = ptr.val
            ptr.val = tmp
            ptr = ptr.next.next
        return head

    def walkList(self, head):
        ptr = head
        while ptr != None:
            print ptr.val
            ptr = ptr.next

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)


sol.swapPairs(head)
sol.walkList(head)

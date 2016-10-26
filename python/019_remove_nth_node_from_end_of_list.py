# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        needle = head
        end = head
        for i in range(n-1):
            end = end.next

        while end.next != None:
            needle = needle.next
            end = end.next
            
        needle.next = needle.next.next

        return head
        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

numbers = ListNode(1)
numbers.next = ListNode(2)
numbers.next.next = ListNode(3)
numbers.next.next.next = ListNode(4)
n = 2
sol = Solution()
print sol.removeNthFromEnd(numbers, n)

##Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for each in lists:
            while(each != None):
                heapq.heappush(heap, each.val)
                each = each.next
        while heap:
            print [heapq.heappop(heap) for x in range(len(heap))]
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
t1 = ListNode(1)
t2 = ListNode(2)
t1.next = ListNode(3)
t2.next = ListNode(4)
sol = Solution()
sol.mergeKLists([t1,t2])

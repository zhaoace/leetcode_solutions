# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        points = []
        point = head
        while point:
            points.append(point)
            point = point.next

        # target = points[-n]
        if n == len(points):
            head = head.next            
        else:
            if n == 1:
                points[-1*n-1].next = None
            else:
                points[-1*n-1].next = points[-1*n+1]
        return head

if __name__ == "__main__":
    # solution = Solution()
    # calling_function = getattr(solution,"func")
    # assert 123 == calling_function(123)

    print "PASS!!!"
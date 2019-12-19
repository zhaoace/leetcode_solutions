# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = []
        while l1 :
            l.append(l1.val)
            l1 = l1.next
        while l2 :
            l.append(l2.val)
            l2 = l2.next
        
        l3 = None
        p = None
        for n in sorted(l):
            node = ListNode(n)
            if l3 == None:
                l3 = node
                p = node
            else:
                p.next = node
                p = node
        
        
        return l3

if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"func")
    # assert 123 == calling_function(123)

    print "PASS!!!"


# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

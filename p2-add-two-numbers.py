# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def transNumber(ln):
    n = 0
    g = 0
    while True:
        if ln is None:
            break
        n += ln.val * pow(10,g)
        g += 1
        ln = ln.next
    return n


def transNode(num):
    header = None
    for c in str(num):
        ln = ListNode(int(c))
        if  header == None :
            header = ln
        else:
            ln.next = header
            header = ln
    return header

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return transNode(transNumber(l1) + transNumber(l2))



# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l_answer = ListNode(7)
    l_answer.next = ListNode(0)
    l_answer.next.next = ListNode(8)

    answer =  transNumber(transNode(transNumber(l1) + transNumber(l2)))

    assert answer == 807
    print "PASS!"
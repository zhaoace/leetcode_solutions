# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/count-and-say

def next(s):
    l =[s[0]]
    for c in s[1:]:
        if c == l[-1][0]:
            l[-1] += c
        else:
            l.append(c)

    result = ""
    for x in l:
        result += str(len(x))
        result += x[0]

    return result

def looping(n):
    if n == 1:
        return "1"
    return next(looping(n -1 ))


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return looping(n)
        

if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"countAndSay")
    assert 1211 == calling_function(4)

    print "PASS!!!"
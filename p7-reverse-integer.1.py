# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s =str(x)
        result= None
        if x < 0:
            result=  -1*int(s[1:][::-1])
        else:
            result= int(s[::-1])
    
        if result >= pow(2,31)-1 or result <= -1*pow(2,31):
            return 0
        else:
            return result




if __name__ == "__main__":
    solution = Solution()
    assert 321 == solution.reverse(123)
    assert -321 == solution.reverse(-123)
    assert 21 == solution.reverse(120)
    assert 0 == solution.reverse(-1563847412)
    print "PASS!!!"
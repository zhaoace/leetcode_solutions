# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        if str_x == str_x[::-1] :
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"isPalindrome")
    assert True == calling_function(121)
    assert False == calling_function(-121)
    assert False == calling_function(10)
    print "PASS!!!"
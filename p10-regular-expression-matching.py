# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/regular-expression-matching/

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        m = re.search(p,s)
        if m:
            print m.group()
            if m.group() == s:
                return True
            else:
                return False
        else:
            return False





if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"isMatch")
    assert False == calling_function("a","aa")
    assert True == calling_function("aa","a*")
    assert True == calling_function("","")
    assert True == calling_function("ab",".*")
    assert True == calling_function("aab","c*a*b")
    assert False == calling_function("mississippi","mis*is*p*.")
    print "PASS!!!"
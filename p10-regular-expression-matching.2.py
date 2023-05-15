# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/regular-expression-matching/

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i_s = 0
        i_p = 0
        len_s = len(s)
        len_p = len(p)

        print "----------------> s: %s, p: %s " % (s, p)
        while i_p < len_p and i_s < len_s:
            print "p:", p, ", s:", s, 
            print "p[i_p]:", p[i_p] , ", s[i_s]:",  s[i_s] ,
            print "i_p:", i_p , ", i_s:",  i_s 
            if i_p < (len_p - 1) and p[i_p+1] == "*" :
                print "m is true"
                m = True 
            else:
                print "m is false"
                m = False

            
            if not m:
                if p[i_p] == s[i_s]:
                    i_p+= 1
                    i_s += 1
                    continue
                else:
                    print i_s, len_s
                    return i_s == len_s
            else :
                # m = 0
                if p[i_p] != s[i_s]:
                    i_p+= 1
                    continue
                # m = 1 ~ N
                else:
                    if i_s + 1 > len_s :
                        i_s += 1
                        break
                    else:
                        while m:
                            i_s += 1
                            if i_s == len_s:
                                m = False
                                continue
                            if not s[i_s] == p[i_p]:
                                i_p += 2
                                break
                            else:
                                m = False
                                
        return i_s == len_s





if __name__ == "__main__":
    import time
    solution = Solution()
    calling_function = getattr(solution,"isMatch")
    # assert True == calling_function("a","a")
    # assert False == calling_function("aa","a")
    # assert True == calling_function("aaaa","a*")
    # assert True == calling_function("","")
    # assert True == calling_function("ab",".*")
    # assert True == calling_function("aab","c*a*b")
    # assert False == calling_function("mississippi","mis*is*p*.")
    print "PASS!!!"
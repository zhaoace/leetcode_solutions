# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        start = {}
        start["("] = ")"
        start["["] = "]"
        start["{"] = "}"

        end = {}
        end[")"] = "(" 
        end["]"] = "[" 
        end["}"] = "{" 

        stack = []
        for c in s:
            if c not in start.keys() and c not in end.keys():
                return False
            if c in start.keys():
                stack.append(c)
            elif c in end.keys():
                if len(stack) == 0:
                    return False
                if end[c] != stack.pop():        
                    return False
                

        
        if len(stack) != 0 :
            return False
        else :
            return True
        


                    


            





if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"isValid")
    assert True = calling_function("()")
    assert True = calling_function("()[]{}")
    assert False = calling_function("(]")
    assert False = calling_function("([)]")
    assert True = calling_function("{[]}")
    print "PASS!!!"
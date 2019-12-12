# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/string-to-integer-atoi/



INT_MAX = pow(2,31)-1
INT_MIN = -pow(2,31)
class Solution(object):
    
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip(" ")
        my_arr = str.split(" ")
        if my_arr[0] == "" :
            return 0
        # print my_arr

        leading_str = my_arr[0]
        positive_num = 1
        if leading_str[0] == "-" :
            positive_num = -1
            leading_str=leading_str[1:]
        elif leading_str[0] == "+" :
            leading_str=leading_str[1:]
        leading_str = leading_str.lstrip("0")

        
        first_non_digit = None
        for i, c in  enumerate(leading_str):
            if not c in "0123456789":
                first_non_digit = i
                break
        leading_str = leading_str[:first_non_digit]

        try:
            i = int(leading_str) * positive_num
            if i > INT_MAX:
                return INT_MAX
            elif i < INT_MIN:
                return INT_MIN
            return i
        except Exception as e:
            # print "ERROR:", e
            return 0



if __name__ == "__main__":
    solution = Solution()
    callingFunction = getattr(solution,"myAtoi")
    assert 21474836 == callingFunction("21474836++")
    assert 0 == callingFunction("")
    assert -12 == callingFunction("  -0012a42")
    assert 3 == callingFunction("3.14159")
    assert 42 == callingFunction("42")
    assert -42 == callingFunction("    -42")
    assert 4193 == callingFunction("4193 with words")
    assert 0 == callingFunction(" words with 478")
    assert -2147483648 == callingFunction("-91283472332")
    print "PASS!!!"
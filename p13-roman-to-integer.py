# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        trans_num = {
            "I" :1,  
            "IV" :4, 
            "V" :5, 
            "IX" :9, 
            "X" :10, 
            "XL" :40, 
            "L" :50, 
            "XC" :90, 
            "C" :100, 
            "CD" :400, 
            "D" :500, 
            "CM" :900, 
            "M" :1000, 
        }
        result = 0
        print s
        skipFlag = False
        for i in range(0,len(s)):
            print "i:", i
            if skipFlag :
                skipFlag = False
                continue
            if i+1 < len(s) :
                if  str(s[i]) + str(s[i+1]) in trans_num.keys():
                    result += trans_num[str(s[i]) + str(s[i+1])]
                    print "str(s[i]):" +str(s[i]) , "str(s[i+1]):" + str(s[i+1])
                    print "result:" , result
                    skipFlag = True
                    continue
            result += trans_num[str(s[i])]
            print "result:" , result
        return result


if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"romanToInt")
    assert 3 == calling_function("III")
    assert 58 == calling_function("LVIII")

    assert 4 == calling_function("IV")
    assert 9 == calling_function("IX")
    assert 1994 == calling_function("MCMXCIV")

    print "PASS!!!"
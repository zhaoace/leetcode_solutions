# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/integer-to-roman/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        keys = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

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

        result = ""
        for key in keys:
            current_position = int(num/trans_num[key]) if int(num/trans_num[key]) > 0 else None
            print key
            print current_position
            if current_position:
                for cp in range(0,current_position):
                    result += key
                num = num - current_position * trans_num[key]
        print result

        return result

if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"intToRoman")
    
    assert "III" == calling_function(3)
    assert "LVIII" == calling_function(58)
    assert "IV" == calling_function(4)
    assert "IX" == calling_function(9)
    assert "MCMXCIV" == calling_function(1994)

    print "PASS!!!"
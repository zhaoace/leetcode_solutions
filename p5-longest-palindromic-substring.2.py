# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/longest-palindromic-substring/

#encoding = 'utf-8'


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        print "s == ", s

        if s=="":
            return ""

        longest_strings = []
        longest_string = ""
        for i in range(0, len(s)):
            current_longest_string = s[i]
            
            for j in range(0,i+1):
                if i+j+1 > len(s):
                    break
                print "s:",s, "i:",i, "j:",j, 
                print "s[i-j:i+j+1]==" , s[i-j:i+j+1]
                
                if s[i-j] == s[i+j]:
                    current_longest_string = s[i-j:i+j+1]
                    longest_strings[i] = s[i-j:i+j+1]
            if longest_string < current_longest_string :
                longest_string = current_longest_string
            print longest_strings
        
        print "==================> longest_string:",longest_string
        return longest_string
        # for ls in longest_strings:
        #     print ls
            


if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"longestPalindrome")

    assert "bab" == calling_function("babad") or "aba" == calling_function("babad") 
    assert "bb" == calling_function("cbbd")
    assert "" == calling_function("")
    assert "ccc" == calling_function("ccc")
    assert "abccba" == calling_function("abccba")
    assert "abcba" == calling_function("abcbac")
    assert "jtdtj" == calling_function("gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv")

    print "PASS!!!"
# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/longest-palindromic-substring/



def findLongestPalindrome(s):
    # print "--------->", s
    longest = s[0]
    for i in range(0, len(s)):
        # print i, s[:2*i+2]
        if len(s) == 1:
            # print "sublongest = ", longest
            return longest
        if i == 0 :
            if s[0] == s[1]:
                longest= s[:2]
                # print "sublongest = ", longest
                continue
            else:
                longest=s[0]
                # print "sublongest = ", longest
                continue
        if s[0:i+1] == s[i+1:2*i+2][::-1] :
            # print s[:2*i+2]
            longest = s[:2*i+2]
        elif s[0:i] == s[i+1:2*i+1][::-1] :
            # print s[:2*i+1]
            longest = s[:2*i+1]
        
        # print "sublongest = ", longest
    return longest


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=="":
            return ""
        longest = s[0]
        for i in range(0,len(s)):
            sublong = findLongestPalindrome(s[i:])
            if len(sublong) >= len(longest):
                longest = sublong
            # print "longest = ", longest      
        return longest

        

if __name__ == "__main__":
    solution = Solution()

    assert "bab" == solution.longestPalindrome("babad") or "aba" == solution.longestPalindrome("babad") 
    assert "bb" == solution.longestPalindrome("cbbd")
    assert "ccc" == solution.longestPalindrome("ccc")
    assert "abccba" == solution.longestPalindrome("abccba")
    assert "abcba" == solution.longestPalindrome("abcbac")
    assert "jtdtj" == solution.longestPalindrome("gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv")
    print "TIMEOUTED!!!"
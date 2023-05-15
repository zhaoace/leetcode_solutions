# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/



def findNoneDuplicates(s):
    none_dup_string = ""
    for c in s:
        if c not in none_dup_string:
            none_dup_string += c
        else:
            return none_dup_string
    return none_dup_string

class Solution(object):
    def longestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = ""
        for i, c in enumerate(s): 
            none_dup_string = findNoneDuplicates(s[i:])
            if none_dup_string != None :
                len_none_dup_string = len(none_dup_string)
            else:
                len_none_dup_string = 0
            if len_none_dup_string >= len(longest) :
                longest = none_dup_string
        return longest


    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(self.longestSubstring(s))
        



if __name__ == "__main__":
    solution = Solution()
    assert 3 == solution.lengthOfLongestSubstring("abcabcbb")
    assert 1 == solution.lengthOfLongestSubstring("bbbbb")
    assert 3 == solution.lengthOfLongestSubstring("pwwkew")
    assert 1 == solution.lengthOfLongestSubstring(" ")
    assert 2 == solution.lengthOfLongestSubstring("au")
    print "PASS!"
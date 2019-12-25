# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/implement-strstr
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "" :
            return 0
        
        if haystack == needle:
            return 0
        
        
        position = -1
        for i in xrange(len(haystack) -len(needle)+1):
            # print haystack[i]
            if haystack[i] == needle[0] and haystack[i:i+len(needle)]==needle:
                position = i
                break

        return position


if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"strStr")
    assert 2 == calling_function("hello", "ll")
    assert 0 == calling_function("a", "a")
    print "PASS!!!"
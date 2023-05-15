# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = ""
        if len(strs) == 0:
            return ""
        for i,c in enumerate(strs[0]):
            # print c
            # print common_prefix
            for str in strs:
                if i == len(str):
                    return common_prefix
                if str[i] == c:
                    continue
                else:
                    return common_prefix 
            common_prefix += c
        return common_prefix


if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"longestCommonPrefix")
    assert "fl" == calling_function(["flower","flow","flight"])
    assert "" == calling_function(["dog","racecar","car"])
    assert "" == calling_function([])
    assert "a" == calling_function(["aa","a"])
    print "PASS!!!"
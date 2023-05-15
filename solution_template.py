# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/${filename}

class Solution(object):
    def func(self, x):
        """
        :type x: int
        :rtype: int
        """
        return 123


if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"func")
    assert 123 == calling_function(123)

    print "PASS!!!"
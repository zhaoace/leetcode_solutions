# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/search-insert-position

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)


if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"searchInsert")
    assert 2 == calling_function([1,3,5,6],5)
    print "PASS!!!"
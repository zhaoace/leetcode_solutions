# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = len(nums)-2
        while i >= 0:
            # print nums
            # print i
            # print nums[i]
            # print nums[i+1]
            if nums[i] == nums[i+1]:
                del(nums[i+1])
                i-=1
            else:
                i-=1
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"removeDuplicates")
    # assert 123 == calling_function(123)
    print "PASS!!!"
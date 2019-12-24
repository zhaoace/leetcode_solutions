# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/remove-element

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        for i in range(0, len(nums))[::-1]:
            
            if nums[i] == val:
                del(nums[i])
        
        
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"removeElement")
    # assert 123 == calling_function(123)

    print "PASS!!!"
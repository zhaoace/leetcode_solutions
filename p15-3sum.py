# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        print  nums[i], nums[j] , nums[k]
                        current=sorted([nums[i],nums[j],nums[k]])
                        if current not in result:
                            result.append(current)
        print result
        return result


if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"threeSum")
    assert [ [0,0,0] ] == calling_function( [-1, 0, 0, 2, 0])
    assert [ [-1, 0, 1], [-1, -1, 2] ] == calling_function( [-1, 0, 1, 2, -1, -4])

    print "TIMEOUT!!!"
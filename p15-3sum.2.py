# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        print "threeSum:",nums 

        res = []
        nums.sort()
        length = len(nums)

        for i in range(0, length-2):
            if nums[i] > 0: 
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1 
            r = length - 1

            while l < r:
                print nums
                print l, r
                print "nums[i] + nums[l]  + nums[r]: %s , %s , %s" % (nums[i] ,nums[l]  ,nums[r])
                total = nums[i] + nums[l]  + nums[r]
                if total < 0 :
                    l += 1 
                elif total > 0 :
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1] :
                        l+=1
                    while l < r and nums[r] == nums[r-1] :
                        r-=1
                    l+=1
                    r-=1

        print res
        return res


if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"threeSum")
    assert [[-5,1,4],[-5,2,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-2,4],[-2,-1,3],[-2,0,2],[-2,1,1],[-1,-1,2],[-1,0,1]] == calling_function( [-1,-2,-3,4,1,3,0,3,-2,1,-2,2,-1,1,-5,4,-3])
    assert [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]] == calling_function( [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
    assert [ [-2,-1,3],[-2,0,2],[-1,0,1] ] == calling_function( [3,0,-2,-1,1,2])
    assert [ ] == calling_function( [])
    assert [ [0,0,0] ] == calling_function( [0,0,0] )
    assert [ [0,0,0] ] == calling_function( [-1, 0, 0, 2, 0])
    assert [  [-1, -1, 2] ,[-1, 0, 1]] == calling_function( [-1, 0, 1, 2, -1, -4])
    print "PASS!!!"
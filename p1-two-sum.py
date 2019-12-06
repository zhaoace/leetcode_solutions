# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def findPosition(self, num_a, num_b, nums):
        idx1=None
        idx2=None
        for i,num in enumerate(nums):
            if num_a == num and idx1 ==None:
                idx1 =i
            else:
                if num_b==num :
                    idx2 = i
            if idx1 !=None and idx2 !=None:
                return idx1, idx2
            
        
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        target_nums = [target - num for num in nums]
        
        findings =list( set(target_nums) & set(nums))
        
        len_findings = len(findings)
        
        if len_findings == 1:
            return self.findPosition(findings[0],findings[0],nums)
        if len_findings == 2:
            return self.findPosition(findings[0],findings[1],nums)
        if len_findings == 3:
            findings = sorted(findings)
            return self.findPosition(findings[0],findings[2],nums)




if __name__ == "__main__":
    nums = [-3,4,3,90]
    target = 0
    solution = Solution()
    print solution.twoSum(nums, target)

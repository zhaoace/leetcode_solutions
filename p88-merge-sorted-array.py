# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/merge-sorted-array

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        
        j = 0
        for i in range(0,len(nums1)):
            if i < m: 
                continue
            
            nums1[i] = nums2[j]
            j +=1
        
        nums1.sort()
            
            


if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"func")
    # assert 123 == calling_function(123)
    print "PASS!!!"
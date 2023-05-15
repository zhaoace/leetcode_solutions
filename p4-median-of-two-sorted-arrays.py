# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums_all = nums1 + nums2

        nums_all = sorted(nums_all)

        nl = len(nums_all)
        if nl % 2 == 1:
            median_idx = (nl-1)/2
            return nums_all[median_idx]
        else:
            median_idx1 = nl/2-1
            median_idx2 = nl/2          
            return (nums_all[median_idx1] + nums_all[median_idx2])/2.0



if __name__ == "__main__":
    solution = Solution()
    assert 1 == solution.findMedianSortedArrays([1], [])
    assert 2.5 == solution.findMedianSortedArrays([1, 2], [3,4])
    assert 2 == solution.findMedianSortedArrays([1, 3], [2])
    print "PASS!"
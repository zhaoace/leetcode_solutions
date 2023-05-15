# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/container-with-most-water/



class Solution(object):
    def area(self, height, i, j):
        h = height[i] if height[i] < height[j] else height[j]
        return h * (j-i)

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0 
        i = 0
        j = len(height) - 1
        while True:
            current = self.area(height, i, j)
            if current > max:
                max = current
            if height[i] <= height[j]:
                i += 1
            else:
                j -=1
            if i == j:
                break
        return max

if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"maxArea")
    assert 49 == calling_function([1,8,6,2,5,4,8,3,7])

    print "PASS!!!"
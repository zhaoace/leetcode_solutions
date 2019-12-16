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

        length = len(height)
        for i in range(0,length):
            for j in range(i+1, length):
                currentArea = self.area(height, i , j )
                if currentArea >= max:
                    max = currentArea
        return max

if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"maxArea")
    assert 49 == calling_function([1,8,6,2,5,4,8,3,7])

    print "TIMEOUT!!!"
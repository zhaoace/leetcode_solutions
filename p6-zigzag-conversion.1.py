# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/zigzag-conversion/


def printMap(map):
    for i in map.keys():
        for c in map[i]:
            print c,
        print "\n---------------"


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        map = {}
        i_map = 0
        i_map_direction = 1
        result = ""
        for i,c in enumerate(s):
            if map.get(i_map, None) is None:
                map[i_map] = [c]
            else:
                map[i_map].append(c)

            if numRows == 1 :
                i_map = 0
            else:
                i_map = i_map + i_map_direction
                if i_map == numRows-1 or i_map == 0:
                    i_map_direction *= -1
            print "xxxxxxxxxxxxxxxxxxxxxxxxxx"
            printMap(map)
        for x in map:
            result += "".join(map[x])
        print result
        return result


if __name__ == "__main__":
    solution = Solution()
    callingFunction = getattr(solution,"convert")
    assert "PAHNAPLSIIGYIR" == callingFunction("PAYPALISHIRING", 3)
    assert "PAYPALISHIRING" == callingFunction("PAYPALISHIRING", 1)
    assert "PINALSIGYAHRPI" == callingFunction("PAYPALISHIRING", 4)
    print "PASS!!!"
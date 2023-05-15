# https://leetcode.com/zhaoace/
# https://leetcode.com/problems/letter-combinations-of-a-phone-number


digitsMapping = {}
digitsMapping["1"] = None
digitsMapping["2"] = "abc"
digitsMapping["3"] = "def"
digitsMapping["4"] = "ghi"
digitsMapping["5"] = "jkl"
digitsMapping["6"] = "mno"
digitsMapping["7"] = "pqrs"
digitsMapping["8"] = "tuv"
digitsMapping["9"] = "wxyz"
digitsMapping["0"] = " "

def do_it(x):
    # print x
    # print len(x)
    if len(x) > 2 :
        t = []
        t.append(do_it(x[:-1]))
        t.append(x[-1])
        x=t

    res= []
    for i in x[0]:
        for j in x[1]:
            res.append(i+j)
    # print res
    return res

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 0:
            return []


        if len(digits) == 1:
            return [c for c in digitsMapping[digits]]


        input = []
        for c in digits:
            input.append(digitsMapping[c])

        return do_it(input)




if __name__ == "__main__":
    solution = Solution()
    calling_function = getattr(solution,"letterCombinations")
    assert [] == calling_function("")
    assert ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"] == calling_function("23")

    print "PASS!!!"
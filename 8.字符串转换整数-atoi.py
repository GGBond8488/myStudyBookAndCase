#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = []
        nums = ('0','1','2','3','4','5','6','7','8','9')
        maps = {
            '0':0,
            '1':1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9
        }
        begin = True
        sign = True
        for chr in s:
            
            if not begin and chr not in nums:
                break            

            if begin and chr == " ":
                continue

            if begin and chr in ("+","-"):
                sign = False if chr == "-" else True
                begin = False

            if chr in nums: 
                begin = False
                number.append(maps[chr])
            elif begin:
                return 0
          

        ret = 0
        length = len(number)
        for index in range(length):

            ret += number[index]*(10**(length-1-index))
            
            if sign and ret >= 2**31 - 1 :
                return 2**31 - 1
            
            if not sign and ret >= 2**31 :
                return -1 * 2**31


        if not sign:
            ret = -1 * ret

        
        return ret

        

# @lc code=end

sol = Solution()
print(sol.myAtoi("2147483648"))


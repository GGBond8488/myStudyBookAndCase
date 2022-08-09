#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        instack = ['(','[','{']
        outstack = [')',']','}']
        out2in = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for chr in s:
            if chr in instack:
                stack.append(chr)
                #print("in",stack)
                continue
            if chr in outstack:
                if len(stack)>0 and stack[len(stack)-1]==out2in[chr]:
                    stack = stack[:len(stack)-1]
                    #print("out",stack)
                    continue
                else:
                    return False

        #print(stack)
        if len(stack) > 0:
            return False

        return True    
        
# @lc code=end
sol = Solution()

print(sol.isValid("()"))

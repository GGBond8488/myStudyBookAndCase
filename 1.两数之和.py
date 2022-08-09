#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        ret = {}
        for index,num in enumerate(nums):
            if target-num in ret:
                return [ret[target-num],index]
            ret[num]=index
            
        return []
# @lc code=end

s = Solution()
s.twoSum([2,7,11,8],9)
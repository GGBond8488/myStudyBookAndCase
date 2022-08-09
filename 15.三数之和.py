#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self,nums,start,target):
        map = {}
        ret = []
        while start < len(nums):
            num = nums[start]
            if target - num in map:
                ret.append([start, map[target-num]])
            map[num] = start
            start += 1
        return ret

    def threeSums(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        for i, num in enumerate(nums):

            if i > 0 and num == nums[i-1]:
                continue

            if i >= len(nums) - 2:
                break
            l = i + 1
            r = len(nums) - 1 
            target = -1 * num
            #print(nums,target)
            while nums[l] + nums[r] >= target:

                if l >= r :
                    break
                #去重
                if nums[l + 1] == nums[l]:
                    l += 1
                    continue
                if nums[r - 1] == nums[r]:
                    r -= 1
                    continue

                if nums[l] + nums[r] == target and l < r:
                    ret.append([num,nums[l],nums[r]])
                    #print(l,r)

                elif nums[l+1] + nums[r] == target and l+1 < r:
                    ret.append([num,nums[l+1],nums[r]])
                    #print(l+1,r)
                
                elif nums[l] + nums[r-1] == target and l < r-1:
                    ret.append([num,nums[l],nums[r-1]])
                    #print(l,r-1)

                l += 1
                r -= 1
          
        return ret

    def threeSum(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        ans = list()
        
        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans

    def threeSums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        for i, num in enumerate(nums):
            if i > len(nums) - 3:
                break
            tmp = self.twoSum(nums,i+1 ,-1 * num)
            for item in tmp:
                item.append(i)
                item.sort()
                item = [nums[i] for i in item]
                ret.append(item)        
        return ret
# @lc code=end



def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        for i, num in enumerate(nums):

            if i > 0 and num == nums[i-1]:
                continue

            if i >= len(nums) - 2:
                break
            l = i + 1
            r = len(nums) - 1 
            target = -1 * num
            #print(nums,target)
            while nums[l] + nums[r] >= target:

                if l >= r :
                    break
                #去重
                if nums[l + 1] == nums[l]:
                    l += 1
                    continue
                if nums[r - 1] == nums[r]:
                    r -= 1
                    continue

                if nums[l] + nums[r] == target and l < r:
                    ret.append([num,nums[l],nums[r]])
                    #print(l,r)

                elif nums[l+1] + nums[r] == target and l+1 < r:
                    ret.append([num,nums[l+1],nums[r]])
                    #print(l+1,r)
                
                elif nums[l] + nums[r-1] == target and l < r-1:
                    ret.append([num,nums[l],nums[r-1]])
                    #print(l,r-1)

                l += 1
                r -= 1
          
        return ret
                

print(threeSum([-1,0,1,0]))
        


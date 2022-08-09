#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个升序链表
#
# https://leetcode.cn/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (57.11%)
# Likes:    2097
# Dislikes: 0
# Total Accepted:    517.8K
# Total Submissions: 906.2K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
# 
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 
# 
# 示例 2：
# 
# 输入：lists = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：lists = [[]]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):

    def merge(self,list1,list2):
        head = ListNode()

        cur = head

        while list1 and list2 :
            if list1.val >= list2.val:
                cur.next = list2
                list2 = list2.next
            else :
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        
        if list1:
            cur.next = list1
        
        if list2:
            cur.next = list2

        return head.next 

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = len(lists)

        if l == 0:
            return ListNode()

        if l == 1:
            return lists[0]    

        ret = self.merge2part(lists,0,l-1)
        
        return ret

    def merge2part(self, lists, l, r):
        if l == r:
            return lists[l]

        mid = l + r / 2

        return  self.merge(self.merge2part(lists,l,mid),
                            self.merge2part(lists,mid+1,r)
                            )


# @lc code=end


def mergeTwoPart(list1, list2):
        l1 = len(list1) 
        l2 = len(list2)
        if l1 == 1 and l2 == 1:
            return self.merge(list1[0],list2[0])
        if l1 == 1 and l2 == 0:
            return list1[0]
        if l1 == 0 and l2 == 1:
            return list2[0]
        if l1 == l2 == 0:
            return []

        return self.mergeTwoPart(self.mergeTwoPart(list1[:l1/2],list1[l1/2:]),
                                 self.mergeTwoPart(list2[:l2/2],list2[l2/2:]))

def merge(list1,list2):
        head = ListNode()

        cur = head

        while list1 and list2 :
            if list1.val >= list2.val:
                cur.next = list2
                list2 = list2.next
            else :
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        
        if list1:
            cur.next = list1
        
        if list2:
            cur.next = list2

        return head.next 